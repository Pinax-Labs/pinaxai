"""Run `pip install pinaxai llama-api-client duckduckgo-search` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.models.meta import Llama
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Llama(id="Llama-4-Maverick-17B-128E-Instruct-FP8"),
    tools=[DuckDuckGoTools()],
)
agent.print_response("Tell me the latest news about Llama API")
