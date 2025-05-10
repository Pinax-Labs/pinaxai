from pinaxai.agent import Agent
from pinaxai.knowledge.pdf_url import PDFUrlKnowledgeBase
from pinaxai.vectordb.qdrant import Qdrant

COLLECTION_NAME = "thai-recipes"

vector_db = Qdrant(collection=COLLECTION_NAME, url="http://localhost:6333")

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://pinaxai-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)

knowledge_base.load(recreate=False)  # Comment out after first run

# Create and use the agent
agent = Agent(knowledge=knowledge_base, show_tool_calls=True)
agent.print_response("List down the ingredients to make Massaman Gai", markdown=True)
