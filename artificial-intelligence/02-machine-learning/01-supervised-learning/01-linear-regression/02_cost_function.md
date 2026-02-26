# 02 Cost Function

The **Cost Function** is the mathematical formula used to measure how "wrong" the model's predictions are. It quantifies the error between the predicted values ($\hat{y}$) and the actual target values ($y$).

## 1. Defining the Error (Residual)

For any single data point, the error is the vertical distance between the actual data point and the regression line.

$$Error = \hat{y}^{(i)} - y^{(i)}$$

- **$\hat{y}^{(i)}$**: The value predicted by the model for the $i^{th}$ observation.
- **$y^{(i)}$**: The actual value from the dataset.

## 2. Mean Squared Error (MSE)

The most common cost function for linear regression is **Mean Squared Error (MSE)**, often denoted as $J(w, b)$. We square the errors to ensure they are all positive and to penalize larger errors more heavily.

$$J(w, b) = \frac{1}{2m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})^2$$

### Breakdown of the Formula:

- **$m$**: The total number of training examples.
- **$\sum$ (Sigma)**: Summation of the squared errors for all data points from $i=1$ to $m$.
- **$\frac{1}{2m}$**: We divide by $m$ to get the average error. The $2$ in the denominator is a mathematical convenience that cancels out during calculus (differentiation) later.

## 3. Visualizing the Cost Function

If we plot the cost $J$ against different values of $w$ and $b$, the resulting shape is a **convex bowl** (a parabola in 2D).

- **High Cost:** The values of $w$ and $b$ result in a line that is far from the data points.
- **Minimum Cost:** The bottom of the bowl represents the "Global Minimum," where $w$ and $b$ produce the best-fit line.

## 4. Goal of the Cost Function

| Concept              | Description                                                                           |
| -------------------- | ------------------------------------------------------------------------------------- |
| **Objective**        | Minimize $J(w, b)$.                                                                   |
| **Ideal Scenario**   | $J(w, b) = 0$ (The line passes through every data point perfectly).                   |
| **Role in Training** | It provides a single number that tells the model how well it is currently performing. |
