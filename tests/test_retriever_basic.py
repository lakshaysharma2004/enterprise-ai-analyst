from core.chunk import Chunk
from parsing.text_parser import TextParser
from chunking.text_chunker import TextChunker
from embeddings.sentence_transformer_embedder import SentenceTransformerEmbedder
from vectorstore.in_memory_vectorstore import InMemoryVectorStore
from retriever.simple_retriever import SimpleRetriever

parser=TextParser()
parsed_document=parser.parse("tests/large_sample_doc.txt")

chunker=TextChunker(chunk_size=100)
chunks=chunker.chunk(parsed_document=parsed_document,source_file="large_sample_doc.txt")

print(f"Number of Chunks: {len(chunks)}")

embedder=SentenceTransformerEmbedder()
vectors=embedder.embed_batch([chunk.text for chunk in chunks])

vector_store=InMemoryVectorStore(len(vectors[0]))
vector_store.add(vectors,chunks)

retriever=SimpleRetriever(embedder,vector_store)

# query1="What are cats?" this is working
# query = "What are cats known for?"
# query = "Explain relational databases"
# query = "What is machine learning?"
# query = "Why is testing important in software engineering?"
query = "What is cloud computing?"

results=retriever.retrieve(query=query,top_k=3)

print("\n Top Retrieved Results:")
print(results)

