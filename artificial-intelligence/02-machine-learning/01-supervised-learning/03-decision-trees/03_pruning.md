# 03 Pruning

Because Decision Trees continue to split until every leaf is pure, they often create overly complex rules that only apply to the training data. This is **overfitting**. **Pruning** is the process of removing sections of the tree that provide little power to classify new instances.

## 1. Pre-Pruning (Early Stopping)

Pre-pruning involves stopping the tree-building process before it reaches its full depth. We set "stopping conditions" or **hyperparameters** during training:

- **Max Depth:** Limits how many levels the tree can have.
- **Min Samples Split:** The minimum number of samples a node must have before it can be split.
- **Min Samples Leaf:** The minimum number of samples allowed in a leaf node.
- **Max Leaf Nodes:** Limits the total number of terminal nodes.

## 2. Post-Pruning (Cost Complexity Pruning)

In post-pruning, we allow the tree to grow to its full extent and then "trim" branches that add more complexity than they are worth.

- **Logic:** We evaluate each sub-tree. If removing a sub-tree and replacing it with a leaf node doesn't significantly decrease the model's accuracy on a validation set, we prune it.
- **Cost Complexity Parameter ($\alpha$):** We define a cost function that balances the tree's error rate against the number of leaves.

$$Cost = Error + \alpha \cdot (\text{Number of Leaves})$$

- As $\alpha$ increases, more nodes are pruned, resulting in a smaller, simpler tree.

## 3. Why Prune?

1. **Reduces Variance:** Prevents the model from being too sensitive to noise in the training data.
2. **Improves Generalization:** Makes the model perform better on new, unseen data.
3. **Better Interpretability:** A smaller tree is much easier for a human to read and understand.

## 4. The Bias-Variance Trade-off in Trees

- **Unpruned Tree:** High Variance / Low Bias (Overfits).
- **Heavily Pruned Tree:** Low Variance / High Bias (Underfits).
- **The Goal:** Find the "Sweet Spot" where the tree is complex enough to capture the pattern but simple enough to ignore the noise.
