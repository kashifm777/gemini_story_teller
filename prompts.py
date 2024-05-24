from langchain.prompts import PromptTemplate

story_template = """Write a {length_of_story} story based on the following premise: \n
character_name: {character_name} \n
character_type: {character_type} \n
character_persona: {character_persona} \n
character_location: {character_location} \n
story_premise: {story_premise} \n
If the story is "short", then make sure to have 5 chapters or else if it is "long" then 10 chapters.
Important point is that each chapters should be generated based on the premise given above.
First start by giving the book introduction, chapter introductions and then each chapter. It should also have a 
proper ending.
The book should have prologue and epilogue.
"""

story_prompt = PromptTemplate(
    input_variables=["length_of_story", "character_name", "character_type", "character_persona", "character_location",
                     "story_premise"],
    template=story_template
)

prompt_formatted = {
    "length_of_story": length_of_story,
    "character_name": character_name,
    "character_type": character_type,
    "character_persona": character_persona,
    "character_location": character_location,
    "story_premise": story_premise,
}