# 03 Encoding

Most ML algorithms (like Linear Regression or SVMs) require numerical input. Encoding is the process of converting Categorical Data (text/labels) into Numerical Data without losing the underlying meaning.

## 1. Label Encoding

| Feature       | Description                                                                     |
| :------------ | :------------------------------------------------------------------------------ |
| **Concept**   | Assigns a unique integer to each category (e.g., Low=0, Med=1, High=2).         |
| **Use Case**  | **Ordinal Data** (where order matters).                                         |
| **Pros/Cons** | Simple, but algorithms might misinterpret the order as magnitude (e.g., 2 > 0). |

## 2. One-Hot Encoding

| Feature      | Description                                                                                                                                                                                  |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Concept**  | Creates a new binary column for each category (e.g., `Color_Red`, `Color_Blue`, `Color_Green`).                                                                                              |
| **Use Case** | **Nominal Data** (where order doesn't matter). (e.g., Red=[1,0,0], Blue=[0,1,0], Green=[0,0,1]).                                                                                             |
| **Trap**     | **Dummy Variable Trap**: Multicollinearity caused by including all $N$ columns. (e.g., If you have 'Red', 'Blue', and 'Green', knowing it's not Red or Blue automatically means it's Green). |
| **Solution** | Drop one column (use $N-1$ columns).                                                                                                                                                         |

## 3. Target (Mean) Encoding

| Feature     | Description                                                                   |
| :---------- | :---------------------------------------------------------------------------- |
| **Concept** | Replaces the category with the mean of the target variable for that category. |
| **Risk**    | High risk of **Data Leakage** or **Overfitting**.                             |

## 4. The Dummy Variable Trap

When using One-Hot Encoding, if you have $N$ categories, you only need $N-1$ columns. Including all $N$ columns creates **Multicollinearity**.
**Multicollinearity** occurs when independent variables are highly correlated, meaning one can be linearly predicted from the others. This makes models like **Linear Regression** unstable because it becomes difficult to determine the individual effect of each variable on the target.

> **Note:** Tree-based models are generally unaffected by the Dummy Variable Trap.
