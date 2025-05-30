from pinaxai.agent import Agent
from pinaxai.models.openai import OpenAIChat
from pinaxai.tools.yfinance import YFinanceTools

agent = Agent(
    model=OpenAIChat(id="o3-mini"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        )
    ],
    instructions="Use tables to display data.",
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Write a report comparing NVDA to TSLA", stream=True)
