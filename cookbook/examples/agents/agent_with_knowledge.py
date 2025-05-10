from pinaxai.agent import Agent
from pinaxai.embedder.openai import OpenAIEmbedder
from pinaxai.knowledge.url import UrlKnowledge
from pinaxai.models.anthropic import Claude
from pinaxai.tools.reasoning import ReasoningTools
from pinaxai.vectordb.lancedb import LanceDb, SearchType

# Load Pinaxai documentation in a knowledge base
knowledge = UrlKnowledge(
    urls=["https://docs.pinax.tech/introduction/agents.md"],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="pinaxai_docs",
        search_type=SearchType.hybrid,
        # Use OpenAI for embeddings
        embedder=OpenAIEmbedder(id="text-embedding-3-small", dimensions=1536),
    ),
)

agent = Agent(
    name="Pinaxai Assist",
    model=Claude(id="claude-3-7-sonnet-latest"),
    instructions=[
        "Use tables to display data.",
        "Include sources in your response.",
        "Search your knowledge before answering the question.",
        "Only include the output in your response. No other text.",
    ],
    knowledge=knowledge,
    tools=[ReasoningTools(add_instructions=True)],
    add_datetime_to_instructions=True,
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment out after first run
    # Set recreate to True to recreate the knowledge base if needed
    agent.knowledge.load(recreate=False)
    agent.print_response(
        "What are Agents?",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
