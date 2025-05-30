import asyncio
from typing import Iterator  # noqa

from pinaxai.agent import Agent, RunResponse  # noqa
from pinaxai.models.aws import Claude

agent = Agent(
    model=Claude(id="anthropic.claude-3-5-sonnet-20240620-v1:0"), markdown=True
)

# Get the response in a variable
# run_response: Iterator[RunResponse] = agent.run("Share a 2 sentence horror story", stream=True)
# for chunk in run_response:
#     print(chunk.content)

# Print the response in the terminal
asyncio.run(agent.aprint_response("Share a 2 sentence horror story", stream=True))
