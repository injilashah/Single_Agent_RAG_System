import streamlit as st
import tempfile
from prepare import prepare_document
from agent import create_agent
from prompt_template import prompt_template
from LLM import groq_llm
from langchain.schema import Document


# Streamlit app 
st.set_page_config(page_title="Single Agent RAG System", layout="centered")


with st.sidebar:
    st.header("Upload Documents")

    uploaded_file = st.file_uploader(
        "Upload documents", 
        type=["pdf"]
    )

    

    if uploaded_file:
        st.write("Document uploaded successfully")
        st.write("Processing...")

        try:
            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file.write(uploaded_file.read())  # Save the uploaded file content
                temp_file_path = temp_file.name  # Get the path of the saved file

                # Pass this file path to the prepare_document function
                tool,retriever = prepare_document(temp_file_path)  # Pass the path directly
                st.success("Document processing complete!")
                
        except Exception as e:
            st.error(f"Error processing document: {e}")

st.title("Single Agent RAG System")

# Query input
query = st.text_input("Enter your query:")




if query:
    
    
    
    if tool and retriever:
        
        retrieved_documents = retriever.get_relevant_documents(query)
        st.subheader("Retrieved_documents")
        for i, doc in enumerate(retrieved_documents, 1):
            st.write(f"Document {i} : {doc.page_content[:200]}")
        prompt_message = prompt_template()
        llm = groq_llm()
        st.subheader("Generated Response")
        answer = create_agent(llm, tool, prompt_message, query)
        
        st.write(answer["output"])
    else:
        st.error("Please upload and process a document first.")
else:
    st.write("Please enter your query.")
