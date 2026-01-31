from parsing.base_parser import BaseParser
class TextParser(BaseParser):
    """
    Parser for plain text (.txt) files
    
    This parser reads the entire text file and returns its content in a structured format compatible with other parsers.
    """
    def parse(self, file_path):
        """
        Parse a text file and read its content.
        
        Args:
            file_path (str): Path to the next file.
            
        Returns:
            dict: Parsed document content in the format:
                 {
                     "pages": [
                         {
                             "page_number": 1,
                             "text": text
                         }
                     ]
                 }  
        """
        with open(file_path,"r",encoding="utf-8") as file:
            text=file.read().strip()
            
        return {
                     "pages": [
                         {
                             "page_number": 1,
                             "text": text
                         }
                     ]
                 }  