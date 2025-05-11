from pinaxai.agents import Agent
from pinaxai.models.groq import Groq

agent = Agent(model=Groq(id="deepseek-r1-distill-llama-70b-specdec"), markdown=True)

# Print the response on the terminal
agent.print_response("Share a 2 sentence horror story")
