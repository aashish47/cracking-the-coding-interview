# 02 Random Forest

A **Random Forest** is an ensemble of many Decision Trees, built using the **Bagging** (Bootstrap Aggregating) method. It is one of the most robust and widely used algorithms because it effectively handles the overfitting problem inherent in single trees.

## 1. How it Works: The Two Levels of "Randomness"

To ensure the trees in the forest are diverse and uncorrelated, Random Forest introduces randomness in two ways:

- **Bootstrapping (Row Randomness):** Each tree is trained on a random sample of the data, selected with replacement. This means some rows may be repeated, and some may be left out entirely (called "Out-of-Bag" data).
- **Feature Randomness (Column Randomness):** At every split point in a tree, the algorithm only considers a **random subset of features** (usually $\sqrt{n}$ for classification) rather than all available features. This prevents a single dominant feature from making all the trees look identical.

## 2. The Aggregation Step

Once all the trees ($T_1, T_2, \dots, T_n$) are trained, the forest makes a prediction:

- **Classification:** The forest takes a **Majority Vote**. If 70 trees say "Spam" and 30 say "Not Spam," the final answer is "Spam."
- **Regression:** The forest calculates the **Average** of the predictions from all individual trees.

## 3. Key Advantages

- **Reduced Overfitting:** While individual trees have high variance, the averaging process of the forest cancels out errors, leading to low variance.
- **Out-of-Bag (OOB) Error:** Since each tree only sees a portion of the data, the "leftover" data can be used to test the model's accuracy during training, often removing the need for a separate validation set.
- **Feature Importance:** It provides a clear ranking of which features are most useful for making predictions.

## 4. Hyperparameters to Watch

- **n_estimators:** The number of trees in the forest. More trees generally improve performance but increase computation time.
- **max_features:** The size of the random subset of features allowed at each split.
- **bootstrap:** Whether to use bootstrap samples (usually True).

| Feature              | Single Decision Tree | Random Forest                      |
| -------------------- | -------------------- | ---------------------------------- |
| **Complexity**       | Low                  | High                               |
| **Overfitting Risk** | High                 | Low                                |
| **Interpretability** | Easy to visualize    | Hard (a "Black Box" of 100+ trees) |
| **Performance**      | Moderate             | High                               |
