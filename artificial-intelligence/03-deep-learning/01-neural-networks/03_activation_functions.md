# 03 Activation Functions

Activation functions are the "gatekeepers" of a neural network. Without them, a neural network is just a giant linear regression model, no matter how many layers you add. They introduce **non-linearity**, which allows the network to learn complex, curvy patterns in data.

## 1. Why do we need them?

If we don't use activation functions, the output of every layer is just a linear combination of the inputs ($y = wx + b$). If you stack 100 linear layers, the result is still mathematically equivalent to a single linear layer.

**Non-linearity** allows the network to "bend" the space to fit data that isn't just a straight line.

## 2. Common Activation Functions

### A. Sigmoid

The Sigmoid function squashes any input into a range between **0 and 1**.

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

- **Best for:** The output layer of a binary classification model (gives a probability).
- **Weakness:** The **Vanishing Gradient** problem. For very high or very low inputs, the curve becomes flat, meaning the gradient is nearly zero, which stops the network from learning.

### B. Tanh (Hyperbolic Tangent)

Similar to Sigmoid, but squashes values between **-1 and 1**.

$$\tanh(z) = \frac{e^{z} - e^{-z}}{e^{z} + e^{-z}}$$

- **Best for:** Hidden layers. Since the output is zero-centered (mean is 0), it often makes the next layer's learning easier.
- **Weakness:** Still suffers from the vanishing gradient problem.

### C. ReLU (Rectified Linear Unit)

The "gold standard" for hidden layers in modern deep learning.

$$f(z) = \max(0, z)$$

- **How it works:** If the input is positive, it passes it through. If it's negative, it outputs zero.
- **Pros:** It is computationally very fast and solves the vanishing gradient problem for positive values.
- **Cons:** **"Dying ReLU"**—if a neuron gets stuck in the negative range, it always outputs 0 and effectively "dies" (stops learning).

### D. Leaky ReLU

A variation of ReLU that prevents neurons from "dying."

$$f(z) = \max(0.01z, z)$$

- **How it works:** Instead of being zero for negative inputs, it has a very small slope (e.g., 0.01).
- **Pros:** It ensures that even negative inputs have a small gradient, allowing the neuron to eventually "wake up" and continue learning.

### E. Softmax

Used exclusively in the **output layer** for multi-class classification. It exponentiates the inputs and normalizes them.

$$\sigma(\vec{z})_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}$$

- **How it works:** It turns a vector of numbers into a vector of probabilities that sum up to **1.0**.
- **Example:** If you are classifying an image as Cat, Dog, or Bird, Softmax might output $[0.1, 0.7, 0.2]$.

### F. Swish (SiLU)

A modern alternative to ReLU discovered by Google researchers.

$$f(z) = z \cdot \sigma(z)$$

- **Pros:** It is a smooth, non-monotonic function that often outperforms ReLU in very deep networks (e.g., EfficientNet).
- **Cons:** Slightly more computationally expensive than ReLU.

### G. GELU (Gaussian Error Linear Unit)

The standard activation function for modern Transformers (like BERT and GPT).

$$GELU(z) = z \cdot \Phi(z)$$

- **How it works:** It weights the input by its probability under a Gaussian distribution. It is essentially a "smoother" ReLU that allows for a small gradient in the negative range.
- **Pros:** Currently the state-of-the-art for NLP and Transformer-based architectures.

## 3. Comparison

| Function       | Range                 | Main Use Case                 | Key Issue          |
| -------------- | --------------------- | ----------------------------- | ------------------ |
| **Sigmoid**    | (0, 1)                | Binary Output Layer           | Vanishing Gradient |
| **Tanh**       | (-1, 1)               | Hidden Layers                 | Vanishing Gradient |
| **ReLU**       | [0, $\infty$)         | Hidden Layers                 | Dying ReLU         |
| **Leaky ReLU** | (-$\infty$, $\infty$) | Hidden Layers (if ReLU fails) | None               |
| **Softmax**    | (0, 1)                | Multi-class Output Layer      | None               |
| **Swish**      | [≈-0.28, $\infty$)    | Deep Hidden Layers            | Computation Cost   |
| **GELU**       | [≈-0.17, $\infty$)    | Transformers / NLP            | Computation Cost   |

## 4. How to Choose?

1. **Hidden Layers:** Start with **ReLU**. If you notice many neurons are "dying," try **Leaky ReLU**.
2. **Output Layer (Binary):** Use **Sigmoid**.
3. **Output Layer (Multi-class):** Use **Softmax**.
4. **Output Layer (Regression):** Use **Linear** (no activation) or **ReLU** (if the value must be positive).
