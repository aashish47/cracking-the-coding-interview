# 05 The Attention Mechanism

The **Attention Mechanism** solved the "Memory Bottleneck" of previous sequential models. Instead of compressing a sequence into a single fixed-length vector, Attention allows the model to dynamically "look back" at all parts of the input sequence simultaneously.

## 1. The Bottleneck Problem

In standard RNNs, the hidden state $h_t$ must act as a summary of every word seen so far. For long sentences, the gradient disappears, and the "summary" becomes blurry. Attention bypasses this by creating a direct connection between any two words, regardless of distance.

## 2. Query, Key, and Value ($Q, K, V$)

To calculate attention mathematically, the model projects each word embedding into three distinct spaces using learned weights ($W^Q, W^K, W^V$):

- **Query ($Q$):** "What am I searching for?"
- **Key ($K$):** "What information do I offer?" (Used for matching).
- **Value ($V$):** "What is my actual content?"

## 3. The Scaled Dot-Product Math

The "Spotlight" is actually a matrix calculation. The attention score is determined by how well a Query matches a Key:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

1. **Similarity ($QK^T$):** A dot product that measures the alignment between words.
2. **Scaling ($\sqrt{d_k}$):** We divide by the square root of the dimension to prevent the Softmax from "saturating" and causing flat gradients.
3. **Softmax:** Turns the scores into probabilities (0 to 1) that sum to 100%.
4. **Weighted Sum:** We multiply those probabilities by the Values ($V$) to get the final context-aware representation.

## 4. Self vs. Cross Attention

- **Self-Attention:** $Q, K,$ and $V$ all come from the same sequence. It allows the model to resolve dependencies (e.g., matching the pronoun "it" to the noun "animal").
- **Cross-Attention:** $Q$ comes from the Decoder, while $K$ and $V$ come from the Encoder. This is the "bridge" that allows a translation model to look at the source language while writing the target language.
