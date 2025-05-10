from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIResponses
from pinaxai.tools.file import FileTools

agent = Agent(
    model=OpenAIResponses(id="gpt-4o"),
    tools=[{"type": "web_search_preview"}, FileTools()],
    instructions="Save the results to a file with a relevant name.",
    markdown=True,
)
agent.print_response("Whats happening in France?")
