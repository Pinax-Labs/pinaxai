"""Run `pip install duckduckgo-search` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.models.lmstudio import LMStudio
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=LMStudio(id="qwen2.5-7b-instruct-1m"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Whats happening in France?", stream=True)
