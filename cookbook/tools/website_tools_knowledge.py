from pathlib import Path

from pinaxai.agent import Agent
from pinaxai.knowledge.combined import CombinedKnowledgeBase
from pinaxai.knowledge.pdf_url import PDFUrlKnowledgeBase
from pinaxai.knowledge.website import WebsiteKnowledgeBase
from pinaxai.tools.website import WebsiteTools
from pinaxai.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

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

# Combine knowledge bases
knowledge_base = CombinedKnowledgeBase(
    sources=[
        pdf_url_kb,
        website_kb,
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
    show_tool_calls=True,
    tools=[
        WebsiteTools(
            knowledge_base=knowledge_base
        )  # Set combined or website knowledge base
    ],
)

knowledge_base.load(recreate=False)

# Use the agent
agent.print_response(
    "How do I get started on Mistral: https://docs.mistral.ai/getting-started/models/models_overview",
    markdown=True,
    stream=True,
)
