# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Extreme Gradient Boosting, or XGBoost, is the model used for this project. Imstead of one big decision tree, it makes small ones, one after the other. Each new tree fixes any mistakes from the previous one made.
## Intended Use
The intended use is to find out if an individual has a salary either greater than or less than $50,000.
## Training Data
The training data is sourced from Barry Becker's 1994 U.S. Census dataset. It includes 14 features and a total of 48,842 entries. 80% of the dataset was allocated for training the model.
## Evaluation Data
The evaluation data will be the remaining 20% of the census dataset used for the training data.
## Metrics
_Please include the metrics used and your model's performance on those metrics._
Precision: 0.7901 | Recall: 0.6805 | F1: 0.7312
## Ethical Considerations
Using this model requires careful consideration of fairness, potential bias, privacy, and transparency. Because the dataset is older and includes sensitive demographic information, the model could reflect outdated patterns or produce unequal outcomes across different groups.
## Caveats and Recommendations
You should use the model for either educational or experimental use, but not for high-stake decisions. You can retrain the model periodically with more up to date info or document any potential biases or limitations you come across while using it.