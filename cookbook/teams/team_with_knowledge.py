from pathlib import Path

from pinaxai.agent import Agent
from pinaxai.embedder.openai import OpenAIEmbedder
from pinaxai.knowledge.url import UrlKnowledge
from pinaxai.models.openai import OpenAIChat
from pinaxai.team import Team
from pinaxai.tools.duckduckgo import DuckDuckGoTools
from pinaxai.vectordb.lancedb import LanceDb, SearchType

# Setup paths
cwd = Path(__file__).parent
tmp_dir = cwd.joinpath("tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)

# Initialize knowledge base
pinaxai_docs_knowledge = UrlKnowledge(
    urls=["https://docs.pinax.tech/llms-full.txt"],
    vector_db=LanceDb(
        uri=str(tmp_dir.joinpath("lancedb")),
        table_name="pinaxai_docs",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)

web_agent = Agent(
    name="Web Search Agent",
    role="Handle web search requests",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
)

team_with_knowledge = Team(
    name="Team with Knowledge",
    members=[web_agent],
    model=OpenAIChat(id="gpt-4o"),
    knowledge=pinaxai_docs_knowledge,
    show_members_responses=True,
    markdown=True,
)

if __name__ == "__main__":
    # Set to False after the knowledge base is loaded
    load_knowledge = True
    if load_knowledge:
        pinaxai_docs_knowledge.load()

    team_with_knowledge.print_response("Tell me about the Pinaxai framework", stream=True)
