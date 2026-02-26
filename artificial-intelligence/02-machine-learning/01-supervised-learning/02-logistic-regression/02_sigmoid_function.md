# 02 Sigmoid Function

The **Sigmoid Function** (also known as the Logistic Function) is the mathematical core of Logistic Regression. It serves as the transformation that maps any real-valued number from the linear model into a probability value between 0 and 1.

## 1. The Mathematical Formula

The Sigmoid function, denoted as $g(z)$, is defined as:

$$g(z) = \frac{1}{1 + e^{-z}}$$

Where:

- **$z$**: The output from the linear equation $z = \vec{w} \cdot \vec{x} + b$.
- **$e$**: Euler's number (approximately 2.718).

## 2. Properties of the Sigmoid Curve

The function produces an "S-shaped" curve with specific mathematical properties:

- **Asymptotes:** As $z \to \infty$, $g(z) \to 1$. As $z \to -\infty$, $g(z) \to 0$.
- **The Midpoint:** When $z = 0$, $g(z) = 0.5$. This is the default threshold for classification.
- **Range:** The output is strictly bounded between $(0, 1)$, making it a valid probability.

## 3. Applying the Function to the Model

In Logistic Regression, we substitute the linear expression into the Sigmoid function to get the prediction $\hat{y}$:

$$\hat{y} = \frac{1}{1 + e^{-(\vec{w} \cdot \vec{x} + b)}}$$

This output represents the probability that the target $y$ belongs to the positive class (1):

$$P(y=1 | \vec{x}; \vec{w}, b) = \hat{y}$$

$$P(y=0 | \vec{x}; \vec{w}, b) = 1 - \hat{y}$$

## 4. Why Use Sigmoid?

1. **Probability Mapping:** It converts "confidence scores" ($z$) into meaningful probabilities.
2. **Differentiability:** The function is smooth and differentiable everywhere, which is a requirement for optimization via Gradient Descent.
3. **Thresholding:** It provides a clear inflection point at $z=0$ to distinguish between classes.
