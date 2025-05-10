from pinaxai.agent import Agent
from pinaxai.media import File
from pinaxai.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    markdown=True,
    add_history_to_messages=True,
)

agent.print_response(
    "Suggest me a recipe from the attached file.",
    files=[File(url="https://pinaxai-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf")],
)
