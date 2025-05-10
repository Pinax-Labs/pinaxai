from pinaxai.agent import Agent
from pinaxai.document.chunking.document import DocumentChunking
from pinaxai.knowledge.pdf_url import PDFUrlKnowledgeBase
from pinaxai.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://pinaxai-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes_document_chunking", db_url=db_url),
    chunking_strategy=DocumentChunking(),
)
knowledge_base.load(recreate=False)  # Comment out after first run

agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
)

agent.print_response("How to make Thai curry?", markdown=True)
