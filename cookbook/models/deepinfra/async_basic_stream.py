import asyncio
from typing import Iterator  # noqa

from pinaxai.agent import Agent, RunResponse  # noqa
from pinaxai.models.deepinfra import DeepInfra  # noqa

agent = Agent(
    model=DeepInfra(id="meta-llama/Llama-2-70b-chat-hf"),
    markdown=True,
)

# Print the response in the terminal
asyncio.run(agent.aprint_response("Share a 2 sentence horror story", stream=True))
