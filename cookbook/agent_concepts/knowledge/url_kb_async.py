"""Agent with Knowledge - An agent that can search a knowledge base

Install dependencies: `pip install openai lancedb tantivy pinaxai`
"""

import asyncio
from pathlib import Path

from pinaxai.agent import Agent
from pinaxai.knowledge.url import UrlKnowledge
from pinaxai.models.openai import OpenAIChat
from pinaxai.vectordb.lancedb import LanceDb, SearchType

# Setup paths
cwd = Path(__file__).parent
tmp_dir = cwd.joinpath("tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)

# Initialize knowledge base
agent_knowledge = UrlKnowledge(
    urls=["https://docs.pinax.techintroduction"],
    vector_db=LanceDb(
        uri=str(tmp_dir.joinpath("lancedb")),
        table_name="pinaxai_assist_knowledge",
        search_type=SearchType.hybrid,
    ),
)

agent_with_knowledge = Agent(
    name="Agent with Knowledge",
    model=OpenAIChat(id="gpt-4o"),
    knowledge=agent_knowledge,
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    asyncio.run(agent_knowledge.aload(recreate=False))

    asyncio.run(
        agent_with_knowledge.aprint_response(
            "Tell me about teams with context to pinaxai", stream=True
        )
    )
