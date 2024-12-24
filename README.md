#Textbook Q&A System
This system enables users to query large textbooks and retrieve accurate, contextually relevant answers using hierarchical indexing and advanced retrieval techniques.

##Features
-**PDF Content Extraction: Extracts text from large textbooks for analysis.**
-**Hierarchical Tree-based Indexing: Organizes content into chapters, sections, and paragraphs for efficient retrieval.**
-**Hybrid Retrieval (BM25 + Semantic Search): Combines traditional and deep learning-based search techniques.**
-**Question Answering with LLM: Generates precise answers using advanced language models.**
-**Interactive User Interface: A Streamlit-powered interface for user interaction.**

##Setup
1. Clone the repository:
```bash
git clone https://github.com/your-username/textbook-qa-system.git
cd textbook-qa-system

2. Create a virtual environment:
```bash
python -m venv venv

3. Activate the virtual environment:
-**Windows:**
```bash
venv\Scripts\activate
-**macOS/Linux:**
```bash
source venv/bin/activate

4. Install dependencies:
```bash
pip install -r requirements.txt

##Run the Application
1. Launch the Streamlit app:
```bash
streamlit run ui/streamlit_app.py

2. Open the displayed URL in your browser (e.g., http://localhost:8501).

##How to Use
1. Enter a query in the input box to search for answers.
2. View generated answers alongside relevant textbook sections and chapters.



