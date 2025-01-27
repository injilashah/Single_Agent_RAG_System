import streamlit as st
import tempfile
from prepare import prepare_document
from agent import create_agent
from prompt_template import prompt_template
from LLM import groq_llm

# Streamlit app interface
st.set_page_config(page_title="Single Agent RAG System", layout="centered")

# Initialize session state variables
if "processing" not in st.session_state:
    st.session_state.processing = False  # Tracks if a file is being processed
if "tool" not in st.session_state:
    st.session_state.tool = None  # Stores the document processing tool

# Sidebar for document upload
with st.sidebar:
    st.header("Upload Documents")

    # Disable upload button while processing
    upload_button_disabled = st.session_state.processing
    uploaded_file = st.file_uploader(
        "Upload documents", 
        type=["pdf"], 
        disabled=upload_button_disabled
    )

    if uploaded_file and not st.session_state.processing:
        # Set processing to True
        st.session_state.processing = True
        st.write("Document uploaded successfully")
        st.write("Processing...")
        
        try:
            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file.write(uploaded_file.read())  # Save the uploaded file content
                temp_file_path = temp_file.name  # Get the path of the saved file
                
                # Now pass this file path to the prepare_document function
                tool = prepare_document(temp_file_path)  # Pass the path directly
                st.session_state.tool = tool  # Save the tool in session state
                st.success("Document processing complete!")
        except Exception as e:
            st.error(f"Error processing document: {e}")
        finally:
            # Set processing to False after processing
            st.session_state.processing = False

st.title("Single Agent RAG System")



# Query input
query = st.text_input("Enter your query:")
prompt_message = prompt_template()
llm = groq_llm()

if query:
    st.subheader("Generated Response")
    if st.session_state.tool:
        answer = create_agent(llm, st.session_state.tool, prompt_message, query)
        st.write(answer)
    else:
        st.error("Please upload and process a document first.")
else:
    st.write("Please enter your Query")
