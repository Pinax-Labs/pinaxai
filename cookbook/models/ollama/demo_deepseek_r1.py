from pinaxai.agent import Agent, RunResponse  # noqa
from pinaxai.models.ollama import Ollama

agent = Agent(model=Ollama(id="deepseek-r1:14b"), markdown=True)

# Print the response in the terminal
agent.print_response(
    "Write me python code to solve quadratic equations. Explain your reasoning."
)
