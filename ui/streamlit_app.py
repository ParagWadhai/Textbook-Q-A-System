import sys
import os

# Add the root directory (textbook_qa_system) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.retrieval import hybrid_retrieve
from app.answer_generation import generate_answer

# Load corpus (sample corpus for demonstration)
corpus = [
    "This is a sample paragraph from Chapter 1.",
    "Another sample paragraph from Chapter 2.",
    "This text explains advanced topics in Chapter 1."
]

st.title("Textbook Q&A System")
query = st.text_input("Enter your question:")

if st.button("Submit"):
    # Retrieve content
    results = hybrid_retrieve(corpus, query)
    context = " ".join(results)
    
    # Generate answer
    if context:
        answer = generate_answer(context, query)
        st.write(f"**Answer:** {answer['answer']}")
        st.write(f"**Related Context:** {context}")
    else:
        st.write("No relevant content found.")

