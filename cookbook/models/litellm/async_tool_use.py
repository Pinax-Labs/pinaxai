import asyncio

from pinaxai.agent import Agent
from pinaxai.models.litellm import LiteLLM
from pinaxai.tools.duckduckgo import DuckDuckGoTools
from pinaxai.tools.yfinance import YFinanceTools

agent = Agent(
    model=LiteLLM(
        id="gpt-4o",
        name="LiteLLM",
    ),
    markdown=True,
    tools=[DuckDuckGoTools()],
)

# Ask a question that would likely trigger tool use
asyncio.run(agent.aprint_response("What is happening in France?"))
