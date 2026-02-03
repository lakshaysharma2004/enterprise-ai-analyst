from parsing.text_parser import TextParser
parser=TextParser()
parsed_text=parser.parse("tests/test.txt")
print(f"Parsed Text:{parsed_text}")