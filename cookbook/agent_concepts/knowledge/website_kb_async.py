import asyncio

from pinaxai.agent import Agent
from pinaxai.knowledge.website import WebsiteKnowledgeBase
from pinaxai.vectordb.qdrant import Qdrant

COLLECTION_NAME = "website-content"

vector_db = Qdrant(collection=COLLECTION_NAME, url="http://localhost:6333")


# Create a knowledge base with the seed URLs
knowledge_base = WebsiteKnowledgeBase(
    urls=["https://docs.pinax.techintroduction"],
    # Number of links to follow from the seed URLs
    max_links=5,
    # Table name: ai.website_documents
    vector_db=vector_db,
)

# Create an agent with the knowledge base
agent = Agent(knowledge=knowledge_base, search_knowledge=True, debug_mode=True)

if __name__ == "__main__":
    # Comment out after first run
    asyncio.run(knowledge_base.aload(recreate=False))

    # Create and use the agent
    asyncio.run(agent.aprint_response("How does pinaxai work?", markdown=True))
