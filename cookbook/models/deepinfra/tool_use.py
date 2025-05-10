"""Run `pip install duckduckgo-search` to install dependencies."""

from pinaxai.agent import Agent  # noqa
from pinaxai.models.deepinfra import DeepInfra  # noqa
from pinaxai.tools.duckduckgo import DuckDuckGoTools  # noqa

agent = Agent(
    model=DeepInfra(id="meta-llama/Llama-2-70b-chat-hf"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Whats happening in France?", stream=True)
