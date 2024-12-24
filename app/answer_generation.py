from transformers import pipeline

def generate_answer(context, question):
    """Generates answers using an LLM."""
    qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
    return qa_pipeline({"context": context, "question": question})
