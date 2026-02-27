# 2. Convolutional Layers: The Feature Extractors

The **Convolutional Layer** is the core building block of the network. It replaces the "global" view of a Dense layer with a "local" scanning mechanism.

## 1. The Kernel (Filter) & The Operation

A **Kernel** is a small matrix of learnable weights (typically $3 \times 3$ or $5 \times 5$).

**The Convolution Operation:**
The kernel slides (convolves) over the input. At each position, it performs an **element-wise multiplication** between the kernel weights and the pixel values, then **sums** the results into a single scalar.

$$y = \sum_{i=1}^{k} \sum_{j=1}^{k} (I_{i,j} \cdot K_{i,j}) + b$$

- $I$: Input patch
- $K$: Kernel matrix
- $b$: Bias term
- $y$: Single output pixel in the Feature Map

---

## 2. Feature Maps (Activation Maps)

The output of this sliding process is a **Feature Map**.

- **High Values:** Indicate the filter "found" its target (e.g., a vertical edge).
- **Low Values:** Indicate the absence of that specific pattern.
- **Non-Linearity:** Usually, a **ReLU** (Rectified Linear Unit) activation function is applied immediately after convolution to discard negative values: $f(x) = \max(0, x)$.

---

## 3. Key Hyperparameters

These settings determine the dimensions of the output feature map.

### A. Stride ($S$)

The "step size" of the filter.

- **Stride 1:** Moves 1 pixel at a time. Preserves maximum spatial info.
- **Stride 2+:** Skips pixels. This performs **downsampling**, reducing the computational load and the size of the next layer.

### B. Padding ($P$)

Filters naturally shrink the input because the center of the filter cannot go past the edge of the image.

- **Valid Padding:** $P=0$. The output is smaller than the input.
- **Same Padding:** We surround the image with a border of zeros so that $Output \text{ } Size = Input \text{ } Size$.

> **The General Formula for Output Size:**
> For an input of size $W$, kernel size $K$, padding $P$, and stride $S$:
>
> $$O = \frac{W - K + 2P}{S} + 1$$

## 4. Depth and Volume

In a real CNN layer, we don't use one filter; we use a **bank of filters** (e.g., 32, 64, or 128).

- **Input:** $(H, W, 3)$
- **Operation:** Each of the 64 filters produces its own 2D feature map.
- **Output:** The maps are stacked to create a volume with a **Depth** of 64.

## 5. Feature Hierarchy

One thing to add to your notes is **Representation Learning**. CNNs learn features in a hierarchical "pyramid":

1. **Layer 1 (Low-level):** Detects edges, dots, and color gradients.
2. **Layer 2 (Mid-level):** Combines edges into textures, circles, or corners.
3. **Layer 3+ (High-level):** Combines shapes into complex motifs (eyes, tires, honeycombs).
4. **Final Layers:** Recognize entire objects (faces, cars, dogs).

## 6. Parameters vs. Hyperparameters

| Term            | Category       | Description                                                     |
| --------------- | -------------- | --------------------------------------------------------------- |
| **Weights**     | Parameter      | The actual numbers inside the kernel (learned during training). |
| **Kernel Size** | Hyperparameter | The dimensions of the filter (e.g., $3 \times 3$).              |
| **Stride**      | Hyperparameter | How many pixels the filter jumps.                               |
| **Padding**     | Hyperparameter | Extra border added to the input.                                |
