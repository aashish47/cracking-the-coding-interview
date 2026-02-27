# 01 Perceptron to Neurons

Artificial Neural Networks (ANNs) are the foundation of modern AI, inspired by the biological neurons in our brains. The journey begins with the **Perceptron**, the simplest form of a neural network.

## 1. The Biological Inspiration

In nature, a neuron receives signals through **dendrites**, processes them in the **cell body**, and fires an electrical impulse through the **axon** to other neurons if the signal strength exceeds a certain threshold.

## 2. The Perceptron (The "Grandfather" Neuron)

Developed by Frank Rosenblatt in 1958, the Perceptron is a mathematical model that takes several binary inputs, multiplies them by weights, and passes the sum through a "Step Function."

### The Mathematical Formula:

$$z = \sum_{i=1}^{n} w_i x_i + b$$

- **$x_i$**: The input features.
- **$w_i$**: The weights (the "importance" of each input).
- **$b$**: The bias (how easy it is to get the neuron to fire).
- **$z$**: The weighted sum.

### The Decision Rule (Step Function):

$$Output = \begin{cases} 1 & \text{if } z > 0 \\ 0 & \text{if } z \leq 0 \end{cases}$$

## 3. The Evolution: From Perceptron to "Neuron"

The classic Perceptron had a major flaw: it could only output a $0$ or $1$. This "hard" switch made it impossible to use **Gradient Descent** (the math used to train deep networks), because you can't calculate a slope on a sharp cliff.

To fix this, we replaced the Step Function with **Activation Functions** (like Sigmoid or ReLU).

### How it compares to Logistic Regression:

If you use a **Sigmoid** activation function on a single neuron, the math is exactly the same as **Logistic Regression**:

$$\hat{y} = \sigma(\vec{w} \cdot \vec{x} + b)$$

**The key difference:** In a Neural Network, we don't just have one neuron; we stack thousands of them in layers.

## 4. The Linear Limitation (The XOR Problem)

A single perceptron can only learn **linear boundaries** (a straight line). In 1969, it was famously proven that a single perceptron could not solve the **XOR** (Exclusive OR) problem, because you cannot separate the points with one straight line.

**The Solution:** Adding a "Hidden Layer." By stacking neurons, the first layer transforms the data so the second layer can finally draw a valid boundary.
