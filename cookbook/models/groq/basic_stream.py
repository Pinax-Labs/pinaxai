from typing import Iterator  # noqa
from pinaxai.agent import Agent, RunResponse  # noqa
from pinaxai.models.groq import Groq

agent = Agent(model=Groq(id="llama-3.3-70b-versatile"), markdown=True)

# Get the response in a variable
# run_response: Iterator[RunResponse] = agent.run("Share a 2 sentence horror story", stream=True)
# for chunk in run_response:
#     print(chunk.content)

# Print the response on the terminal
agent.print_response("Share a 2 sentence horror story", stream=True)
