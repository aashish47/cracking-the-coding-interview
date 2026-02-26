# Introduction to Artificial Intelligence

## 1. AI vs. ML vs. DL

| Feature         | Artificial Intelligence (AI)                                              | Machine Learning (ML)                                                | Deep Learning (DL)                                             |
| :-------------- | :------------------------------------------------------------------------ | :------------------------------------------------------------------- | :------------------------------------------------------------- |
| **Definition**  | The broad concept of machines acting "smart" or mimicking human behavior. | A subset of AI that uses algorithms to learn patterns from data.     | A subset of ML that uses multi-layered neural networks.        |
| **Logic**       | Can be based on "if-then" rules or complex math.                          | Learns from data without being explicitly programmed for every task. | Mimics the human brain structure to process unstructured data. |
| **Data Needs**  | Varies (can be very little for rule-based AI).                            | Requires thousands of data points (structured).                      | Requires millions of data points (Big Data).                   |
| **Human Input** | High (humans write the logic/rules).                                      | Medium (humans must "feature engineer" or label data).               | Low (the system discovers features on its own).                |
| **Hardware**    | Low to Medium (runs on standard CPUs).                                    | Medium (standard computers are usually fine).                        | High (requires powerful GPUs or TPUs).                         |
| **Examples**    | Chess bots, basic calculators, Siri/Alexa.                                | Spam filters, product recommendations, credit scoring.               | Self-driving cars, ChatGPT, facial recognition.                |

## 2. Types of Machine Learning

| Feature           | Supervised Learning         | Unsupervised Learning                | Reinforcement Learning         |
| :---------------- | :-------------------------- | :----------------------------------- | :----------------------------- |
| **Data Source**   | Labeled (Input + Answer)    | Unlabeled (Raw data)                 | Environment (No fixed dataset) |
| **Feedback**      | Direct (Correct vs. Wrong)  | None (Finds hidden patterns)         | Delayed (Reward or Penalty)    |
| **Goal**          | Predict a Class or Value    | Find Clusters or Structure           | Maximize Cumulative Reward     |
| **Core Idea**     | "Teacher-led" learning      | "Self-discovery"                     | "Trial and error"              |
| **Analogy**       | Learning with an Answer Key | Sorting a box of random LEGOs        | Teaching a dog a trick         |
| **Typical Tasks** | Classification, Regression  | Clustering, Dimensionality Reduction | Game AI, Robotics, Navigation  |

## 3. Key Terminology

- **Feature ($X$):** The input variables (e.g., square footage, number of rooms).
- **Target ($y$):** The variable you are trying to predict (e.g., the price of the house).
- **Model:** The mathematical representation of the relationship between $X$ and $y$.
- **Training:** The process of the model "learning" the patterns from the data.
- **Inference:** Using the trained model to make predictions on new, unseen data.

## 4. ML Workflow

1. **Data Collection:** Gathering the raw information.
2. **Data Cleaning:** Handling missing values and outliers.
3. **Feature Engineering:** Selecting and transforming variables (Encoding/Scaling).
4. **Model Selection:** Choosing the right algorithm.
5. **Training & Evaluation:** Teaching the model and testing its accuracy.
6. **Deployment:** Putting the model into a real-world application.
