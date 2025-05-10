from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIResponses

agent = Agent(model=OpenAIResponses(id="o1-pro"))
agent.print_response(
    "Solve the trolley problem. Evaluate multiple ethical frameworks. "
    "Include an ASCII diagram of your solution.",
    stream=True,
)
