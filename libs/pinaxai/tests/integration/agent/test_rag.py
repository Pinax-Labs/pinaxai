# Create a knowledge base of PDFs from URLs
import asyncio

import pytest
import pytest_asyncio

from pinaxai.agent.agent import Agent
from pinaxai.embedder.openai import OpenAIEmbedder
from pinaxai.knowledge.pdf_url import PDFUrlKnowledgeBase
from pinaxai.models.openai.chat import OpenAIChat
from pinaxai.vectordb.lancedb.lance_db import LanceDb
from pinaxai.vectordb.search import SearchType


# Add a session-scoped event loop fixture
@pytest_asyncio.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def loaded_knowledge_base():
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://pinaxai-public.s3.amazonaws.com/recipes/thai_recipes_short.pdf"],
        vector_db=LanceDb(
            table_name="recipes",
            uri="tmp/lancedb",
            search_type=SearchType.vector,
            embedder=OpenAIEmbedder(),
        ),
    )
    await knowledge_base.aload()
    return knowledge_base


@pytest.mark.asyncio
async def test_add_references(loaded_knowledge_base):
    agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        knowledge=loaded_knowledge_base,
        # Enable RAG by adding references from AgentKnowledge to the user prompt.
        add_references=True,
        # Set as False because Agents default to `search_knowledge=True`
        search_knowledge=False,
        show_tool_calls=True,
        markdown=True,
    )
    response = await agent.arun("How do I make chicken and galangal in coconut milk soup")
    assert response.content is not None
