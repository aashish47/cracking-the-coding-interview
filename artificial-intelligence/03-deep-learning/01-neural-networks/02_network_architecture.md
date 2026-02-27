# 02 Network Architecture

Architecture refers to the structural arrangement of the neurons into layers and how they connect to one another.

## 1. The Three Standard Layers

A basic "Feedforward" Neural Network (also known as a Multi-Layer Perceptron or MLP) consists of three types of layers:

### A. The Input Layer

- This layer receives the raw data (features).
- There is exactly **one neuron for every input feature** (e.g., if you are predicting house prices using "size" and "bedrooms," you have 2 input neurons).
- No math happens here; it simply passes the signal forward.

### B. The Hidden Layer(s)

- These are the layers between the input and output. This is where the "learning" happens.
- A network can have one hidden layer (shallow) or hundreds (Deep Learning).
- Each neuron in a hidden layer looks for a specific **feature or pattern** in the data.

### C. The Output Layer

- This layer produces the final prediction.
- The number of neurons depends on the task:
- **Binary Classification:** 1 neuron (Outputting a probability between 0 and 1).
- **Regression:** 1 neuron (Outputting a continuous value).
- **Multi-class Classification:** $N$ neurons (One for each possible class).

## 2. Fully Connected (Dense) Layers

In a standard architecture, we usually use **Dense Layers**. This means every neuron in Layer $A$ is connected to every single neuron in Layer $B$.

- Each connection has its own unique **Weight ($w$)**.
- If Layer 1 has 3 neurons and Layer 2 has 4 neurons, there are $3 \times 4 = 12$ weights connecting them.
- As the network grows, the number of parameters (weights and biases) can reach into the millions or billions.

## 3. Deep vs. Shallow Networks

- **Shallow Networks:** Have only one or two hidden layers. They are good for simple, structured data.
- **Deep Networks:** Have many hidden layers. Each layer builds upon the previous one:
- **Early layers** might detect simple shapes or edges.
- **Middle layers** combine edges into complex patterns (like eyes or tires).
- **Final layers** recognize entire objects (like a face or a car).

## 4. How Data Flows: Forward Propagation

Data travels in one direction: **Input $\rightarrow$ Hidden $\rightarrow$ Output**.

1. Input features are multiplied by weights and summed.
2. A bias is added.
3. An **Activation Function** is applied to the result.
4. This output becomes the input for the next layer.
