from pinaxai.agent import Agent
from pinaxai.models.anthropic import Claude

agent = Agent(model=Claude(id="claude-3-7-sonnet-latest"), markdown=True)
agent.print_response("What is the stock price of Apple?", stream=True)
