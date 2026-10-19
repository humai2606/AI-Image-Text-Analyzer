from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(text):
    """
    Convert text into sentence embeddings.
    """

    embedding = model.encode(text)

    return embedding


def get_embedding_dimension():
    """
    Return the size of the generated embedding vector.
    """

    return model.get_sentence_embedding_dimension()


if __name__ == "__main__":

    text = "Artificial Intelligence is changing the world."

    embedding = create_embeddings(text)

    print("Input text:")
    print(text)

    print("\nEmbedding dimension:")
    print(len(embedding))

    print("\nFirst 10 embedding values:")
    print(np.round(embedding[:10], 4))