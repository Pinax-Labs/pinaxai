from pinaxai.agent import Agent
from pinaxai.embedder.openai import OpenAIEmbedder
from pinaxai.knowledge.url import UrlKnowledge
from pinaxai.models.openai import OpenAIChat
from pinaxai.storage.sqlite import SqliteStorage
from pinaxai.vectordb.lancedb import LanceDb, SearchType

pinaxai_assist = Agent(
    name="Pinaxai Assist",
    model=OpenAIChat(id="gpt-4o"),
    description="You help answer questions about the Pinaxai framework.",
    instructions="Search your knowledge before answering the question.",
    knowledge=UrlKnowledge(
        urls=["https://docs.pinax.tech/llms-full.txt"],
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="pinaxai_assist_knowledge",
            search_type=SearchType.hybrid,
            embedder=OpenAIEmbedder(id="text-embedding-3-small"),
        ),
    ),
    storage=SqliteStorage(table_name="pinaxai_assist_sessions", db_file="tmp/agents.db"),
    add_history_to_messages=True,
    add_datetime_to_instructions=True,
    markdown=True,
)

if __name__ == "__main__":
    pinaxai_assist.knowledge.load()  # Load the knowledge base, comment after first run
    pinaxai_assist.print_response("What is Pinaxai?")
