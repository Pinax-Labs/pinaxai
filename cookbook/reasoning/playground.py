from pinaxai.agent import Agent
from pinaxai.models.anthropic import Claude
from pinaxai.playground import Playground, serve_playground_app
from pinaxai.tools.reasoning import ReasoningTools
from pinaxai.tools.yfinance import YFinanceTools

claude_reasoning_agent = Agent(
    name="Claude Reasoning Finance Agent",
    model=Claude(id="claude-3-7-sonnet-latest"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    stream_intermediate_steps=True,
    instructions="Use tables where possible",
    markdown=True,
)


app = Playground(
    agents=[claude_reasoning_agent],
).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
