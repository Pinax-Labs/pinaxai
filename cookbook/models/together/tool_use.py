"""Run `pip install duckduckgo-search` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.models.together import Together
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Together(id="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Whats happening in France?", stream=True)
