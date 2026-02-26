# 06 Multiclass Classification

While standard Logistic Regression is designed for binary classification (0 or 1), real-world problems often involve multiple categories (e.g., classifying a handwritten digit as 0–9). We use two primary strategies to extend the model for multiclass tasks.

## 1. One-vs-Rest (OvR)

This approach, also known as **One-vs-All**, breaks the multiclass problem into multiple independent binary classification problems.

- **How it works:** If you have 3 classes (A, B, and C), you train 3 separate classifiers:

1. **Classifier 1:** Class A vs. (Class B and C)
2. **Classifier 2:** Class B vs. (Class A and C)
3. **Classifier 3:** Class C vs. (Class A and B)

- **Prediction:** To classify a new input, you run it through all classifiers. The class with the **highest probability** score is chosen as the final prediction.

## 2. Softmax Regression (Multinomial Logistic Regression)

Softmax is a more direct generalization of logistic regression for multiple classes. Instead of training separate classifiers, it uses a single model with multiple output nodes—one for each class.

### The Softmax Function

For a problem with $K$ classes, the probability that an input belongs to class $j$ is:

$$P(y=j | \vec{x}) = \frac{e^{z_j}}{\sum_{k=1}^{K} e^{z_k}}$$

Where:

- **$z_j$**: The linear output ($\vec{w}_j \cdot \vec{x} + b_j$) for class $j$.
- **Denominator**: The sum of $e^z$ for all possible classes, ensuring that all probabilities sum up to exactly **1.0**.

## 3. Cost Function: Categorical Cross-Entropy

For multiclass classification using Softmax, we replace the Binary Log Loss with **Categorical Cross-Entropy**:

$$J = -\sum_{j=1}^{K} y_j \log(\hat{y}_j)$$

In this formula, $y_j$ is 1 for the correct class and 0 for all others. The model only "pays attention" to the probability it assigned to the correct class; the higher the probability of the correct class, the lower the cost.

## 4. Comparison of Methods

| Feature         | One-vs-Rest (OvR)                              | Softmax Regression                               |
| --------------- | ---------------------------------------------- | ------------------------------------------------ |
| **Model Type**  | Multiple binary classifiers.                   | Single integrated model.                         |
| **Probability** | Probabilities don't necessarily sum to 1.      | Probabilities always sum to 1.                   |
| **Usage**       | Common in SVMs and simple Logistic Regression. | Standard for Neural Networks and Deep Learning.  |
| **Complexity**  | Simple to implement on top of binary code.     | More computationally intensive for many classes. |
