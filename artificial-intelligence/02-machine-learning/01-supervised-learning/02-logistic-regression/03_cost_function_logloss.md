# 03 Cost Function (Log Loss)

In Logistic Regression, we cannot use the Mean Squared Error (MSE) from Linear Regression because the Sigmoid function would result in a "non-convex" cost function with many local minima. Instead, we use **Log Loss** (also called Binary Cross-Entropy).

## 1. The Individual Loss Function

For a single training example $(x^{(i)}, y^{(i)})$, the loss $L(\hat{y}^{(i)}, y^{(i)})$ is calculated based on the actual class:

$$L(\hat{y}^{(i)}, y^{(i)}) = \begin{cases} -\log(\hat{y}^{(i)}) & \text{if } y^{(i)} = 1 \\ -\log(1 - \hat{y}^{(i)}) & \text{if } y^{(i)} = 0 \end{cases}$$

### Mathematical Logic:

- **If $y=1$:** As the prediction $\hat{y}$ approaches 1, the loss goes to 0. As $\hat{y}$ approaches 0, the loss goes to $\infty$.
- **If $y=0$:** As the prediction $\hat{y}$ approaches 0, the loss goes to 0. As $\hat{y}$ approaches 1, the loss goes to $\infty$.

## 2. The Unified Cost Function ($J$)

To simplify the implementation, we combine these two cases into a single equation for the entire training set of $m$ examples:

$$J(\vec{w}, b) = -\frac{1}{m} \sum_{i=1}^{m} \left[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \right]$$

### Why this formula works:

- When $y^{(i)} = 1$, the second term $(1 - y^{(i)})$ becomes 0, leaving only the $\log(\hat{y})$ term.
- When $y^{(i)} = 0$, the first term $y^{(i)}$ becomes 0, leaving only the $\log(1 - \hat{y})$ term.

## 3. Simplified Gradient Descent

Remarkably, when we take the derivative of this Log Loss function with respect to $w$ and $b$, the update rules look identical to the ones used in Linear Regression:

$$\frac{\partial J}{\partial w_j} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})x_j^{(i)}$$

$$\frac{\partial J}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})$$

**Note:** The formulas are the same, but the definition of $\hat{y}$ is different (it is now a Sigmoid function output, not a linear one).

## 4. Regularized Log Loss

To prevent overfitting in classification, we add the L2 penalty term to the cost function:

$$J(\vec{w},b) = -\frac{1}{m} \sum_{i=1}^{m} \left[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \right] + \frac{\lambda}{2m} \sum_{j=1}^{n} w_j^2$$

The derivative for the regularized weight $w_j$ becomes:

$$\frac{\partial J}{\partial w_j} = \left[ \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})x_j^{(i)} \right] + \frac{\lambda}{m}w_j$$
