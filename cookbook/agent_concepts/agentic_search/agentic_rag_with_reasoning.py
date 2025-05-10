"""This cookbook shows how to implement Agentic RAG with Reasoning.
1. Run: `pip install pinaxai anthropic cohere lancedb tantivy sqlalchemy` to install the dependencies
2. Export your ANTHROPIC_API_KEY and CO_API_KEY
3. Run: `python cookbook/agent_concepts/agentic_search/agentic_rag_with_reasoning.py` to run the agent
"""

from pinaxai.agent import Agent
from pinaxai.embedder.cohere import CohereEmbedder
from pinaxai.knowledge.url import UrlKnowledge
from pinaxai.models.anthropic import Claude
from pinaxai.reranker.cohere import CohereReranker
from pinaxai.tools.reasoning import ReasoningTools
from pinaxai.vectordb.lancedb import LanceDb, SearchType

# Create a knowledge base, loaded with documents from a URL
knowledge_base = UrlKnowledge(
    urls=["https://docs.pinax.tech/introduction/agents.md"],
    # Use LanceDB as the vector database, store embeddings in the `pinaxai_docs` table
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="pinaxai_docs",
        search_type=SearchType.hybrid,
        embedder=CohereEmbedder(id="embed-v4.0"),
        reranker=CohereReranker(model="rerank-v3.5"),
    ),
)

agent = Agent(
    model=Claude(id="claude-3-7-sonnet-latest"),
    # Agentic RAG is enabled by default when `knowledge` is provided to the Agent.
    knowledge=knowledge_base,
    # search_knowledge=True gives the Agent the ability to search on demand
    # search_knowledge is True by default
    search_knowledge=True,
    tools=[ReasoningTools(add_instructions=True)],
    instructions=[
        "Include sources in your response.",
        "Always search your knowledge before answering the question.",
    ],
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment after first run
    # knowledge_base.load(recreate=True)
    agent.print_response(
        "What are Agents?",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
