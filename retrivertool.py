from langchain.tools.retriever import create_retriever_tool

def retrieval_tool(retriever):
    retrieval_tool = create_retriever_tool(retriever,"Search","search for information about documnet")
    tool= [retrieval_tool]
    return tool