from pinaxai.agent import Agent
from pinaxai.tools.serpapi import SerpApiTools

agent = Agent(tools=[SerpApiTools()], show_tool_calls=True)
agent.print_response("Whats happening in the USA?", markdown=True)
