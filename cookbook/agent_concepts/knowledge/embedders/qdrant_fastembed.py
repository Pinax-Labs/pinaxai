from pinaxai.agent import AgentKnowledge
from pinaxai.embedder.fastembed import FastEmbedEmbedder
from pinaxai.vectordb.pgvector import PgVector

embeddings = FastEmbedEmbedder().get_embedding(
    "The quick brown fox jumps over the lazy dog."
)

# Print the embeddings and their dimensions
print(f"Embeddings: {embeddings[:5]}")
print(f"Dimensions: {len(embeddings)}")

# Example usage:
knowledge_base = AgentKnowledge(
    vector_db=PgVector(
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
        table_name="qdrant_embeddings",
        embedder=FastEmbedEmbedder(),
    ),
    num_documents=2,
)
