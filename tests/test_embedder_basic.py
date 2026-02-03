from embeddings.sentence_transformer_embedder import SentenceTransformerEmbedder
import math

def cosine_similarity(vec1,vec2):
    dot=sum(a * b for a,b in zip(vec1,vec2))
    mag1=math.sqrt(sum(a*a for a in vec1))
    mag2=math.sqrt(sum(b*b for b in vec2))
    return dot/(mag1+mag2)

embedder=SentenceTransformerEmbedder()
sentence_1 = "Cats are small domestic animals"
sentence_2 = "Dogs are common household pets"
sentence_3 = "Databases store structured information"

vec1=embedder.embed(sentence_1)
vec2=embedder.embed(sentence_2)
vec3=embedder.embed(sentence_3)

print(f"Embedding dimensions: {len(vec1)}")

sim_1_2=cosine_similarity(vec1,vec2)
sim_1_3=cosine_similarity(vec1,vec3)

print(f"Cosine similarity( cats vs dogs): {sim_1_2}")
print(f"Cosine similarity (cats vs database): {sim_1_3}")