"""Build a Web Search Agent using xAI."""

from pinaxai.agent import Agent
from pinaxai.models.xai import xAI
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=xAI(id="grok-2"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Whats happening in France?", stream=True)
