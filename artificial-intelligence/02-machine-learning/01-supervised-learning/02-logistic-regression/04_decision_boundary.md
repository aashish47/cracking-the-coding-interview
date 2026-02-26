# 04 Decision Boundary

A **Decision Boundary** is the line (or surface) that separates different classes in a classification problem. While the logistic regression model outputs a probability, the decision boundary is what we use to make a final discrete prediction.

## 1. The Prediction Rule

By default, we classify an input into the positive class (1) if the predicted probability $\hat{y}$ is greater than or equal to 0.5.

- **Predict $y = 1$:** if $\hat{y} \geq 0.5$
- **Predict $y = 0$:** if $\hat{y} < 0.5$

## 2. Relation to the Linear Equation ($z$)

Recall that $\hat{y} = g(z)$, where $g$ is the Sigmoid function. The property of the Sigmoid function is that $g(z) \geq 0.5$ whenever $z \geq 0$.

Therefore, the decision is actually determined by the linear part of the model:

- **Predict $y = 1$:** if $\vec{w} \cdot \vec{x} + b \geq 0$
- **Predict $y = 0$:** if $\vec{w} \cdot \vec{x} + b < 0$

The equation $\vec{w} \cdot \vec{x} + b = 0$ represents the **Decision Boundary** itself.

## 3. Linear vs. Non-Linear Boundaries

The shape of the boundary depends on the features included in the model:

- **Linear Boundary:** Created using original features (e.g., $z = w_1x_1 + w_2x_2 + b$). This results in a straight line in 2D or a flat plane in 3D.
- **Non-Linear Boundary:** Created using **Polynomial Features** (e.g., $z = w_1x_1^2 + w_2x_2^2 + b$). This allows the model to create circles, ellipses, or complex curves to separate data that is not linearly separable.

## 4. Adjusting the Threshold

While 0.5 is the standard threshold, it is not set in stone. We can adjust the threshold depending on the cost of different types of errors:

- **Higher Threshold (e.g., 0.8):** Use this if you want to be very certain before predicting "Positive" (e.g., classifying a high-risk surgery).
- **Lower Threshold (e.g., 0.2):** Use this if you want to catch as many "Positive" cases as possible, even if you get some false alarms (e.g., screening for a rare disease).
