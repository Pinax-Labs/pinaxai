"""Run `pip install duckduckgo-search` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.models.aws import AwsBedrock
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=AwsBedrock(id="amazon.nova-lite-v1:0"),
    tools=[DuckDuckGoTools()],
    instructions="You are a helpful assistant that can use the following tools to answer questions.",
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Whats happening in France?", stream=True)
