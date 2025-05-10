"""Run `pip install duckduckgo-search sqlalchemy pgvector pypdf openai ollama` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.embedder.ollama import OllamaEmbedder
from pinaxai.knowledge.pdf_url import PDFUrlKnowledgeBase
from pinaxai.models.ollama import Ollama
from pinaxai.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://pinaxai-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(
        table_name="recipes",
        db_url=db_url,
        embedder=OllamaEmbedder(id="llama3.2", dimensions=3072),
    ),
)
knowledge_base.load(recreate=True)  # Comment out after first run

agent = Agent(
    model=Ollama(id="llama3.2"),
    knowledge=knowledge_base,
    show_tool_calls=True,
)
agent.print_response("How to make Thai curry?", markdown=True)
