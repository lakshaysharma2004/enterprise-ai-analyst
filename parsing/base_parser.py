class BaseParser:
    """
    Base class for all document parsers.

    All concrete parsers (PDFParser, TextParser, DocxParser, etc.)
    must inherit from this class and implement the parse method.
    """
    def __init__(self):
        """
        Initializes base parser.
        Concrete Parsers will parse text from documents.
        """
        pass
    def parse(self, file_path):
        """
        Parse a document file and extract its text in a structured format.

        Args:
            file_path (str): Path to the document file.

        Returns:
            dict: A dictionary containing parsed document content.
                  Expected format:
                  {
                      "pages": [
                          {"page_number": int, "text": str}
                      ]
                  }
        """
        raise NotImplementedError(
            "parse() method must be implemented by subclasses of BaseParser"
        )
