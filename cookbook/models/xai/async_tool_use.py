"""Run `pip install duckduckgo-search` to install dependencies."""

import asyncio

from pinaxai.agent import Agent
from pinaxai.models.xai import xAI
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=xAI(id="grok-2"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
