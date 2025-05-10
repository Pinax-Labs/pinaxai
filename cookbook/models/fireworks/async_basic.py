"""
Basic async example using Fireworks.
"""

import asyncio

from pinaxai.agent import Agent
from pinaxai.models.fireworks import Fireworks

agent = Agent(
    model=Fireworks(id="accounts/fireworks/models/llama-v3p1-405b-instruct"),
    markdown=True,
)

asyncio.run(agent.aprint_response("Share a 2 sentence horror story"))
