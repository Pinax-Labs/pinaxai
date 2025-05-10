from textwrap import dedent

from pinaxai.agent import Agent
from pinaxai.knowledge.url import UrlKnowledge
from pinaxai.models.anthropic import Claude
from pinaxai.models.openai import OpenAIChat
from pinaxai.team.team import Team
from pinaxai.tools.duckduckgo import DuckDuckGoTools
from pinaxai.tools.knowledge import KnowledgeTools
from pinaxai.tools.reasoning import ReasoningTools
from pinaxai.tools.yfinance import YFinanceTools
from pinaxai.vectordb.lancedb import LanceDb, SearchType

pinaxai_docs = UrlKnowledge(
    urls=["https://www.paulgraham.com/read.html"],
    # Use LanceDB as the vector database and store embeddings in the `pinaxai_docs` table
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="pinaxai_docs",
        search_type=SearchType.hybrid,
    ),
)

knowledge_tools = KnowledgeTools(
    knowledge=pinaxai_docs,
    think=True,
    search=True,
    analyze=True,
    add_few_shot=True,
)

web_agent = Agent(
    name="Web Search Agent",
    role="Handle web search requests",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    add_datetime_to_instructions=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Handle financial data requests",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)
    ],
    add_datetime_to_instructions=True,
)

team_leader = Team(
    name="Reasoning Finance Team",
    mode="coordinate",
    model=OpenAIChat(id="gpt-4o"),
    members=[
        web_agent,
        finance_agent,
    ],
    tools=[knowledge_tools],
    instructions=[
        "Only output the final answer, no other text.",
        "Use tables to display data",
    ],
    markdown=True,
    show_members_responses=True,
    enable_agentic_context=True,
    add_datetime_to_instructions=True,
    success_criteria="The team has successfully completed the task.",
    debug_mode=True,
)


def run_team(task: str):
    # Comment out after first run
    pinaxai_docs.load(recreate=True)
    team_leader.print_response(
        task,
        stream=True,
        stream_intermediate_steps=True,
        show_full_reasoning=True,
    )


if __name__ == "__main__":
    run_team("What does Paul Graham talk about the need to read in this essay?")
