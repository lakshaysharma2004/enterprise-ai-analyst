from sentence_transformers import SentenceTransformer
from embeddings.base_embedder import BaseEmbedder
class SentenceTransformerEmbedder(BaseEmbedder):
    """
    It uses a Sentence Transformer Embedder model.
    It generates semantic embeddings for text
    """
    def __init__(self,model_name="all-MiniLM-L6-v2"):
        super().__init__()
        self.model=SentenceTransformer(model_name)
        self.dimension=384
    def embed(self,text):
        """
        Convert a single text into a numerical vector.

        Args:
            text (str): Input text to be embedded.

        Returns:
            list[float]: Embedding vector representing the text.
        """
        embedding=self.model.encode(text)
        return embedding.tolist()
    def embed_batch(self,texts):
        """
        Convert multiple texts into numerical vectors.

        Args:
            texts (list[str]): List of input texts to be embedded.

        Returns:
            list[list[float]]: List of embedding vectors.
        """
        embeddings=self.model.encode(texts)
        return [vector.tolist() for vector in embeddings]
    
    