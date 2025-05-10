"""Run `pip install duckduckgo-search sqlalchemy pgvector pypdf openai` to install dependencies."""

from pinaxai.agent import Agent
from pinaxai.embedder.azure_openai import AzureOpenAIEmbedder
from pinaxai.knowledge.pdf_url import PDFUrlKnowledgeBase
from pinaxai.models.azure import AzureAIFoundry
from pinaxai.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://pinaxai-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(
        table_name="recipes",
        db_url=db_url,
        embedder=AzureOpenAIEmbedder(),
    ),
)
knowledge_base.load(recreate=False)  # Comment out after first run

agent = Agent(
    model=AzureAIFoundry(id="Cohere-command-r-08-2024"),
    knowledge=knowledge_base,
    show_tool_calls=True,
    debug_mode=True,
)
agent.print_response("How to make Thai curry?", markdown=True)
