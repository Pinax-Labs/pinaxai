"""
Basic streaming async example using DeepSeek.
"""

import asyncio

from pinaxai.agent import Agent
from pinaxai.models.deepseek import DeepSeek

agent = Agent(
    model=DeepSeek(id="deepseek-chat"),
    markdown=True,
)

asyncio.run(agent.aprint_response("Share a 2 sentence horror story", stream=True))
