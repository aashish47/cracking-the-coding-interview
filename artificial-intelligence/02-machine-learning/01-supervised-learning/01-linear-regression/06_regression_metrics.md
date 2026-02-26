# 06 Regression Metrics

To determine the effectiveness of a linear regression model, we must quantify the difference between the predicted values ($\hat{y}$) and the actual values ($y$). These metrics allow us to compare different models and evaluate their predictive power.

## 1. Mean Absolute Error (MAE)

MAE measures the average magnitude of the errors in a set of predictions, without considering their direction. It is the average of the absolute differences between prediction and actual observation.

$$MAE = \frac{1}{m} \sum_{i=1}^{m} |y^{(i)} - \hat{y}^{(i)}|$$

- **Interpretation:** It tells us, on average, how far off our predictions are in the same units as $y$.
- **Robustness:** It is more robust to outliers than MSE because it does not square the errors.

## 2. Mean Squared Error (MSE)

As discussed in the cost function section, MSE squares the residuals before averaging them.

$$MSE = \frac{1}{m} \sum_{i=1}^{m} (y^{(i)} - \hat{y}^{(i)})^2$$

- **Interpretation:** Because the errors are squared, MSE heavily penalizes large errors (outliers).
- **Unit Issue:** The units of MSE are the square of the target units (e.g., dollars squared), making it harder to interpret intuitively.

## 3. Root Mean Squared Error (RMSE)

RMSE is simply the square root of the MSE. This brings the error metric back into the original units of the target variable $y$.

$$RMSE = \sqrt{\frac{1}{m} \sum_{i=1}^{m} (y^{(i)} - \hat{y}^{(i)})^2}$$

- **Interpretation:** "The model's predictions are, on average, within $RMSE$ units of the actual value."
- **Usage:** This is often the preferred metric in many ML competitions and business cases.

## 4. R-Squared ($R^2$) - Coefficient of Determination

$R^2$ measures the proportion of variance in the dependent variable explained by the model compared to a simple mean baseline.

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$

### Component Notations:

- **$SS_{res}$ (Sum of Squared Residuals):** $\sum_{i=1}^{m} (y^{(i)} - \hat{y}^{(i)})^2$. Represents the error remaining after the model has been fitted.
- **$SS_{tot}$ (Total Sum of Squares):** $\sum_{i=1}^{m} (y^{(i)} - \bar{y})^2$. Represents the total variance in the data (where $\bar{y}$ is the mean of $y$).

### Interpretation of $R^2$ Values:

| Value        | Meaning                                                               |
| ------------ | --------------------------------------------------------------------- |
| **1.0**      | The model explains 100% of the variance (Perfect fit).                |
| **0.0**      | The model performs no better than simply predicting the mean.         |
| **Negative** | The model is worse than predicting the mean (rare in trained models). |

## 5. Adjusted R-Squared

Standard $R^2$ will always increase or stay the same when you add more features, even if those features are useless noise. **Adjusted $R^2$** penalizes the addition of unnecessary features.

$$Adjusted\ R^2 = 1 - \left[ \frac{(1 - R^2)(m - 1)}{m - n - 1} \right]$$

- **$m$:** Number of data points.
- **$n$:** Number of features.
- **Usage:** Use this when comparing multivariate models with different numbers of predictors.

## Summary Table: Which Metric to Use?

| Metric         | Primary Use Case                                           | Sensitivity to Outliers |
| -------------- | ---------------------------------------------------------- | ----------------------- |
| **MAE**        | When you want an intuitive average error.                  | Low                     |
| **RMSE**       | When large errors are particularly undesirable.            | High                    |
| **$R^2$**      | When you want to know how much "info" your model captured. | N/A                     |
| **Adj. $R^2$** | When comparing models with different feature counts.       | N/A                     |
