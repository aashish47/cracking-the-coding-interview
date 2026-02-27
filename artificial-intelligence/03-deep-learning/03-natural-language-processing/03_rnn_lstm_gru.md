# 03 RNN LSTM GRU

Standard neural networks assume all inputs are independent. However, language is a sequence—to understand word number 10, you often need to remember word number 1. **Recurrent Neural Networks (RNNs)** were designed to solve this by adding "memory."

## 1. The Recurrent Neuron

An RNN has a "hidden state" ($h$) that acts as its memory. As it processes each word in a sentence, it passes that hidden state to the next step.

- **The Loop.** The output of the neuron at time $t$ is fed back into itself at time $t+1$.
- **The Problem.** RNNs have a very short memory. As a sentence gets longer, the information from the beginning of the sentence starts to fade away. This is called the **Vanishing Gradient Problem**.

## 2. LSTM (Long Short-Term Memory)

LSTMs were designed specifically to fix the short-term memory problem. They use a complex internal structure called **"Gates"** to decide what to remember and what to forget.

- **The Cell State.** Think of this as a "long-term memory" conveyor belt that runs through the whole sequence.
- **Forget Gate.** Decides which information is no longer useful (e.g., a subject changed from singular to plural).
- **Input Gate.** Decides which new information is worth adding to the long-term memory.
- **Output Gate.** Decides what part of the memory to use for the current output.

## 3. GRU (Gated Recurrent Unit)

A GRU is a simpler, faster version of the LSTM.

- **Combined Gates.** It merges the forget and input gates into a single "Update Gate."
- **Efficiency.** Because it has fewer parameters, it trains faster and often performs just as well as LSTM on smaller datasets.

## 4. Bidirectional RNNs

Sometimes, to understand a word, you need to know what comes **after** it.

- **How it works.** A Bidirectional RNN runs two sequences: one from left-to-right and one from right-to-left.
- **Result.** At any point in the sentence, the model has context from both the past and the future.

## 5. Summary Table

| Architecture   | Memory Type   | Best Use Case                           |
| -------------- | ------------- | --------------------------------------- |
| **Simple RNN** | Very Short    | Very short sequences, simple patterns.  |
| **LSTM**       | Long & Short  | Complex language tasks, long documents. |
| **GRU**        | Long & Short  | Faster training, similar to LSTM.       |
| **Bi-RNN**     | Past & Future | Named Entity Recognition, Translation.  |
