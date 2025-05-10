"""Run `pip install pinaxai llama-api-client duckduckgo-search` to install dependencies."""

import asyncio

from pinaxai.agent import Agent
from pinaxai.models.meta import Llama
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Llama(id="Llama-4-Maverick-17B-128E-Instruct-FP8"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
)
asyncio.run(agent.aprint_response("What's happening in France?", stream=True))
