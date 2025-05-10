from pinaxai.agent import Agent
from pinaxai.models.ollama.chat import Ollama
from pinaxai.tools.reasoning import ReasoningTools
from pinaxai.tools.yfinance import YFinanceTools

reasoning_agent = Agent(
    model=Ollama(id="llama3.2:latest"),
    tools=[
        ReasoningTools(
            think=True,
            analyze=True,
            add_instructions=True,
            add_few_shot=True,
        ),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    instructions="Use tables where possible",
    markdown=True,
)
reasoning_agent.print_response(
    "Write a report comparing NVDA to TSLA",
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=True,
)
