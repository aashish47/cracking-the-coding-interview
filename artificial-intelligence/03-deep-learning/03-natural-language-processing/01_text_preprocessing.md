# 01 Text Preprocessing

Computers cannot read text; they can only process numbers. **Text Preprocessing** is the pipeline of cleaning and converting raw human language into a numerical format (Tensors).

## 1. Tokenization

_The first step in defining the "unit" of study._

- **Word Tokenization:** `["I", "love", "AI"]`.
- **Character Tokenization:** Splitting into letters. Memory efficient but loses semantic meaning.
- **Subword Tokenization (Modern Standard):** Used by GPT/BERT. It splits rare words into chunks (`"unhappiness"` $\rightarrow$ `["un", "happi", "ness"]`).
- **Context:** This solved the **OOV (Out-Of-Vocabulary)** problem that plagued older models.

## 2. Normalization & Reduction

_Leveling the playing field so "Apple" = "apple"._

- **Normalization:** Lowercasing and noise removal (stripping HTML/punctuation).
- **Stop Word Removal:** Deleting high-frequency words ("the", "is").
- **Context Note:** This is common in **Classical ML** (like Spam Filters) but often skipped in **Deep Learning** because Transformers use those words to understand grammar.

- **Stemming vs. Lemmatization:** \* **Stemming:** Crude chopping (`"flies"` $\rightarrow$ `"fli"`).
- **Lemmatization:** Linguistic root finding (`"saw"` $\rightarrow$ `"see"`).

## 3. N-Grams

_Moving beyond single words to capture phrases._

- **Unigram ($n=1$):** Analyzes each word as an isolated unit. Example: `["I", "love", "AI"]`.
- **Bigram ($n=2$):** Examines adjacent pairs. Example: `["I love", "love AI"]`.
- **Trigram ($n=3$):** Examines sequences of three. Example: `["I love AI"]`.

**The Logic:** One calculates the probability of a specific word appearing based on the preceding $n-1$ words:
$$P(w_n | w_{n-1}, ..., w_{n-n+1})$$

**The Limitation:** These models suffer from **Contextual Myopia**. A Bigram model retains a memory of only a single previous word, failing to capture long-range dependencies.

## 4. TF-IDF (Term Frequency - Inverse Document Frequency)

_Determining which words actually matter._

- **Term Frequency (TF):** Measures the density of a term in a document.
- **Inverse Document Frequency (IDF):** Penalizes terms that appear frequently across the entire corpus (like "the", "and").
  **The Formula:**
  $$\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \log\left(\frac{N}{\text{DF}(t)}\right)$$

## 5. Vectorization

_The final conversion into Tensors._

- **One-Hot Encoding:** A sparse vector where only the index of the word is $1$.
- Example: If vocab is `["Apple", "Banana", "Cat"]`, "Banana" is `[0, 1, 0]`.

- **The Sparsity Problem:** As your vocabulary grows to 50,000 words, your vectors become 50,000 numbers long—but 49,999 of them are zeros. This is mathematically "hollow" and computationally expensive.

## 6. The Semantic Wall

_The fundamental limitation of everything above._

Even with TF-IDF and N-Grams, these vectors are **orthogonal** (perpendicular). They have no concept of similarity:
$\text{Hotel} \cdot \text{Motel} = 0$. Mathematically, a "Hotel" is just as similar to a "Banana" as it is to a "Motel." To solve this, we move to **Dense Word Embeddings**.
