from retriever.base_retriever import BaseRetriever

class SimpleRetriever(BaseRetriever):
    """
    A simple retriever that embeds a query and retrieves
    the most relevant chunks from a vector store.
    """

    def __init__(self, embedder, vector_store):
        super().__init__()
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(self, query, top_k):
        """
        Retrieve the top-k most relevant chunks for a query.

        Args:
            query (str): User query.
            top_k (int): Number of chunks to retrieve.

        Returns:
            list[Chunk]: Retrieved chunks.
        """
        query_vector = self.embedder.embed(query)
        return self.vector_store.search(query_vector, top_k)
