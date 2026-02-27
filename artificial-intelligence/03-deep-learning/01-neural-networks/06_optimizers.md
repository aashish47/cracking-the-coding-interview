# 06 Optimizers

While Gradient Descent is the foundation of learning, using the basic version (Vanilla SGD) on a complex, high-dimensional loss surface is often too slow or gets stuck. **Optimizers** are algorithms that refine the weight update rule to speed up convergence and find better minima.

## 1. The Challenges of Standard Gradient Descent

Standard Stochastic Gradient Descent (SGD) faces several hurdles:

- **Local Minima & Saddle Points:** The model can get stuck in "valleys" that aren't the lowest point.
- **Oscillations:** If the learning rate is too high, the updates might "zig-zag" across a narrow valley instead of following it down.
- **One-Size-Fits-All Learning Rate:** It applies the same learning rate to every single weight, even though some weights might need to change faster than others.

## 2. Momentum: The "Rolling Ball"

**Momentum** mimics physics. Imagine a ball rolling down a hill; it accumulates speed (velocity) as it continues in the same direction.

- **Logic:** It keeps a running average of the previous gradients. If the current gradient points in the same direction as the previous ones, the update gets bigger.
- **Benefit:** It helps "dampen" oscillations and allows the model to push through small local plateaus.

## 3. Adaptive Optimizers

Instead of a fixed learning rate, these algorithms adjust the learning rate for each weight individually.

### A. AdaGrad (Adaptive Gradient)

- **How it works:** It scales the learning rate inversely to the sum of the squares of all historical gradients.
- **Benefit:** Weights that receive infrequent updates get a higher learning rate, while frequently updated weights get a lower one.
- **Drawback:** The learning rate eventually shrinks to zero, and the model stops learning.

### B. RMSProp (Root Mean Square Propagation)

- **How it works:** Similar to AdaGrad, but it uses an **exponential moving average** of the squared gradients.
- **Benefit:** It prevents the learning rate from dropping to zero, allowing the model to continue learning indefinitely.

## 4. Adam (Adaptive Moment Estimation)

**Adam** is the "Gold Standard" optimizer for most Deep Learning tasks. It combines the best of both worlds: **Momentum** (speed) and **RMSProp** (adaptive learning rates).

- **First Moment:** Estimates the mean of the gradients (like Momentum).
- **Second Moment:** Estimates the uncentered variance of the gradients (like RMSProp).
- **Why use it?** It is computationally efficient, requires little memory, and usually works very well with default hyperparameters (like a learning rate of $0.001$).

## 5. Summary Table

| Optimizer    | Main Concept                 | Best For                                  |
| ------------ | ---------------------------- | ----------------------------------------- |
| **SGD**      | Basic descent.               | Simple models, very large batches.        |
| **Momentum** | Speed and direction history. | Speeding up SGD.                          |
| **RMSProp**  | Adaptive learning rate.      | Recurrent Neural Networks (RNNs).         |
| **Adam**     | Momentum + Adaptive Rate.    | **Default choice** for almost everything. |

## 6. Learning Rate Schedulers

Even with a good optimizer, you might want to change the learning rate over time.

- **Step Decay:** Reduce the learning rate by half every 10 epochs.
- **Cosine Annealing:** Slowly decrease the learning rate following a cosine curve.
- **Warm-up:** Start with a very small rate and slowly increase it before beginning the decay.
