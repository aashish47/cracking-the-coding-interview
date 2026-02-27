# 01 Introduction to Decision Trees

A **Decision Tree** is a non-parametric supervised learning algorithm used for both classification and regression. It mimics human decision-making by using a flowchart-like structure to break down a complex dataset into smaller, more manageable subsets.

## 1. Structure of a Decision Tree

The tree consists of nodes and edges, organized hierarchically:

- **Root Node:** The very top node representing the entire dataset. It is the first split.
- **Internal (Decision) Nodes:** Points where the data is split based on a specific feature or attribute.
- **Branches:** The outcome of a decision, connecting nodes.
- **Leaf Nodes:** The terminal nodes that represent a final class label or a continuous value. These nodes do not split further.

## 2. The Logic: Recursive Binary Splitting

Decision trees use a "top-down, greedy" approach.

- **Top-down:** Starts at the root and moves down.
- **Greedy:** At each node, it chooses the split that results in the greatest immediate improvement in purity, without looking ahead to see if a different split would be better later.

## 3. Advantages of Decision Trees

- **Interpretability:** They are easy to visualize and explain to non-technical stakeholders.
- **No Scaling Required:** Unlike Linear Regression or Neural Networks, Decision Trees do not require feature scaling (normalization/standardization).
- **Handles Non-linearity:** They naturally capture non-linear relationships between features.

## 4. The Main Weakness: Overfitting

Decision trees are highly prone to **overfitting**. A tree can grow deep enough to essentially "memorize" the training data, creating a rule for every single data point. This results in high variance—the model performs perfectly on training data but fails on new, unseen data.
