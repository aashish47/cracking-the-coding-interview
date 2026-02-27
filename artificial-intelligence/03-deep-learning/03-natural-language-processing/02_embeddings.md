# 02 Word Embeddings

If one-hot encoding is a simple ID badge, **Embeddings** are a detailed personality profile. They represent words as **Dense Vectors** (e.g., a vector of size 300) where the numerical distance between vectors represents the similarity in meaning.

## 1. How Embeddings are Created: The Feature Matrix

Imagine we want to describe words based on "concepts." Instead of a giant sparse list, we create a **Dense Matrix** where each row is a word and each column is a "hidden feature" (like _Living Being_, _Royalty_, _Food_, or _Gender_).

### **Example: A 4-Dimensional Embedding Space**

| Word       | Living Being | Royalty | Gender (Masculine) | Food |
| ---------- | ------------ | ------- | ------------------ | ---- |
| **King**   | 0.99         | 0.95    | 0.92               | 0.02 |
| **Queen**  | 0.99         | 0.94    | 0.05               | 0.01 |
| **Apple**  | 0.01         | 0.02    | 0.01               | 0.98 |
| **Orange** | 0.01         | 0.01    | 0.01               | 0.97 |

- **Observation:** "King" and "Queen" have nearly identical values for _Living Being_ and _Royalty_, making them "close" in those dimensions.
- **The Magic:** In real life, we don't name these columns. The neural network discovers these features (e.g., Column 42 might represent "Mechanicalness") during training.

## 2. Measuring Similarity: Cosine Similarity

In a one-hot system, the distance between any two different words is always the same. In Embeddings, we use **Cosine Similarity** to measure the angle between two vectors.

- **Formula:** $\text{Similarity} = \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|}$
- **Logic:** If the angle is $0^{\circ}$, the words are identical in context. If the angle is $90^{\circ}$, they are unrelated.

## 3. Word2Vec: Learning by Association

Developed by Google, Word2Vec learns by assuming that **"a word is characterized by the company it keeps."**

- **CBOW (Continuous Bag of Words):** The model hides the middle word and tries to guess it.

    _Input:_ ["The", "cat", "___", "on", "the"] $\rightarrow$ _Target:_ "sat".

- **Skip-gram:** The model takes one word and tries to guess the neighbors.

    _Input:_ "sat" $\rightarrow$ _Target:_ ["The", "cat", "on", "the"].

- **Training Logic:** The "Weights" learned inside the neural network during this guessing game become the **Embedding Vectors**.

## 4. GloVe (Global Vectors)

Developed by Stanford, GloVe uses a **Co-occurrence Matrix**.

- It counts how often "Ice" appears near "Solid" vs. "Steam" appearing near "Solid" across the entire internet.
- It then uses matrix factorization to squash that giant count-table into small, dense vectors.

## 5. Why Embeddings are "Static" (The Polysemy Problem)

Traditional embeddings (Word2Vec, GloVe) are **static**. This means the word "Bank" always has the same vector, regardless of context.

- **The Limitation:** They cannot handle **Polysemy** (words with multiple meanings).
- _Sentence A:_ "I went to the **bank** to deposit money."
- _Sentence B:_ "I sat on the river **bank**."

- In these models, the "Bank" vector is a confusing average of both meanings.

## 6. Summary Comparison

| Feature              | One-Hot Encoding                | Word Embeddings              |
| -------------------- | ------------------------------- | ---------------------------- |
| **Data Type**        | Sparse (mostly zeros)           | Dense (all real numbers)     |
| **Dimensionality**   | Huge (Vocab size, e.g., 50,000) | Small (typically 100–1000)   |
| **Semantic Meaning** | None ($Hotel \perp Motel$)      | High ($Hotel \approx Motel$) |
| **Relationship**     | Hard-coded / Manual             | Learned automatically        |
| **Memory**           | Inefficient                     | Highly Efficient             |
