class Chunk:
    def __init__(self, text, source_file, page_number=1, section=None, chunk_id=None):
        """Represents a single chunk of text extracted from a document.

        Args:
            text (str): The textual content of the chunk.
            source_file (str): Name of the source document file.
            page_number (int, optional): Page number from which the chunk was extracted. Defaults to 1.
            section (str, optional): Section or heading name of the chunk. Defaults to None.
            chunk_id (int or str, optional): Unique identifier for the chunk. Defaults to None.
        """
        self.text = text
        self.source_file = source_file
        self.page_number = page_number
        self.section = section
        self.chunk_id = chunk_id

    def __repr__(self):
        """Returns a readable string representation of the Chunk.

        Returns:
            str: Short, human-readable summary of the chunk.
        """
        preview = self.text.replace("\n", " ")[:50]
        if len(self.text) > 50:
            preview += "..."

        return (
            f"Chunk(id={self.chunk_id}, file={self.source_file}, "
            f"page={self.page_number}, section={self.section}, "
            f"text='{preview}')"
        )

    def to_dict(self):
        """Converts the Chunk object into a dictionary.

        Returns:
            dict: Dictionary representation of the chunk.
        """
        return {
            "chunk_id": self.chunk_id,
            "text": self.text,
            "source_file": self.source_file,
            "page_number": self.page_number,
            "section": self.section,
        }
