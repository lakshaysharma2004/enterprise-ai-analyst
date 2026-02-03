from chunking.base_chunker import BaseChunker
from core.chunk import Chunk
class TextChunker(BaseChunker):
    """
    Chunker for plain text document
    Splits parsed text into fixed-size chunks and converts them into chunk objects
    """
    def __init__(self,chunk_size=500):
        super().__init__()
        self.chunk_size=chunk_size
        
    def chunk(self,parsed_document,source_file):
        """
        Split parsed document text into fixed-size chunks.
        Chunk size is configurable via constructor

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
        chunks=[]
        chunk_id=0
        pages=parsed_document.get("pages",[])
        for page in pages:
            page_number=page.get("page_number")
            page_text=page.get("text","")
            for start_index in range(0,len(page_text),self.chunk_size):
                chunk_text=page_text[start_index:start_index+self.chunk_size]
                chunk=Chunk(
                    text=chunk_text,
                    source_file=source_file,
                    page_number=page_number,
                    section=None,
                    chunk_id=chunk_id
                )
                chunks.append(chunk)
                chunk_id+=1
        return chunks 
            