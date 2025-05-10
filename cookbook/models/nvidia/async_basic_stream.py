"""
Basic streaming async example using Nvidia.
"""

import asyncio

from pinaxai.agent import Agent
from pinaxai.models.nvidia import Nvidia

agent = Agent(model=Nvidia(id="meta/llama-3.3-70b-instruct"), markdown=True)

asyncio.run(agent.aprint_response("Share a 2 sentence horror story", stream=True))
