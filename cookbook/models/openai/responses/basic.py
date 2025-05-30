from pinaxai.agent import Agent, RunResponse  # noqa
from pinaxai.models.openai import OpenAIResponses

agent = Agent(model=OpenAIResponses(id="gpt-4o"), markdown=True)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story")
# print(run.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story")

agent.run_response.metrics
