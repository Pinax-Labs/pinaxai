"""
1. Run: `pip install openai pinaxai lancedb tantivy sqlalchemy` to install the dependencies
2. Export your OPENAI_API_KEY
3. Run: `python cookbook/reasoning/tools/knowledge_tools.py` to run the agent
"""

from pinaxai.agent import Agent
from pinaxai.embedder.openai import OpenAIEmbedder
from pinaxai.knowledge.url import UrlKnowledge
from pinaxai.models.openai import OpenAIChat
from pinaxai.tools.knowledge import KnowledgeTools
from pinaxai.vectordb.lancedb import LanceDb, SearchType

# Create a knowledge base containing information from a URL
pinaxai_docs = UrlKnowledge(
    urls=["https://docs.pinax.tech/llms-full.txt"],
    # Use LanceDB as the vector database and store embeddings in the `pinaxai_docs` table
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="pinaxai_docs",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)

knowledge_tools = KnowledgeTools(
    knowledge=pinaxai_docs,
    think=True,
    search=True,
    analyze=True,
    add_few_shot=True,
)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[knowledge_tools],
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment after first run
    pinaxai_docs.load(recreate=True)
    agent.print_response("How do I build multi-agent teams with Pinaxai?", stream=True)
