from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from prompts import story_prompt, prompt_formatted
from dotenv import load_dotenv
import streamlit  as st


load_dotenv()

temperature=0.3
max_output_tokens=2048

def get_gemini_pro_text_response(prompt, prompt_dict):
    llm = ChatGoogleGenerativeAI(model="gemini-pro",
                                 temperature=temperature,
                                 max_output_tokens=max_output_tokens)
    print(prompt)
    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

    response = chain.invoke(prompt_dict)
    return response["text"]

st.header("Story Writing App")
st.subheader("Generate a story")

character_name = st.text_input(
    "Enter character name: \n\n", key="character_name", value="Mittens"
)
character_type = st.text_input(
    "What type of character is it? \n\n", key="character_type", value="Cat"
)
character_persona = st.text_input(
    "What personality does the character have? \n\n",
    key="character_persona",
    value="Mitten is a very friendly cat.",
)
character_location = st.text_input(
    "Where does the character live? \n\n",
    key="character_location",
    value="Andromeda Galaxy",
)
story_premise = st.multiselect(
    "What is the story premise? (can select multiple) \n\n",
    [
        "Love",
        "Adventure",
        "Mystery",
        "Horror",
        "Comedy",
        "Sci-Fi",
        "Fantasy",
        "Thriller",
    ],
    key="story_premise",
    default=["Love", "Adventure"],
)
creative_control = st.radio(
    "Select the creativity level: \n\n",
    ["Low", "High"],
    key="creative_control",
    horizontal=True,
)
length_of_story = st.radio(
    "Select the length of the story: \n\n",
    ["Short", "Long"],
    key="length_of_story",
    horizontal=True,
)

if creative_control == "Low":
    temperature = 0.30
else:
    temperature = 0.95

if length_of_story == "Short":
    max_output_tokens = 1000
else:
    temperature = 2048

generate_story = st.button("Generate my story", key="generate_story")
if generate_story and story_prompt:
    with st.spinner("Generating your story ..."):
        tab1, tab2 = st.tabs(["Story", "Prompt"])
        with tab1:
            response = get_gemini_pro_text_response(story_prompt, prompt_formatted)
            if response:
                st.write("Your story:")
                st.write(response)
        with tab2:
            st.text(story_prompt)