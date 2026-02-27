# 02 Splitting Criteria

The goal of a Decision Tree is to make the "leaves" as pure as possible. A node is considered **pure** if all data points in that node belong to the same class. To achieve this, the tree uses mathematical criteria to evaluate potential splits and choose the best feature.

## 1. Entropy

Entropy is a measure of disorder or uncertainty in a dataset. In the context of classification, it measures the "impurity" of a node.

### The Equation

$$H(S) = -\sum_{i=1}^{c} p_i \log_2(p_i)$$

- **$H(S)$**: The entropy of the set $S$. The $H$ stands for "uncertainty." If $H(S) = 0$, you have zero uncertainty (perfectly pure).
- **$c$**: The number of classes (e.g., for binary classification, $c=2$).
- **$p_i$**: The **probability** (or proportion) of finding an item of class $i$ in that node.
- **$\log_2(p_i)$**: Log base 2 is used because entropy is measured in "bits."
- **The Negative Sign ($-$)**: Since $p_i$ is a fraction, the log is negative; the sign ensures entropy is a positive value.

## 2. Information Gain

Information Gain is the reduction in entropy achieved by splitting the data on a specific feature ($A$). The tree chooses the feature that maximizes this value.

### The Equation

$$IG(S, A) = H(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} H(S_v)$$

- **$IG(S, A)$**: The "Gain" in information from the split.
- **$H(S)$**: The **Parent Entropy** before the split.
- **$v$**: A specific value of feature $A$ (e.g., if Feature A is "Color," $v$ could be "Red").
- **$\frac{|S_v|}{|S|}$**: The **Weight** of the child node (ratio of child samples to parent samples).
- **$H(S_v)$**: The **Child Entropy**—the disorder remaining in each subset after the split.

## 3. Gini Impurity

Gini Impurity is an alternative used by the CART algorithm. It measures the probability of a random element being incorrectly classified.

### The Equation

$$Gini = 1 - \sum_{i=1}^{c} (p_i)^2$$

- **$(p_i)^2$**: The probability of picking two items of the same class from the node.
- **$1 - \dots$**: By subtracting from 1, we find the likelihood of **inconsistency** (impurity).
- **Why use Gini?** It is computationally faster than Entropy because it doesn't involve logarithmic calculations. The results are usually very similar to Entropy.

## 4. Summary Table

| Criteria    | Range    | Calculation | Advantage                           |
| ----------- | -------- | ----------- | ----------------------------------- |
| **Entropy** | 0 to 1   | Logarithmic | Slower but mathematically rigorous. |
| **Gini**    | 0 to 0.5 | Squared     | Faster; avoids complex log math.    |
