import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from system.clean import f_content, i_content

#Load Bert encoder and turn our contents into vector embeddings
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
f_emb = model.encode(f_content["review_content"].tolist())
i_emb = model.encode(i_content["review_content"].tolist())

def get_similar_reviews(df, cleaned_df, embeddings, source_id, k):
    """Find k most similar reviews using cosine similarity."""

    #Find the review index
    check = cleaned_df["id"] == source_id
    if not check.any():
        raise ValueError(f"Source ID {source_id} not found in dataset")
        
    source_idx = cleaned_df.index[cleaned_df["id"] == source_id][0]
    query_embedding = embeddings[source_idx].reshape(1, -1)

    #Calculate similarities
    similarities = cosine_similarity(embeddings, query_embedding).ravel()

    #Remove the current content
    similarities[source_idx] = -1

    #Get top k similar items
    top_indices = np.argsort(-similarities)[:k]
    top_ids = cleaned_df.iloc[top_indices]["id"].tolist()

    #Results
    results = cleaned_df.iloc[top_indices].copy()
    original_reviews = df.set_index("id").loc[top_ids, "review_content"]

    return pd.DataFrame({
        "cleaned_content": results["review_content"].values,
        "original_content": original_reviews.values,
        "id": top_ids,
        "similarity_score": similarities[top_indices].round(3)
    })