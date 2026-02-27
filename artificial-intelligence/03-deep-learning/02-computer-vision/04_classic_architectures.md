# 04 Classic Architectures

Now that we understand the building blocks (Convolution and Pooling), we look at the breakthrough designs that proved CNNs could outperform humans in image recognition.

## 1. LeNet-5 (1998)

Developed by Yann LeCun, this was the first successful CNN. It was designed to recognize handwritten digits for the US Postal Service.

- **Architecture.** It used a simple pattern: `Conv -> Pool -> Conv -> Pool -> Dense`.
- **Impact.** It proved that machines could learn features directly from pixels rather than humans manually designing them.

## 2. AlexNet (2012)

The "Big Bang" of modern AI. Alex Krizhevsky and Geoffrey Hinton entered this model into the ImageNet competition and crushed the competition.

- **Architecture.** Much deeper than LeNet (8 layers).
- **Innovations.** \* **ReLU.** First major use of ReLU instead of Sigmoid.
- **Dropout.** Used to prevent massive overfitting.
- **GPUs.** First to use Graphics Cards to train a model in parallel.

- **Impact.** This started the "Deep Learning" era.

## 3. VGG-16 (2014)

Developed by the Visual Geometry Group at Oxford, this model focused on **simplicity and depth**.

- **Architecture.** It used 16 layers but kept things very uniform. Every Convolution was a small 3x3 filter, and every Pooling was 2x2.
- **The Philosophy.** By stacking many small 3x3 filters, you can see the same area as one large filter but with more non-linearity and fewer parameters.
- **Impact.** It is still widely used today as a "backbone" for feature extraction because of its elegant, repetitive structure.

## 4. Why these were limited

As researchers tried to make these models even deeper (e.g., 50 or 100 layers), they hit a "wall."

- **Vanishing Gradients.** The deeper the network, the harder it was for the error signal to reach the early layers.
- **Degradation.** Adding more layers actually made the accuracy _worse_ because the network became too hard to optimize.

## 5. Summary of the Classic Era

The transition from LeNet to VGG represents the shift from "hand-crafted" logic to "deep-learning" power.

| Model       | Year | Defining Feature           | Main Contribution                                                                    |
| :---------- | :--- | :------------------------- | :----------------------------------------------------------------------------------- |
| **LeNet-5** | 1998 | Hand-written Digit Expert  | Proved that Convolutions can replace manual feature engineering.                     |
| **AlexNet** | 2012 | The Deep Learning Catalyst | Introduced ReLU, Dropout, and GPU training to scale CNNs.                            |
| **VGG-16**  | 2014 | Standardized Depth         | Proved that small $3 \times 3$ filters stacked deeply are better than large filters. |
