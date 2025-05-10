import asyncio

from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIChat
from pinaxai.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
asyncio.run(agent.aprint_response("Whats happening in UK and in USA?"))
