from pathlib import Path

from pinaxai.agent import Agent
from pinaxai.knowledge.combined import CombinedKnowledgeBase
from pinaxai.knowledge.csv import CSVKnowledgeBase
from pinaxai.knowledge.pdf import PDFKnowledgeBase
from pinaxai.knowledge.pdf_url import PDFUrlKnowledgeBase
from pinaxai.knowledge.website import WebsiteKnowledgeBase
from pinaxai.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

# Create CSV knowledge base
csv_kb = CSVKnowledgeBase(
    path=Path("data/csvs"),
    vector_db=PgVector(
        table_name="csv_documents",
        db_url=db_url,
    ),
)

# Create PDF URL knowledge base
pdf_url_kb = PDFUrlKnowledgeBase(
    urls=["https://pinaxai-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(
        table_name="pdf_documents",
        db_url=db_url,
    ),
)

# Create Website knowledge base
website_kb = WebsiteKnowledgeBase(
    urls=["https://docs.pinax.tech/introduction"],
    max_links=10,
    vector_db=PgVector(
        table_name="website_documents",
        db_url=db_url,
    ),
)

# Create Local PDF knowledge base
local_pdf_kb = PDFKnowledgeBase(
    path="data/pdfs",
    vector_db=PgVector(
        table_name="pdf_documents",
        db_url=db_url,
    ),
)

# Combine knowledge bases
knowledge_base = CombinedKnowledgeBase(
    sources=[
        csv_kb,
        pdf_url_kb,
        website_kb,
        local_pdf_kb,
    ],
    vector_db=PgVector(
        table_name="combined_documents",
        db_url=db_url,
    ),
)

# Initialize the Agent with the combined knowledge base
agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
)

knowledge_base.load(recreate=False)

# Use the agent
agent.print_response("Ask me about something from the knowledge base", markdown=True)
