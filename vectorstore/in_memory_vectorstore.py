from vectorstore.base_vectorstore import BaseVectorStore
import math


class InMemoryVectorStore(BaseVectorStore):
    """
    In-memory vector store using brute-force cosine similarity search.
    Intended for small datasets and learning purposes.
    """

    def __init__(self, embedding_dimension=None):
        """
        Initialize empty vector and chunk storage.

        Args:
            embedding_dimension (int, optional): Expected embedding dimension.
        """
        super().__init__()
        self.vectors = []
        self.chunks = []
        self.embedding_dimension = embedding_dimension

    def add(self, vectors, chunks):
        """
        Add embedding vectors and their corresponding chunks to the store.

        Args:
            vectors (list[list[float]]): List of embedding vectors.
            chunks (list[Chunk]): List of Chunk objects.

        Raises:
            ValueError: If number of vectors and chunks do not match.
            ValueError: If vector dimension does not match embedding_dimension.
        """
        if len(vectors) != len(chunks):
            raise ValueError("Number of vectors must match number of chunks")

        if self.embedding_dimension is not None:
            for vector in vectors:
                if len(vector) != self.embedding_dimension:
                    raise ValueError(
                        "Vector dimension does not match embedding dimension"
                    )

        self.vectors.extend(vectors)
        self.chunks.extend(chunks)

    def _cosine_similarity(self, vec1, vec2):
        """
        Compute cosine similarity between two vectors.
        """
        dot = 0.0
        norm1_sq = 0.0
        norm2_sq = 0.0

        for a, b in zip(vec1, vec2):
            dot += a * b
            norm1_sq += a * a
            norm2_sq += b * b

        mag1 = math.sqrt(norm1_sq)
        mag2 = math.sqrt(norm2_sq)

        if mag1 == 0 or mag2 == 0:
            return 0.0

        return dot / (mag1 * mag2)

    def search(self, query_vector, top_k):
        """
        Retrieve the top-k most similar chunks for a query vector.

        Args:
            query_vector (list[float]): Query embedding vector.
            top_k (int): Number of results to return.

        Returns:
            list[Chunk]: Retrieved chunks ordered by similarity.
        """
        if not self.vectors:
            return []

        scores = []

        for index, stored_vector in enumerate(self.vectors):
            score = self._cosine_similarity(query_vector, stored_vector)
            scores.append((score, index))

        scores.sort(key=lambda x: x[0], reverse=True)
        top_k_scores = scores[:top_k]

        return [self.chunks[index] for _, index in top_k_scores]

    def __len__(self):
        """
        Return the number of stored vectors.
        """
        return len(self.vectors)
