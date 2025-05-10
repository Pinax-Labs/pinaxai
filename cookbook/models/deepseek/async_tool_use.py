"""
Async example using DeepSeek with tool calls.
"""

import asyncio

from pinaxai.agent import Agent
from pinaxai.models.deepseek import DeepSeek
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=DeepSeek(id="deepseek-chat"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
