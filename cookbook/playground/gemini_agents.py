from pinaxai.agent import Agent
from pinaxai.models.google import Gemini
from pinaxai.playground import Playground, serve_playground_app
from pinaxai.tools.yfinance import YFinanceTools

finance_agent = Agent(
    name="Finance Agent",
    agent_id="finance-agent",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[YFinanceTools(stock_price=True)],
    debug_mode=True,
)

app = Playground(agents=[finance_agent]).get_app(use_async=False)

if __name__ == "__main__":
    serve_playground_app("gemini_agents:app", reload=True)
