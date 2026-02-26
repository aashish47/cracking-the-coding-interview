# 05 Data Splitting

## 1. Train-Test Split

- **Training Set (70-80%):** Used to learn the parameters (weights).
- **Test Set (20-30%):** Used to evaluate performance on unseen data.

## 2. Train-Validation-Test Split

- **Validation Set:** Used to tune hyperparameters during training to prevent overfitting on the test set.
- **Flow:** Train on Training Set -> Tune on Validation Set -> Final check on Test Set.

## 3. Cross-Validation (K-Fold)

- **Process:** Split data into $K$ folds. Train on $K-1$, validate on 1. Repeat $K$ times.
- **Pros:** More reliable estimate of performance; uses all data for training.
- **Cons:** Computationally expensive.

## 4. Best Practices

- **Random State:** Always set a `random_seed` or `random_state` to ensure the split is reproducible.
- **Stratification:** When dealing with imbalanced datasets (e.g., 90% "No", 10% "Yes"), use **Stratified Splitting**.
    - **Goal:** Ensures the Training and Test sets have the same proportion of class labels as the original dataset.
    - **Why:** Prevents a scenario where the Test set contains no examples of a minority class.
- **Shuffle:** Data should be shuffled before splitting to remove any bias from the order in which data was collected (e.g., time-series data should be handled differently).
