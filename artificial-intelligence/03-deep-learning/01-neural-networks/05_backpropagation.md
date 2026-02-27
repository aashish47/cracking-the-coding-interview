# 05 Backpropagation and Gradient Descent

Backpropagation and Gradient Descent constitute the fundamental optimization framework for training neural networks. While Forward Propagation generates a prediction, Backpropagation computes the necessary adjustments to minimize the objective function.

## 1. Gradient Descent: Optimization via Objective Minimization

Gradient Descent is a first-order iterative optimization algorithm used to find the local minimum of a differentiable cost function $J(w)$. It updates parameters in the opposite direction of the gradient.

### The Math of the Update:

$$w = w - \alpha \cdot \frac{\partial J}{\partial w}$$

- **$\alpha$ (Learning Rate):** The size of the step we take. Too big, and we overstep the valley. Too small, and training takes forever.
- **$\frac{\partial J}{\partial w}$ (The Gradient):** The slope of the hill. It tells us which direction is "downhill" and how steep it is.

## 2. Backpropagation: The Chain Rule

Backpropagation is how we calculate the gradients for every single weight in a network, starting from the output and moving backward to the input.

It relies on the **Chain Rule** from calculus. To find out how much a weight in the _first_ layer affected the _final_ error, we multiply the partial derivatives layer by layer:

$$\frac{\partial \text{Loss}}{\partial w_{input}} = \frac{\partial \text{Loss}}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z_{last}} \cdot \dots \cdot \frac{\partial a_1}{\partial w_{input}}$$

### The 4-Step Cycle:

1. **Forward Pass:** Compute the prediction and the loss.
2. **Backward Pass:** Calculate the gradient of the loss with respect to every weight and bias (using the Chain Rule).
3. **Update:** Adjust the weights using Gradient Descent.
4. **Repeat:** Do this thousands of times until the loss stops decreasing

## 3. The Vanishing Gradient Problem

In very deep networks, as we multiply many small gradients together (especially with **Sigmoid** or **Tanh** activations), the gradient can become incredibly small—almost zero.

- **Result:** The weights in the early layers stop updating, and the network stops learning.
- **Solution:** This is why we use **ReLU**, which keeps a constant gradient of $1$ for all positive values.

## 4. The Neural Network Training Cycle

1. **Initialize** weights randomly.
2. **Forward Propagate** a batch of data.
3. **Calculate Loss** (how wrong were we?).
4. **Backpropagate** to find gradients.
5. **Update Weights** to reduce loss.
6. **Loop** until the model is accurate.
