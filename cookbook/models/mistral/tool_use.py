"""Run `pip install duckduckgo-search` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.models.mistral import MistralChat
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=MistralChat(
        id="mistral-large-latest",
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Whats happening in France?", stream=True)
