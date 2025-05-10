"""Run `pip install duckduckgo-search` to install dependencies."""

import asyncio

from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIResponses
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIResponses(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
