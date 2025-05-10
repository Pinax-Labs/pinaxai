from pinaxai.agent import Agent
from pinaxai.tools.wikipedia import WikipediaTools

agent = Agent(tools=[WikipediaTools()], show_tool_calls=True)
agent.print_response("Search wikipedia for 'ai'")
