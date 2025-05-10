from pinaxai.agent import Agent
from pinaxai.media import File
from pinaxai.models.anthropic import Claude

agent = Agent(
    model=Claude(id="claude-3-5-sonnet-20241022"),
    markdown=True,
)

agent.print_response(
    "Summarize the contents of the attached file.",
    files=[
        File(url="https://pinaxai-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"),
    ],
    stream=True,
)
