import asyncio

from pinaxai.agent import Agent, RunResponse  # noqa
from pinaxai.models.perplexity import Perplexity

agent = Agent(model=Perplexity(id="sonar"), markdown=True)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story")
# print(run.content)

# Print the response in the terminal
asyncio.run(agent.aprint_response("Share a 2 sentence horror story"))
