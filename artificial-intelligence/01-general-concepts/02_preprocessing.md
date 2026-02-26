# 02 Data Preprocessing

Data in the wild is almost always messy, incomplete, or formatted inconsistently. Preprocessing is the "manual labor" of data science where you fix these issues, as models cannot compute equations if there are "NaN" (Not a Number) or null values.

## 1. Handling Missing Data

| Strategy                   | Method           | Description                                                                                 |
| :------------------------- | :--------------- | :------------------------------------------------------------------------------------------ |
| **Deletion**               | Rows/Columns     | Remove if target is missing, data is minimal (<5%), or column has >50% missing values.      |
| **Statistical Imputation** | Mean/Median/Mode | Fill gaps with Mean (normal distribution), Median (skewed/outliers), or Mode (categorical). |
| **Model-based Imputation** | KNN/Regression   | Use algorithms to predict missing values based on other features.                           |

## 2. Handling Outliers

Outliers can skew the mean and pull a model's "best fit line" in the wrong direction.

| Phase         | Technique | Logic                                                                   |
| :------------ | :-------- | :---------------------------------------------------------------------- |
| **Detection** | Z-Score   | Data points > 3 standard deviations from the mean.                      |
|               | IQR       | Data points outside $Q1 - 1.5 \times IQR$ or $Q3 + 1.5 \times IQR$.     |
| **Treatment** | Trimming  | Removing the outliers entirely.                                         |
|               | Capping   | Winsorizing (setting to 5th or 95th percentile) or clipping at max/min. |

## 3. Data Cleaning Checklist

Before moving to encoding or scaling, ensure:

- **Consistency:** Map variations (e.g., "NYC" vs "New York") to a single value.
- **Data Types:** Ensure numbers aren't stored as strings (e.g., "\$1,200" $\rightarrow$ `1200.0`).
- **Duplicates:** Remove identical rows to prevent "over-weighting" specific examples.

## 4. Feature Selection

Not every column is useful. Removing unnecessary data improves model efficiency.

| Type           | Example                   | Action                        |
| :------------- | :------------------------ | :---------------------------- |
| **Redundant**  | "Year of Birth" and "Age" | Keep only one.                |
| **Irrelevant** | "User ID" or "Row Number" | Drop (zero predictive power). |
