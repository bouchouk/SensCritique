# SensCritique

# **Reocmmendation System**

**Goal:** Show reviews that are similar to the one I’m reading (same movie).

**Why embeddings (not TF-IDF)?**
- Text is in French (maybe with a bit of English). Multilingual sentence embeddings understand meaning across both languages better than using TF-IDF.

**Preprocessing**
- Keep only: `id` and cleaned `content` (so we can get the original review later by `id`).
- Drop missing values.
- Remove HTML.
- Remove punctuation.
- Lowercase text.
- Drop rows that become empty after cleaning.

**Model**
- Use a SentenceTransformer to turn each review into a vector (embedding).
- Use cosine similarity to find the closest reviews to the chosen one.
- Return top-k(5) similar reviews with their `id` and similarity score.

## Notes & AI disclosure

1) **Colab Notebook cleanup** – Many exploratory display cells were removed to keep the notebook clean and focused on the final pipeline.

2) **Project structure** – After analyzing in Colab, I packaged the recommendation system into a   small Python project for easy scripting and testing.
3) **How to run locally:** clone the repo, `cd` into it, install requirements, then run  
   `python -m tests.test_fightclub` **or** `python -m tests.test_interstellar`,  
   then enter the **id** of the review you want recommendations for.The result will be saved as a **csv** and **excel** file in **results**
4) **time:** the script may take a few seconds before asking for the ID.because it re-runs the preprocessing and recomputes the vector embeddings on each run instead of loading a cached cleaned file using joblib since we assume the raw data can change between runs (when a new review is added).

5) **AI usage** – Used AI to correct English, and to remember exact Python syntax for some functions (especially in the cosine similarity calculation).  
