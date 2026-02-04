from generator.base_generator import BaseGenerator
from openai import OpenAI

class SimpleRAGGenerator(BaseGenerator):
    """
    A simple Retrieval-Augmented Generation (RAG) generator.

    This generator takes a user query and retrieved chunks,
    constructs a constrained prompt, and uses an OpenAI LLM
    to generate a grounded answer.
    """

    def __init__(self, model_name="gpt-3.5-turbo", temperature=0.0):
        """
        Initialize the RAG generator.

        Args:
            model_name (str): OpenAI model to use.
            temperature (float): Controls randomness of generation.
        """
        super().__init__()
        self.model_name = model_name
        self.temperature = temperature
        self.client = OpenAI()

    def generate(self, query, chunks):
        """
        Generate an answer for a query using retrieved chunks.

        Args:
            query (str): User question.
            chunks (list[Chunk]): Retrieved relevant chunks.

        Returns:
            str: Generated answer.
        """
        context_parts = []
        for chunk in chunks:
            context_parts.append(chunk.text)
        context_text = "\n\n".join(context_parts)

        prompt = (
            "You are an assistant that answers questions using ONLY the provided context.\n"
            "If the answer cannot be found in the context, say \"I don't know\".\n\n"
            "Context:\n"
            f"{context_text}\n\n"
            "Question:\n"
            f"{query}\n\n"
            "Answer:"
        )

        response = self.client.chat.completions.create(
            model=self.model_name,
            temperature=self.temperature,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        answer = response.choices[0].message.content.strip()
        return answer
