class BaseRetriever:
    """
    Base class for all retrievers.
    
    A retriever is responsible for selecting the most relevant chunks for a given query using semantic similarity
    """
    def __init__(self):
        """
        Initialize the retriever.
        Concrete retrievers will inject embedder and vector store.
        """
        pass
    def retrieve(self,query,top_k):
        """
        Retrieve the top-k most relevant chunks for a given query.

        Args:
            query (str): User query text.
            top_k (int): Number of chunks to retrieve.

        Returns:
            list[Chunk]: Retrieved relevant chunks.
        """
        raise NotImplementedError(
            "retrieve() must be implemented bu subclasses of BaseRetriever"
        ) 