class BaseEmbedder:
    """
    Base class for all embedding models.

    Concrete embedders must inherit from this class and implement
    the embedding logic for converting text into numerical vectors.
    """

    def __init__(self):
        """
        Initialize the base embedder.

        The embedding dimension must be defined by subclasses.
        """
        self.dimension = None

    def embed(self, text):
        """
        Convert a single text into a numerical vector.

        Args:
            text (str): Input text to be embedded.

        Returns:
            list[float]: Embedding vector representing the text.
        """
        raise NotImplementedError(
            "embed() must be implemented by subclasses of BaseEmbedder"
        )

    def embed_batch(self, texts):
        """
        Convert multiple texts into numerical vectors.

        Args:
            texts (list[str]): List of input texts to be embedded.

        Returns:
            list[list[float]]: List of embedding vectors.
        """
        raise NotImplementedError(
            "embed_batch() must be implemented by subclasses of BaseEmbedder"
        )
