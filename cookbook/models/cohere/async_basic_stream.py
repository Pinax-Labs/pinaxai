"""
Basic streaming async example using Cohere.
"""

import asyncio

from pinaxai.agent import Agent
from pinaxai.models.cohere import Cohere

agent = Agent(
    model=Cohere(id="command-a-03-2025"),
    markdown=True,
)

asyncio.run(agent.aprint_response("Share a 2 sentence horror story", stream=True))
