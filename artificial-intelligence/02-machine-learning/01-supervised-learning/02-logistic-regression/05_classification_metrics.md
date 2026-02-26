# 05 Classification Metrics

In classification, **Accuracy** alone is often misleading, especially when dealing with imbalanced datasets (e.g., a disease that only affects 1% of the population). We use a **Confusion Matrix** to break down the model's performance.

## 1. The Confusion Matrix

The Confusion Matrix compares the actual labels ($y$) against the predicted labels ($\hat{y}$).

|               | Predicted: 0 (Negative) | Predicted: 1 (Positive) |
| ------------- | ----------------------- | ----------------------- |
| **Actual: 0** | **True Negative (TN)**  | **False Positive (FP)** |
| **Actual: 1** | **False Negative (FN)** | **True Positive (TP)**  |

- **True Positive (TP):** Correctly predicted positive.
- **True Negative (TN):** Correctly predicted negative.
- **False Positive (FP):** Predicted positive, but actually negative (**Type I Error**).
- **False Negative (FN):** Predicted negative, but actually positive (**Type II Error**).

## 2. Key Metrics Derived from the Matrix

### Accuracy

The proportion of total predictions that were correct.

$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$

### Precision (Quality)

Of all the times the model predicted "Positive," how often was it actually right?

$$Precision = \frac{TP}{TP + FP}$$

_Use Case:_ Reducing False Positives (e.g., Spam filters).

### Recall (Quantity/Sensitivity)

Of all the "Positive" cases that exist, how many did the model catch?

$$Recall = \frac{TP}{TP + FN}$$

_Use Case:_ Reducing False Negatives (e.g., Cancer screening).

### F1-Score

The harmonic mean of Precision and Recall. It provides a single score that balances both metrics.

$$F1 = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}$$

## 3. Precision-Recall Trade-off

As you adjust the **Decision Threshold** (as discussed in 04), Precision and Recall move in opposite directions:

- **Lowering Threshold:** Increases Recall (catches more positives) but decreases Precision (more false alarms).
- **Raising Threshold:** Increases Precision (fewer false alarms) but decreases Recall (misses more actual positives).

## 4. ROC and AUC

- **ROC Curve (Receiver Operating Characteristic):** A plot of the **True Positive Rate** (Recall) vs. the **False Positive Rate** at various threshold settings.
- **AUC (Area Under the Curve):** A single number from 0 to 1 representing the model's ability to distinguish between classes. 1.0 is a perfect model; 0.5 is no better than random guessing.
