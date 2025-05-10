import asyncio

from pinaxai.agent import Agent
from pinaxai.models.cerebras import CerebrasOpenAI
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=CerebrasOpenAI(id="llama-3.3-70b"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

asyncio.run(agent.aprint_response("Whats happening in France?"))
