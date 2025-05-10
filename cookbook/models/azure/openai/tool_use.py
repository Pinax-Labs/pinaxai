"""Run `pip install duckduckgo-search` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.models.azure import AzureOpenAI
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=AzureOpenAI(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Whats happening in France?", stream=True)
