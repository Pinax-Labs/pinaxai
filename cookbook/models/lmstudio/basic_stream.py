from typing import Iterator  # noqa
from pinaxai.agent import Agent, RunResponse  # noqa
from pinaxai.models.lmstudio import LMStudio

agent = Agent(model=LMStudio(id="qwen2.5-7b-instruct-1m"), markdown=True)

# Get the response in a variable
# run_response: Iterator[RunResponse] = agent.run("Share a 2 sentence horror story", stream=True)
# for chunk in run_response:
#     print(chunk.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story", stream=True)
