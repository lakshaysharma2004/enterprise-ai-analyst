class BaseGenerator:
    """
    Base class for all answer generators.

    A generator takes a user query and retrieved chunks
    and produces a final human-readable answer.
    """

    def __init__(self):
        """
        Initialize the generator.
        Concrete generators will configure LLM clients.
        """
        pass

    def generate(self, query, chunks):
        """
        Generate an answer for a query using retrieved chunks.

        Args:
            query (str): User question.
            chunks (list[Chunk]): Retrieved relevant chunks.

        Returns:
            str: Generated answer.
        """
        raise NotImplementedError(
            "generate() must be implemented by subclasses of BaseGenerator"
        )
