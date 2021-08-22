<h1 align="center">Classification: Preventing Credit Card Fraud at Point-of-Sale</h1>
<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/Credit_Card_Fraud/images/credit_card_fraud.jpg?raw=true" height="300"></p>

# <a id='0.0'> Project Summary</a>

In this project, I use an openly available dataset of credit card transactions to create a **classification model to detect and prevent future fraudelent transactions at point-of-sale.**

Unlike typical binary classification problems, I <u>do not</u> use performance measures such as [accuracy, precision, recall or AUC](https://en.wikipedia.org/wiki/Confusion_matrix) to evaluate the winnning model. Instead, I take a [cost-sensitive approach](https://machinelearningmastery.com/cost-sensitive-learning-for-imbalanced-classification/). I contrast the current cost of fraudelent transactions (the "do-nothing" approach) and the costs associated with using a classification model (given that misclassification costs differ, that is to say the cost of allowing a fraudelent transaction through is much higher than preventing and reviewing a legitimate transaction incorrectly flagged as fraudelent - something which standard performance measures do not consider).

**I consider 10 models, with the winning model (a hyperparameter tuned logistic regression classifier) reducing the cost of fraud from an estimated € 30,000/day to € 4,800/day (with model costs considered), a cost-saving amount of ~84%.**

Please see [here](https://github.com/three14consulting/Python/blob/main/Credit_Card_Fraud/credit_card_fraud.ipynb) for the notebook containing the analysis.
