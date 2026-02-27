# 06 The Transformer Architecture

In 2017, Google published **"Attention Is All You Need,"** introducing the Transformer. It discarded recurrence (RNNs) entirely, relying on parallelized attention blocks.

## 1. Positional Encoding

Since Transformers process all words at once, they are "permutation invariant" (they don't naturally know the order).

- **The Fix:** We inject a unique mathematical signal into each word embedding using Sine and Cosine waves:

$$PE_{(pos, 2i)} = \sin(pos / 10000^{2i/d_{model}})$$

$$PE_{(pos, 2i+1)} = \cos(pos / 10000^{2i/d_{model}})$$

This allows the model to differentiate between "The dog bit the man" and "The man bit the dog."

## 2. Multi-Head Attention (MHA)

Instead of one big attention calculation, the Transformer runs $h$ smaller attention "heads" in parallel.

- **The Benefit:** One head can focus on syntax (verbs), another on semantics (meaning), and another on literal repetition. These are then concatenated and projected back to the original size.

## 3. The "Add & Norm" and Feed-Forward Blocks

Between the attention layers, the Transformer uses two critical components to keep training stable:

- **Residual Connections (Add):** Like ResNet, these allow gradients to bypass layers, preventing the vanishing gradient problem.
- **Layer Normalization (Norm):** Rescales the values to a mean of 0 and variance of 1, ensuring the math doesn't "explode" as the model gets deeper.
- **Feed-Forward Network (FFN):** A simple two-layer neural network applied to each word independently to process the information gathered by the attention heads.

## 4. The Encoder-Decoder Hierarchy

- **Encoder (e.g., BERT):** Uses **Bi-directional Self-Attention** to build a deep understanding of the input.
- **Decoder (e.g., GPT):** Uses **Masked Self-Attention** (so it can't "cheat" by looking at future words) and **Cross-Attention** to generate text one token at a time.

## 5. Summary Table

| Problem                | RNN Solution              | Transformer Solution            |
| ---------------------- | ------------------------- | ------------------------------- |
| **Speed**              | Sequential (Slow)         | **Parallel (Fast)**             |
| **Memory**             | Hidden State "Bottleneck" | **Global Attention (Infinite)** |
| **Vanishing Gradient** | Complex Gates (LSTM/GRU)  | **Residual Connections + Norm** |
