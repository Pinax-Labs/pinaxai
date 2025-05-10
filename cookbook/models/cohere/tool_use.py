"""Run `pip install duckduckgo-search` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.models.cohere import Cohere
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Cohere(id="command-a-03-2025"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Whats happening in France?", stream=True)
