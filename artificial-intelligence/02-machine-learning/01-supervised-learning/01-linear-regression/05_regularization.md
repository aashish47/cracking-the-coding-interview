# 05 Regularized Linear Regression

## 1. The Regularized Cost Function

To implement regularization, we modify the original Mean Squared Error (MSE) cost function by adding a penalty term based on the magnitude of the weights $\vec{w}$.

$$J(\vec{w},b) = \frac{1}{2m} \left[ \sum_{i=1}^{m} (f_{\vec{w},b}(\vec{x}^{(i)}) - y^{(i)})^2 + \lambda \sum_{j=1}^{n} w_j^2 \right]$$

### Component Breakdown:

- **$\lambda$ (Lambda):** The **Regularization Parameter**. It controls the trade-off between fitting the data and keeping the weights small.
- **$\sum_{j=1}^{n} w_j^2$:** The L2 penalty term (Ridge). Note that we typically **do not** regularize the bias ($b$).
- **$\frac{1}{2m}$:** Applied to the penalty term as well to keep the scaling consistent with the MSE.

## 2. Gradient Descent with Regularization

Because the cost function has changed, the update rules for the weights $w_j$ must also be adjusted. The update for the bias $b$ remains the same.

### The New Update Rule for $w_j$:

For each weight $j$ from $1$ to $n$:

$$w_j := w_j - \alpha \left[ \frac{1}{m} \sum_{i=1}^{m} (f_{\vec{w},b}(\vec{x}^{(i)}) - y^{(i)})x_j^{(i)} + \frac{\lambda}{m}w_j \right]$$

### Weight Decay Interpretation:

If we rearrange the terms, the update rule can be seen as:

$$w_j := w_j(1 - \alpha\frac{\lambda}{m}) - \alpha \frac{1}{m} \sum_{i=1}^{m} (\text{Error})x_j^{(i)}$$

Since $(1 - \alpha\frac{\lambda}{m})$ is slightly less than 1, the weight "decays" or shrinks toward zero in every iteration before the standard gradient update is applied.
