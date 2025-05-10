from pinaxai.agent import Agent
from pinaxai.tools.jina import JinaReaderTools

agent = Agent(tools=[JinaReaderTools()], debug_mode=True, show_tool_calls=True)
agent.print_response("Summarize: https://github.com/Pinax-Labs")
