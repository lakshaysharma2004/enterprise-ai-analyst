class BaseChunker:
    """
    Base class for all document chunkers.

    All concrete chunkers (TextChunker, PDFChunker, DocxChunker, etc.)
    must inherit from this class and implement the chunk method.
    """

    def chunk(self, parsed_document, source_file):
        """
        Split a parsed document into chunks.

        Args:
            parsed_document (dict): Parsed document content in the format:
                {
                    "pages": [
                        {"page_number": int, "text": str}
                    ]
                }
            source_file (str): Name of the source document file.

        Returns:
            list: A list of Chunk objects.
        """
        raise NotImplementedError(
            "chunk() method must be implemented by subclasses of BaseChunker"
        )