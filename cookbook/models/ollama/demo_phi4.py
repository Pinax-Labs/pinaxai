from pinaxai.agent import Agent, RunResponse  # noqa
from pinaxai.models.ollama import Ollama
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(model=Ollama(id="phi4"), markdown=True)

# Print the response in the terminal
agent.print_response("Tell me a scary story in exactly 10 words.")
