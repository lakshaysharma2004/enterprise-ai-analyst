from vectorstore.in_memory_vectorstore import InMemoryVectorStore
from core.chunk import Chunk

chunk1=Chunk(
    text="This text is about cats",
    source_file="test.txt",
    page_number=1,
    section=None,
    chunk_id=1
)

chunk2=Chunk(
    text="This text is about databases",
    source_file="text.txt",
    page_number=1,
    section=None,
    chunk_id=2
)
chunks=[chunk1,chunk2]

vectors=[
    [0.9,0.1],
    [0.0,1.0]
]

store=InMemoryVectorStore(embedding_dimension=2)

store.add(vectors,chunks)

print(f"Store size:{len(store)}")

query_vector=[1.0,0.0]

results=store.search(query_vector,top_k=1)
print("Top result:")
print(results[0])