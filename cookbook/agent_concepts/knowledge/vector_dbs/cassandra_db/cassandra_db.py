from pinaxai.agent import Agent
from pinaxai.embedder.mistral import MistralEmbedder
from pinaxai.knowledge.pdf_url import PDFUrlKnowledgeBase
from pinaxai.models.mistral import MistralChat
from pinaxai.vectordb.cassandra import Cassandra

try:
    from cassandra.cluster import Cluster  # type: ignore
except (ImportError, ModuleNotFoundError):
    raise ImportError(
        "Could not import cassandra-driver python package.Please install it with pip install cassandra-driver."
    )

cluster = Cluster()

session = cluster.connect()
session.execute(
    """
    CREATE KEYSPACE IF NOT EXISTS testkeyspace
    WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
    """
)

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://pinaxai-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=Cassandra(
        table_name="recipes",
        keyspace="testkeyspace",
        session=session,
        embedder=MistralEmbedder(),
    ),
)


knowledge_base.load(recreate=True)  # Comment out after first run

agent = Agent(
    model=MistralChat(),
    knowledge=knowledge_base,
    show_tool_calls=True,
)

agent.print_response(
    "What are the health benefits of Khao Niew Dam Piek Maphrao Awn?",
    markdown=True,
    show_full_reasoning=True,
)
