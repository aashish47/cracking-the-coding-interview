# 06 Gradient Descent

## 1. The Core Concept

Gradient Descent is an optimization algorithm used to find the minimum of a function. In ML, that function is the **Cost Function** (the measure of how wrong the model's predictions are).

- **The Goal:** Adjust the model's parameters (weights $w$ and bias $b$) to reach the lowest possible error.
- **The Analogy:** Imagine you are blindfolded on a mountain (high error) and want to get to the valley (lowest error). You feel the slope with your feet and take a step in the direction where the ground goes down.

## 2. The Key Components

### A. The Cost Function ($J$)

This calculates the error between the predicted value ($\hat{y}$) and the actual value ($y$). A common one is Mean Squared Error (MSE):
$$J(w, b) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

### B. The Learning Rate ($\alpha$)

This defines the size of the steps we take down the hill.

- **Too small:** The model takes forever to learn (slow convergence).
- **Too large:** The model might overshoot the bottom and bounce back and forth, never finding the minimum.

### C. The Gradient

The mathematical derivative (slope) of the cost function.

- If the slope is **positive**, we move in the negative direction.
- If the slope is **negative**, we move in the positive direction.

### D. The Update Rule

The parameters are updated iteratively using the following formula:
$$w = w - \alpha \frac{\partial J}{\partial w}$$
$$b = b - \alpha \frac{\partial J}{\partial b}$$
Where $\frac{\partial J}{\partial w}$ and $\frac{\partial J}{\partial b}$ are the partial derivatives of the cost function with respect to the weights and bias.

## 3. Types of Gradient Descent

| Type                 | How it works                                        | Pros/Cons                                                      |
| :------------------- | :-------------------------------------------------- | :------------------------------------------------------------- |
| **Batch**            | Uses all training data to take one step.            | Very stable, but very slow for large datasets.                 |
| **Stochastic (SGD)** | Uses one random data point to take a step.          | Fast and can escape local minima, but very "noisy" (zig-zags). |
| **Mini-Batch**       | Uses a small group (e.g., 32 or 64) of data points. | The Standard. Best balance of speed and stability.             |

## 4. Convergence and Local Minima

- **Convergence:** When the gradient is nearly zero, meaning we've reached the bottom.
- **Local Minima:** In complex models (like Deep Learning), the "mountain" has many small dips. You might get stuck in a "pothole" (local minimum) instead of the absolute bottom of the mountain (global minimum).
