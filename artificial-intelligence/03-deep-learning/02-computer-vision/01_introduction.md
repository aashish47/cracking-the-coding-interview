# 01 Computer Vision

## 1. Image Representation as Data

To a computer, an image is not a "picture"—it is a **3D Tensor** (a multi-dimensional array of numerical values).

### A. The Digital Anatomy of a Pixel

- **Grid Structure:** An image is a spatial grid of pixels.
- **Intensity Values:** In a standard 8-bit image, each pixel value ranges from **0 to 255**.
- `0`: Absolute Black (No intensity)
- `255`: Absolute White (Full intensity)

- **Resolution:** Defined by $Height \times Width$.

### B. Color Channels (The RGB Model)

Color images are represented by three stacked 2D matrices, one for each primary color:

- **Red, Green, and Blue (RGB)**.
- **Tensor Shape:** $(H, W, C)$ where $C$ is the number of channels.
- _Grayscale:_ $C = 1$
- _Color (RGB):_ $C = 3$

## 2. Why Artificial Neural Networks (ANNs) Fail

Standard "Dense" or Fully Connected (FC) layers are mathematically ill-suited for computer vision for two primary reasons:

### A. The Parameter Explosion

In a Dense layer, every input pixel is connected to every neuron in the hidden layer.

- **Example:** A modest $200 \times 200$ RGB image.
- Input features: $200 \times 200 \times 3 = 120,000$
- If the first hidden layer has **1,000 neurons**:
- Total weights: $120,000 \times 1,000 = 120,000,000$ (**120 Million Parameters**).

- **Result:** High risk of overfitting and massive computational cost.

### B. Destruction of Spatial Topology

Dense layers require "Flattening"—converting a 2D/3D grid into a 1D vector.

- **The Issue:** Pixels have **spatial correlation** (the pixels making up an eye are only meaningful if they are near each other).
- **The Loss:** Flattening treats a pixel at $(0,0)$ and its neighbor at $(0,1)$ as if they have no more relationship than two pixels on opposite corners of the image.

## 3. The CNN Solution: Structural Advantages

Convolutional Neural Networks (CNNs) solve the ANN flaws by introducing three key concepts:

### A. Local Receptive Fields

Instead of looking at the whole image at once, CNNs use small "filters" (kernels) that look at small patches of pixels at a time. This preserves the local relationship between pixels.

### B. Translation Invariance

A feature (like a vertical edge or a circle) should be recognizable regardless of its location in the frame. CNNs achieve this by sliding the same filter across the entire image.

### C. Weight Sharing

Unlike Dense layers where every connection has a unique weight, a CNN filter uses the **same weights** across the whole image.

- **Efficiency Gain:** A $3 \times 3$ filter only has 9 weights (plus 1 bias), regardless of how large the image is.
