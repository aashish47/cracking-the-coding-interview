# 07 Regularization

Neural networks are high-performance machines that easily "overheat" (overfit) or "stall" (unstable gradients). These techniques act as the cooling and suspension systems to keep the model on track.

## 1. Preventing Overfitting (Regularization)

Overfitting happens when the model memorizes the training data. These tools force the model to stay "simple."

### A. Weight Decay (L1 & L2)

We add a penalty to the loss function based on the magnitude of the weights.

- **L2 (Ridge):** Adds $\lambda \sum w^2$. It shrinks weights toward zero but never makes them zero. It keeps the model "balanced."
- **L1 (Lasso):** Adds $\lambda \sum |w|$. It can push weights to **exactly zero**, effectively acting as a feature selector.

### B. Dropout

The most popular deep learning regularization.

- **Mechanism:** Randomly "kills" a fraction of neurons during each training step.
- **Why:** It prevents **co-adaptation**. No neuron can rely on a specific neighbor; every neuron must learn a robust feature on its own.
- **Note:** Used only during training, not during testing.

### C. Early Stopping

- **Mechanism:** You monitor the **Validation Loss**. When the training loss keeps dropping but the validation loss starts rising, you stop training.
- **Why:** The point of divergence is where the model stops learning patterns and starts memorizing noise.

## 2. Stabilizing Training (Normalization)

Normalization ensures that the data flowing through the layers has a consistent scale (mean = 0, variance = 1). This prevents gradients from exploding or vanishing.

### A. Batch Normalization (Across the Batch)

- **How:** It calculates the mean and variance for **each feature** across the entire mini-batch.
- **Best For:** CNNs and deep MLPs.
- **Pro:** It allows for higher learning rates and acts as a slight regularizer.
- **Con:** It fails if the batch size is too small (e.g., 2 or 4 samples).

### B. Layer Normalization (Across the Layer)

- **How:** It calculates the mean and variance for **all features** within a **single sample**.
- **Best For:** RNNs and Transformers (NLP).
- **Pro:** Independent of batch size. It works perfectly even if you only process one sentence at a time.

## 3. Summary Comparison Table

| Technique             | Category       | Problem Solved                         | When to Use                    |
| --------------------- | -------------- | -------------------------------------- | ------------------------------ |
| **L2 Regularization** | Regularization | Overfitting                            | Almost always.                 |
| **Dropout**           | Regularization | Overfitting/Co-adaptation              | Deep layers (Fully Connected). |
| **Early Stopping**    | Regularization | Overfitting/Wasted Time                | Always.                        |
| **Batch Norm**        | Normalization  | Slow training/Internal Covariate Shift | **Computer Vision** (CNNs).    |
| **Layer Norm**        | Normalization  | Sequential instability                 | **NLP** (Transformers/RNNs).   |

## 4. When to combine?

In a modern production model, it is very common to see:

- **ReLU** for activation.
- **Adam** for the optimizer.
- **Batch/Layer Norm** for stability.
- **Dropout** and **L2** to prevent overfitting.
