from pinaxai.agent import Agent
from pinaxai.media import File
from pinaxai.models.openai.responses import OpenAIResponses

agent = Agent(
    model=OpenAIResponses(id="gpt-4o-mini"),
    tools=[{"type": "file_search"}, {"type": "web_search_preview"}],
    markdown=True,
)

agent.print_response(
    "Summarize the contents of the attached file and search the web for more information.",
    files=[File(url="https://pinaxai-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf")],
)

print("Citations:")
print(agent.run_response.citations)
