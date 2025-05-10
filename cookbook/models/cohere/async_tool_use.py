"""
Async example using Cohere with tool calls.
"""

import asyncio

from pinaxai.agent import Agent
from pinaxai.models.cohere import Cohere
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Cohere(id="command-a-03-2025"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
