class BaseVectorStore:
    """
    Base class for vector stores.

    Defines the interface for storing embedding vectors and
    performing similarity-based retrieval. Concrete implementations
    must implement all methods.
    """

    def __init__(self):
        """
        Initialize the base vector store.

        The embedding dimension may be defined by subclasses.
        """
        self.embedding_dimension = None

    def add(self, vectors, chunks):
        """
        Add embedding vectors and their corresponding chunks to the store.

        Args:
            vectors (list[list[float]]): List of embedding vectors.
            chunks (list[Chunk]): List of Chunk objects corresponding to vectors.
        """
        raise NotImplementedError(
            "add() must be implemented by subclasses of BaseVectorStore"
        )

    def search(self, query_vector, top_k):
        """
        Retrieve the top-k most similar chunks for a query vector.

        Args:
            query_vector (list[float]): Embedding vector of the query.
            top_k (int): Number of top similar results to return.

        Returns:
            list[Chunk]: List of retrieved Chunk objects.
        """
        raise NotImplementedError(
            "search() must be implemented by subclasses of BaseVectorStore"
        )

    def __len__(self):
        """
        Return the number of stored vectors.
        """
        raise NotImplementedError(
            "__len__() must be implemented by subclasses of BaseVectorStore"
        )
