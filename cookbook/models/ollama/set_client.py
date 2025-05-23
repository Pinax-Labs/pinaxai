"""Run `pip install yfinance` to install dependencies."""

from pinaxai.agent import Agent, RunResponse  # noqa
from pinaxai.models.ollama import Ollama
from ollama import Client as OllamaClient

agent = Agent(
    model=Ollama(id="llama3.1:8b", client=OllamaClient()),
    markdown=True,
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story")
