# 01 Introduction to Logistic Regression

Despite its name, **Logistic Regression** is a fundamental **classification** algorithm, not a regression algorithm. It is used to predict the probability that an instance belongs to a particular category (usually binary, such as "Yes/No" or "Spam/Not Spam").

---

## 1. Regression vs. Classification

In Linear Regression, the output $\hat{y}$ can be any real number from $-\infty$ to $+\infty$. In classification, we need the output to be a probability between **0 and 1**.

- **Linear Regression:** Predicts continuous values (e.g., Price = $350,000).
- **Logistic Regression:** Predicts the probability of a class (e.g., Probability of Cancer = 0.85).

---

## 2. The Model Equation

Logistic regression applies a mapping function to the linear combination of inputs. It starts with the same linear base we used in linear regression:

$$z = \vec{w} \cdot \vec{x} + b$$

We then pass this value $z$ (often called the **logit**) through a specialized function (the Sigmoid function, covered in 02) to squash the output into the range $[0, 1]$.

$$\hat{y} = g(z)$$

---

## 3. Core Concept: Binary Classification

In the standard version of this model, we deal with two classes:

- **Negative Class (0):** The absence of a condition (e.g., "Not Spam").
- **Positive Class (1):** The presence of a condition (e.g., "Spam").

The output $\hat{y}$ is interpreted as $P(y=1 | x; w, b)$, which is the probability that $y$ is 1, given the input $x$ and parameters $w, b$.

---

## 4. Why not use Linear Regression for Classification?

1. **Outliers:** Linear regression is highly sensitive to outliers, which can shift the best-fit line and drastically change the classification threshold.
2. **Invalid Probabilities:** Linear regression can predict values like 1.5 or -0.2, which make no sense as probabilities.
3. **Nature of Data:** Classification labels are discrete (0 or 1), while linear regression assumes a continuous target.

---

**Next Step:**
Would you like to move to **02: Sigmoid Function** to see the math behind squashing that linear output into a probability?
