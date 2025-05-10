from pinaxai.agent import Agent
from pinaxai.media import File
from pinaxai.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    markdown=True,
    add_history_to_messages=True,
)

agent.print_response(
    "Summarize the contents of the attached file.",
    files=[File(url="https://pinaxai-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf")],
)

agent.print_response("Suggest me a recipe from the attached file.")
