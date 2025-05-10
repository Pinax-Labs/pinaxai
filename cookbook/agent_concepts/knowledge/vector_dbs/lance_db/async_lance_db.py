# install lancedb - `pip install lancedb`

import asyncio

from pinaxai.agent import Agent
from pinaxai.knowledge.pdf_url import PDFUrlKnowledgeBase
from pinaxai.vectordb.lancedb import LanceDb

# Initialize LanceDB
# By default, it stores data in /tmp/lancedb
vector_db = LanceDb(
    table_name="recipes",
    uri="tmp/lancedb",  # You can change this path to store data elsewhere
)

# Create knowledge base
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://pinaxai-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)
agent = Agent(knowledge=knowledge_base, show_tool_calls=True, debug_mode=True)

if __name__ == "__main__":
    asyncio.run(knowledge_base.aload(recreate=False))  # Comment out after first run

    # Create and use the agent
    asyncio.run(agent.aprint_response("How to make Tom Kha Gai", markdown=True))
