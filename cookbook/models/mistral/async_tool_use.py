"""
Async example using Mistral with tool calls.
"""

import asyncio

from pinaxai.agent import Agent
from pinaxai.models.mistral.mistral import MistralChat
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=MistralChat(id="mistral-large-latest"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
