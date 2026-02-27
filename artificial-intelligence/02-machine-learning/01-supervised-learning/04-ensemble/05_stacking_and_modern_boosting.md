# 05 Stacking and Modern Boosting

While Random Forest and XGBoost are powerful, advanced machine learning often requires combining entirely different types of models or using specialized boosting frameworks for speed and categorical data.

## 1. Stacking (Stacked Generalization)

Stacking is a "Meta-Ensemble" technique. Unlike Bagging or Boosting, which use the same algorithm (e.g., all Decision Trees), Stacking combines **diverse** models.

### How it Works:

1. **Base Models (Level 0):** You train several different models independently (e.g., a KNN, a Support Vector Machine, and a Random Forest).
2. **Predictions as Features:** Each base model makes a prediction on the dataset.
3. **Meta-Model (Level 1):** You use the predictions from Step 2 as **input features** for a final model (often a simple Logistic Regression). The Meta-Model learns which base model is most reliable for specific data patterns.

## 2. Voting Classifiers

The simplest way to ensemble. It’s like a committee making a decision.

- **Hard Voting:** Majority wins. If you have 3 models and 2 say "Yes," the final answer is "Yes."
- **Soft Voting:** Sums the predicted probabilities. If Model A is 90% sure it’s "Yes" but Model B and C are only 51% sure it’s "No," the high confidence of Model A might carry the "Yes" vote.

## 3. LightGBM (Light Gradient Boosting Machine)

Developed by Microsoft, LightGBM is the "speed king" of boosting.

- **Leaf-wise Growth:** Traditional GBDT (like XGBoost) grows trees level-by-level. LightGBM grows trees **leaf-wise**, choosing the leaf that reduces the most loss. This leads to much faster convergence.
- **GOSS (Gradient-based One-Side Sampling):** It keeps data points with large gradients (hard cases) and randomly samples from data points with small gradients, drastically reducing computation time without losing much accuracy.

## 4. CatBoost (Categorical Boosting)

Developed by Yandex, this algorithm is the best for datasets with many "strings" or categories (e.g., City Names, Device Types).

- **Native Categorical Handling:** Unlike other models that require "One-Hot Encoding" (turning categories into 0s and 1s), CatBoost handles them internally using a technique called **Ordered Boosting**.
- **Reduced Overfitting:** It uses a unique symmetric tree structure that makes it very robust and less likely to overfit than XGBoost or LightGBM on smaller datasets.

## 5. Summary Table: The Boosting Titans

| Feature             | XGBoost          | LightGBM       | CatBoost             |
| ------------------- | ---------------- | -------------- | -------------------- |
| **Growth Strategy** | Level-wise       | Leaf-wise      | Symmetric            |
| **Speed**           | Fast             | **Fastest**    | Moderate             |
| **Best For**        | General Purpose  | Large Datasets | Categorical Data     |
| **Key Advantage**   | Stability/Proven | Efficiency/RAM | Accuracy/Ease of use |
