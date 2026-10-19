
from sentence_transformers import SentenceTransformer

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(words):
    if not words:
        return []

    model = load_model()
    embeddings = model.encode(words, convert_to_numpy=True)
    return embeddings
