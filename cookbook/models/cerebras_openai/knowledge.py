"""Run `pip install duckduckgo-search sqlalchemy pgvector pypdf cerebras_cloud_sdk` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.knowledge.pdf_url import PDFUrlKnowledgeBase
from pinaxai.models.cerebras import CerebrasOpenAI
from pinaxai.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://pinaxai-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url),
)
knowledge_base.load(recreate=True)  # Comment out after first run

agent = Agent(
    model=CerebrasOpenAI(id="llama-4-scout-17b-16e-instruct"),
    knowledge=knowledge_base,
    show_tool_calls=True,
)
agent.print_response("How to make Thai curry?", markdown=True)
