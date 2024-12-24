from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer, util

def bm25_retrieve(corpus, query):
    """Performs BM25-based retrieval."""
    tokenized_corpus = [doc.split() for doc in corpus]
    bm25 = BM25Okapi(tokenized_corpus)
    return bm25.get_top_n(query.split(), corpus, n=5)

def semantic_retrieve(corpus, query):
    """Performs semantic retrieval using Sentence-BERT."""
    model = SentenceTransformer('all-MiniLM-L6-v2')
    corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
    query_embedding = model.encode(query, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
    results = sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True)
    return [corpus[idx] for idx, score in results[:5]]

def hybrid_retrieve(corpus, query):
    """Combines BM25 and semantic retrieval results."""
    bm25_results = bm25_retrieve(corpus, query)
    semantic_results = semantic_retrieve(corpus, query)
    return list(set(bm25_results + semantic_results))
