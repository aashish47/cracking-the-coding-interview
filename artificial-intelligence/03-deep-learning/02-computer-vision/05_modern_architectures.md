# 05 Modern Architectures

To push past the limits of VGG, researchers had to find ways to train networks with hundreds of layers without the gradients disappearing. This led to the creation of the most powerful architectures used in industry today.

## 1. Inception / GoogLeNet — 2014

Developed by Google, this architecture focused on **computational efficiency**. Instead of choosing between a $3 \times 3$ filter or a $5 \times 5$ filter, it does both.

- **Inception Modules:** Within a single layer, it runs multiple convolutions ($1 \times 1, 3 \times 3, 5 \times 5$) and a pooling operation in parallel, then concatenates the results.
- **1x1 Convolutions:** It uses "bottleneck" layers ($1 \times 1$ filters) to reduce the number of channels before doing expensive $3 \times 3$ or $5 \times 5$ math. This keeps the model fast and small.

## 2. ResNet (Residual Networks) — 2015

Introduced by Microsoft, ResNet is arguably the most important architecture in modern Computer Vision. It allows for networks to be hundreds or even thousands of layers deep.

- **Skip Connections (Residual Blocks):** Instead of forcing every layer to learn a brand-new representation, ResNet uses "identity shortcuts." It passes the input $x$ directly to the output of a layer further down the chain.
- **The Logic:** The layer now only has to learn the _residual_ (the difference) between the input and output: $y = F(x) + x$. This effectively solves the **Vanishing Gradient** problem.
- **Impact:** ResNet-50 and ResNet-101 are the industry standard "backbones" for almost all vision tasks.

## 3. MobileNet — 2017

While ResNet and Inception are powerful, they are often too heavy for smartphones or IoT devices.

- **Depthwise Separable Convolutions:** MobileNet breaks a standard convolution into two smaller steps:

1. **Depthwise:** One filter per input channel (spatial filtering).
2. **Pointwise:** A $1 \times 1$ convolution (combining channels).

- **The Result:** It achieves near-ResNet accuracy but with roughly **10x fewer parameters** and much lower battery consumption.

## 4. EfficientNet — 2019

Created by Google Research using Neural Architecture Search (AI designing AI).

- **Compound Scaling:** Most models are scaled up by just making them deeper. EfficientNet scales **depth**, **width**, and **resolution** simultaneously and in balance.
- **Impact:** It is currently one of the most accurate and efficient models available for image classification.

## 5. Vision Transformers (ViT) — 2021

Strictly speaking, this is **not** a CNN, but it is the current state-of-the-art for large-scale vision.

- **Self-Attention:** Instead of sliding a window (convolution), it breaks an image into "patches" and uses an attention mechanism to see how every patch relates to every other patch.
- **Impact:** While CNNs are better for small/medium datasets, ViTs are superior when you have millions of images because they understand "global" context better.

## 6. ConvNeXt — 2022

A modern "pure" CNN developed by Meta (Facebook) to compete with Vision Transformers.

- **"Transformerized" CNN:** It borrows design choices from Transformers (like larger $7 \times 7$ kernels and fewer activation layers) but keeps the efficiency of a CNN.
- **Impact:** It proved that CNNs can still outperform Transformers in many scenarios if designed with modern techniques.

---

## 7. Summary Table (Chronological)

| Architecture     | Year | Key Innovation         | Best Use Case                     |
| ---------------- | ---- | ---------------------- | --------------------------------- |
| **Inception**    | 2014 | Parallel Filters       | Efficiency & Multi-scale features |
| **ResNet**       | 2015 | Skip Connections       | General purpose "Backbone"        |
| **MobileNet**    | 2017 | Separable Convolutions | Mobile/Edge devices               |
| **EfficientNet** | 2019 | Compound Scaling       | State-of-the-Art accuracy         |
| **ViT**          | 2021 | Self-Attention         | Large-scale "Big Data" vision     |
| **ConvNeXt**     | 2022 | Modernized CNN         | High-performance pure CNN         |
