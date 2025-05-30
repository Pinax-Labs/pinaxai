"""Run `pip install duckduckgo-search` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.models.google import Gemini
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-001"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Whats happening in France?", stream=True)
