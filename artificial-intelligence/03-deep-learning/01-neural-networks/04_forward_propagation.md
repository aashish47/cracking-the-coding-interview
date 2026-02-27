# 04 Forward Propagation

Forward Propagation is the process where the neural network takes input data and passes it through the layers to generate a prediction. Think of it as a series of complex "Weight $\rightarrow$ Sum $\rightarrow$ Activate" steps.

## 1. The Core Calculation

For every single neuron, the math happens in two distinct steps:

### Step 1: The Linear Combination

We multiply the inputs by their weights and add a bias. This is basic matrix math.

$$z = w_1x_1 + w_2x_2 + \dots + w_nx_n + b$$

In vector notation, this is simplified to:

$$z = W \cdot X + b$$

### Step 2: The Non-linear Activation

We pass $z$ through an activation function (like ReLU or Sigmoid) to get the final output of that neuron, called the **activation ($a$)**.

$$a = \sigma(z)$$

## 2. Layer-by-Layer Flow

In a network, the output of one layer becomes the input for the next.

1. **Input Layer ($a^{[0]}$):** The raw features (e.g., pixel values of an image).
2. **First Hidden Layer ($a^{[1]}$):**

- $z^{[1]} = W^{[1]}a^{[0]} + b^{[1]}$
- $a^{[1]} = g(z^{[1]})$ (where $g$ is the activation function).

3. **Second Hidden Layer ($a^{[2]}$):**

- $z^{[2]} = W^{[2]}a^{[1]} + b^{[2]}$
- $a^{[2]} = g(z^{[2]})$

4. **Output Layer ($\hat{y}$):** The final activation is our prediction.

## 3. A Concrete Example

Imagine a single neuron with **two inputs**:

- **Inputs ($X$):** $x_1 = 0.5, x_2 = 1.2$
- **Weights ($W$):** $w_1 = 0.4, w_2 = -0.2$
- **Bias ($b$):** $0.1$
- **Activation:** ReLU

**Step 1: Calculate $z$**
$$z = (0.5 \times 0.4) + (1.2 \times -0.2) + 0.1$$
$$z = 0.2 - 0.24 + 0.1 = 0.06$$

**Step 2: Apply Activation ($a$)**
$$a = \max(0, 0.06) = 0.06$$

If the result $z$ had been **-0.06**, the ReLU activation would have turned the output into **0**.

## 4. Why Matrix Multiplication?

Calculating each neuron one by one would be incredibly slow. Instead, we group all neurons in a layer into a **Weight Matrix ($W$)**.

- By using matrices, we can calculate the activations for an entire layer (and even an entire batch of data) in one single mathematical operation.
- This is why **GPUs (Graphics Processing Units)** are so important for AI—they are designed specifically to do this type of matrix math very, very fast.

## 5. The Result: The Prediction ($\hat{y}$)

At the end of forward propagation, the network spits out a number.

- **Example:** For a cat/dog classifier, the output might be $0.85$.
- The network "thinks" there is an 85% chance this image is a dog.

However, at the start of training, the weights are random, so the prediction will be garbage. To fix this, we need to measure how "wrong" the prediction is.
