from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)


def load_pdf(path):
    loader = PyPDFLoader(path)
    return loader.load()


def make_chunk(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    return splitter.split_documents(documents)


def make_embeddings(chunks):
    texts = [chunk.page_content for chunk in chunks]

    vectors = embeddings.embed_documents(texts)

    return vectors


def orchestration(path):
    docs = load_pdf(path)

    chunks = make_chunk(docs)

    vectors = make_embeddings(chunks)

    return chunks, vectors