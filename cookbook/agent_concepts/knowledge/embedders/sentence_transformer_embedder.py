from pinaxai.agent import AgentKnowledge
from pinaxai.embedder.sentence_transformer import SentenceTransformerEmbedder
from pinaxai.vectordb.pgvector import PgVector

embeddings = SentenceTransformerEmbedder().get_embedding(
    "The quick brown fox jumps over the lazy dog."
)

# Print the embeddings and their dimensions
print(f"Embeddings: {embeddings[:5]}")
print(f"Dimensions: {len(embeddings)}")

# Example usage:
knowledge_base = AgentKnowledge(
    vector_db=PgVector(
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
        table_name="sentence_transformer_embeddings",
        embedder=SentenceTransformerEmbedder(),
    ),
    num_documents=2,
)
