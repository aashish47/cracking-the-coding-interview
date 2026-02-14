# 03 Normal Forms (Normalization)

The process of organizing data to minimize redundancy and dependency anomalies (Update, Insertion, Deletion anomalies).

**The Ultimate Mnemonic:**

> "The data depends on **the Key (1NF)**, **the Whole Key (2NF)**, and **Nothing But the Key (3NF)**... so help me Codd."

| Form     | Requirement                                                                                         |
| :------- | :-------------------------------------------------------------------------------------------------- |
| **1NF**  | Attributes must be **atomic** (no repeating groups or multi-valued attributes).                     |
| **2NF**  | 1NF + No **Partial Dependency** (Non-prime attribute depends on part of a composite Candidate Key). |
| **3NF**  | 2NF + No **Transitive Dependency** (Non-prime attribute depends on another non-prime attribute).    |
| **BCNF** | 3NF + For every dependency $X \rightarrow Y$, $X$ must be a **Super Key**.                          |

## Key Definitions

- **Atomic:** A value that cannot be divided into smaller parts (e.g., a single phone number vs. a list of numbers).
- **Determines ($X \rightarrow Y$):** If the value of attribute $X$ uniquely identifies the value of attribute $Y$, then $X$ determines $Y$.
- **Partial Dependency:** When a non-prime attribute depends on only a _portion_ of a composite primary key rather than the entire key.
- **Transitive Dependency:** When a non-prime attribute depends on another non-prime attribute (e.g., $A \rightarrow B$ and $B \rightarrow C$, therefore $A \rightarrow C$).
- A **Prime Attribute** is an attribute that is part of any candidate key.
