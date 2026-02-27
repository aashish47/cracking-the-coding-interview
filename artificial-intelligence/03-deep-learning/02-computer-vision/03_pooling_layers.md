# 03 Pooling Layers

After a Convolutional layer finds features, we often have "too much" data. **Pooling layers** are used to reduce the spatial size of the representation, which cuts down on the number of parameters and computation in the network.

## 1. Why use Pooling

- **Dimensionality Reduction:** It shrinks the height $H$ and width $W$ of the feature maps, reducing the computational "footprint" of the next layer.
- **Invariance:** It provides **Translational Invariance**. If a feature (like a "cat ear") shifts by a few pixels, the pooling operation still captures the same maximum activation in that region.
- **Prevents Overfitting:** By summarizing the data, the model learns the "essence" of a feature rather than memorizing its exact pixel-perfect location.

## 2. Max Pooling

This is the most common type of pooling. You define a window size (usually $2 \times 2$) and a stride (usually $2$).

- **Operation:** Within the $2 \times 2$ window, you only keep the **maximum value** and discard the rest.
- **Mathematical Logic:** $y = \max(x_{1}, x_{2}, \dots, x_{n})$.
- **Philosophy:** High values represent the "strength" of a detected feature. We only care _if_ a feature was found in that patch, not its microscopic coordinate within that $2 \times 2$ square.

## 3. Average Pooling

Instead of taking the maximum value, you calculate the **arithmetic mean** of all values in the window.

- **Operation:** $y = \frac{1}{n} \sum_{i=1}^{n} x_i$.
- **Usage:** It is used less frequently in hidden layers because it "smooths out" features, potentially washing out the strongest signals.
- **Modern Note:** **Global Average Pooling (GAP)** is often used at the very end of a network to replace dense layers, reducing each feature map to a single average value.

## 4. Pooling Hyperparameters

Pooling layers typically do **not** have learnable weights (no parameters), but they do have hyperparameters:

- **Window Size ($K$):** Usually $2 \times 2$.
- **Stride ($S$):** Usually $2$. This ensures the window doesn't overlap and effectively **halves** the dimensions.
- **Output Dimension Formula:** The same formula from Convolution applies, though padding is rarely used ($P=0$):

$$O = \frac{W - K}{S} + 1$$

_Example:_ A $10 \times 10$ map with $2 \times 2$ pooling and Stride $2$ becomes $5 \times 5$.

## 5. The Result of the "Conv-Pool" Sandwich

A standard CNN architecture often repeats a pattern: **Convolution -> Activation (ReLU) -> Pooling**.

1. **Conv:** Extracts local features (Detectors).
2. **ReLU:** Increases non-linearity, allowing the model to learn complex patterns.
3. **Pool:** Compresses the maps and provides spatial robustness.

> **Pro-Tip: Why Max over Average?**
> In computer vision, we usually care about the **presence** of a feature. Max Pooling acts like a "Signal Booster"—it picks the loudest signal in the room. Average Pooling acts like a "Volume Leveler"—it takes the average noise, which can make a sharp feature look blurry to the next layer.
