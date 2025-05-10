"""
Async example using Claude with tool calls.
"""

import asyncio

from pinaxai.agent import Agent
from pinaxai.models.ibm import WatsonX
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=WatsonX(id="meta-llama/llama-3-3-70b-instruct"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
