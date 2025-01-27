from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from retrivertool import retrieval_tool
import tempfile
def prepare_document(file):
    
    loader = PyPDFLoader(file)
    docs = loader.load()

    text_splitter =RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 300)
    chunk_documents =text_splitter.split_documents(docs)
    
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vector_storage=FAISS.from_documents(chunk_documents,embeddings)
    retriever = vector_storage.as_retriever()
    tool = retrieval_tool(retriever)
    return tool