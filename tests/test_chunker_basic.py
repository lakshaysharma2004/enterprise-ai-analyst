from chunking.text_chunker import TextChunker

parsed_document={
    "pages":[
        {
        "page_number":1,
        "text":"abcdefghijklmnopqrstuvwxyz"
    }
    ]
}

source_file="test.txt"

chunker=TextChunker(chunk_size=10)

chunks=chunker.chunk(parsed_document=parsed_document,source_file=source_file)

print(f"Number of chunks:{len(chunks)}")

for chunk in chunks:
    print(chunk)