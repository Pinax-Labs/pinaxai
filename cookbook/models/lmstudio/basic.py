from pinaxai.agent import Agent, RunResponse  # noqa
from pinaxai.models.lmstudio import LMStudio

agent = Agent(model=LMStudio(id="qwen2.5-7b-instruct-1m"), markdown=True)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story")
# print(run.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story")
