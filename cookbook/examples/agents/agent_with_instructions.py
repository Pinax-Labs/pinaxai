from pinaxai.agent import Agent
from pinaxai.models.anthropic import Claude
from pinaxai.tools.yfinance import YFinanceTools

agent = Agent(
    model=Claude(id="claude-3-7-sonnet-latest"),
    tools=[YFinanceTools(stock_price=True)],
    instructions=[
        "Use tables to display data.",
        "Only include the table in your response. No other text.",
    ],
    markdown=True,
)
agent.print_response("What is the stock price of Apple?", stream=True)
