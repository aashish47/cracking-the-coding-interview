# 03 Univariate Model

The **Univariate Model** focuses on finding the optimal parameters $w$ and $b$ for a single-feature linear relationship. The model uses the specific gradients of the Cost Function to iteratively adjust these parameters.

## 1. The Model Equation

The predicted output is calculated as:

$$\hat{y}^{(i)} = wx^{(i)} + b$$

Where $x^{(i)}$ represents the $i^{th}$ training example and $y^{(i)}$ represents the actual target.

## 2. Gradient Descent Mathematics

The goal is to minimize the Cost Function $J(w, b)$ by updating $w$ and $b$ in the direction of the steepest descent.

### The Simultaneous Update Rule

Both parameters must be updated at the same time in each iteration.

$$w := w - \alpha \frac{\partial J(w,b)}{\partial w}$$

$$b := b - \alpha \frac{\partial J(w,b)}{\partial b}$$

### The Partial Derivatives (Gradients)

The derivatives represent the slope of the cost function relative to each parameter. For Mean Squared Error (MSE), these are calculated as follows:

**1. Gradient for $w$:**

$$\frac{\partial J(w, b)}{\partial w} = \frac{1}{m} \sum_{i=1}^{m} (wx^{(i)} + b - y^{(i)})x^{(i)}$$

**2. Gradient for $b$:**

$$\frac{\partial J(w, b)}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} (wx^{(i)} + b - y^{(i)})$$

## 3. Mathematical Components

| Component                      | Definition        | Role                                                      |
| ------------------------------ | ----------------- | --------------------------------------------------------- |
| **$\alpha$**                   | Learning Rate     | Controls the size of the update step.                     |
| **$m$**                        | Training Set Size | Total number of data points used in the summation.        |
| **$(wx^{(i)} + b - y^{(i)})$** | Error Term        | The difference between the prediction and the target.     |
| **$x^{(i)}$**                  | Input Factor      | Scales the gradient for $w$ based on the input magnitude. |

## 4. Iterative Process

1. **Initialize:** Set $w$ and $b$ to initial values (often 0).
2. **Compute Gradients:** Calculate the partial derivatives for the current $w$ and $b$ using all $m$ examples.
3. **Update:** Apply the update rule using the learning rate $\alpha$.
4. **Repeat:** Continue until the change in $J(w, b)$ is negligible (**Convergence**).
