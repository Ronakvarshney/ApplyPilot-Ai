
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)


def make_embeddings(chunks):
    texts = [chunk.page_content for chunk in chunks]

    vectors = embeddings.embed_documents(texts)

    return vectors
