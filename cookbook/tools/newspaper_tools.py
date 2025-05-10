from pinaxai.agent import Agent
from pinaxai.tools.newspaper import NewspaperTools

agent = Agent(tools=[NewspaperTools()])
agent.print_response("Please summarize https://en.wikipedia.org/wiki/Language_model")
