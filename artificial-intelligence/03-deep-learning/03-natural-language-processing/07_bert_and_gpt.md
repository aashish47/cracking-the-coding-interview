# 07 BERT and GPT

The Transformer architecture led to two distinct "families" of AI models. While they share the same DNA, they were designed for very different purposes: **BERT** is built to understand, while **GPT** is built to generate.

## 1. BERT (Bidirectional Encoder Representations from Transformers)

Created by Google in 2018, BERT is an **Encoder-only** model.

- **The "Look Around" Strategy.** BERT is bidirectional, meaning it looks at the words to the left and the right of a target word simultaneously.
- **Pre-training (Masked LM).** It was trained by hiding (masking) 15% of the words in a sentence and forcing the model to guess them.
- **Best Use Case.** Tasks where you need to understand deep context, such as **Search Engines**, **Sentiment Analysis**, or **Named Entity Recognition**.

## 2. GPT (Generative Pre-trained Transformer)

Created by OpenAI, GPT is a **Decoder-only** model.

- **The "Predict Next" Strategy.** Unlike BERT, GPT is unidirectional. It only looks at the words that came before it.
- **Pre-training (Causal LM).** It was trained on the simple task of predicting the very next word in a sequence.
- **Best Use Case.** Creative writing, **Chatbots**, code generation, and anything involving **Generative AI**.

## 3. The Power of "Pre-training"

Both models follow a two-step life cycle that revolutionized AI development:

1. **Pre-training.** The model reads trillions of words from the internet to learn how language works in general. This is extremely expensive.
2. **Fine-tuning.** You take that "pre-trained" giant and train it for a few hours on a specific task (like medical diagnosis or legal document review).

## 4. Scaling Laws

The biggest difference between GPT-2, GPT-3, and GPT-4 is **Scale**.

- **Parameters.** Increasing the number of "knobs" the model can turn.
- **Data.** Feeding it more diverse and high-quality books, websites, and code.
- **Compute.** Using more powerful GPU clusters for longer periods.
  As these models grew, they began to show "emergent abilities," such as reasoning and basic math, that were not explicitly programmed.

## 5. Summary Table

| Feature          | BERT                               | GPT                            |
| ---------------- | ---------------------------------- | ------------------------------ |
| **Architecture** | Encoder Only                       | Decoder Only                   |
| **Context**      | Bidirectional (Left & Right)       | Unidirectional (Left only)     |
| **Objective**    | Fill in the blanks (Understanding) | Predict next word (Generation) |
| **Company**      | Google                             | OpenAI                         |
