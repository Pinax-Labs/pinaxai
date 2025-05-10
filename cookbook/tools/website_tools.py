from pinaxai.agent import Agent
from pinaxai.tools.website import WebsiteTools

agent = Agent(tools=[WebsiteTools()], show_tool_calls=True)

agent.print_response(
    "Search web page: 'https://docs.pinax.tech/introduction'", markdown=True
)
