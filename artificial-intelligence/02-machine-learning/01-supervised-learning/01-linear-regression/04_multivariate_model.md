# 04 Multivariate Model

Multivariate Linear Regression generalizes the univariate model by incorporating multiple independent variables ($x_1, x_2, ..., x_n$) to predict a single target value. This allows the model to account for several factors simultaneously (e.g., predicting house price based on size, age, and number of rooms).

## 1. The Model Equation

The multivariate model expresses the prediction $\hat{y}$ as a weighted sum of all input features plus a bias term.

$$\hat{y} = w_1x_1 + w_2x_2 + w_3x_3 + ... + w_nx_n + b$$

### Component Breakdown:

- **$x_j$ (Features):** The different input variables (e.g., $x_1$ = sq ft, $x_2$ = age).
- **$w_j$ (Weights):** The parameters representing the influence of each feature. A higher $|w_j|$ indicates the feature $x_j$ has a stronger impact on the prediction.
- **$b$ (Bias):** The constant offset, representing the value of $\hat{y}$ when all features $x$ are zero.

## 2. Vectorization: The Professional Notation

In practice, we use **Vectorization** to represent the equation compactly. This allows us to use linear algebra for efficient computation.

$$\hat{y} = \vec{w} \cdot \vec{x} + b$$

- **$\vec{w}$ (Weight Vector):** A row vector $[w_1, w_2, ..., w_n]$.
- **$\vec{x}$ (Feature Vector):** A column vector $[x_1, x_2, ..., x_n]^T$.
- **$\cdot$ (Dot Product):** The operation that multiplies corresponding elements and sums them up.

## 3. Gradient Descent for Multiple Features

The optimization process updates every weight $w_j$ in the vector $\vec{w}$ simultaneously in each iteration.

### The General Update Rule

For each feature $j$ from $1$ to $n$:

$$w_j := w_j - \alpha \frac{\partial J(\vec{w},b)}{\partial w_j}$$

$$b := b - \alpha \frac{\partial J(\vec{w},b)}{\partial b}$$

### The Partial Derivatives

Using the $\frac{1}{2m}$ cost convention, the gradients for $n$ features are:

**1. Gradient for any Weight ($w_j$):**

$$\frac{\partial J(\vec{w}, b)}{\partial w_j} = \frac{1}{m} \sum_{i=1}^{m} (\vec{w} \cdot \vec{x}^{(i)} + b - y^{(i)})x_j^{(i)}$$

**2. Gradient for the Bias ($b$):**

$$\frac{\partial J(\vec{w}, b)}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} (\vec{w} \cdot \vec{x}^{(i)} + b - y^{(i)})$$

## 4. Key Differences from Univariate

| Feature        | Univariate    | Multivariate                 |
| -------------- | ------------- | ---------------------------- |
| **Input**      | Single $x$    | Vector $\vec{x}$             |
| **Parameters** | Scalar $w, b$ | Vector $\vec{w}$, Scalar $b$ |
| **Geometry**   | 2D Line       | Multi-dimensional Hyperplane |
