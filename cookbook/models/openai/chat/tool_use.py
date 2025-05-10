"""Run `pip install duckduckgo-search` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIChat
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Whats happening in France?")
