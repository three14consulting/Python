<h1 align="center">Regression: Predicting Bike Rental Demand</h1>
<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/Seoul_Bike_Rental/images/seoul_bikes.jpg?raw=true" height="300"></p>

# <a id='0.0'> Project Summary</a>

For this project, I use the **Bike Sharing Demand** dataset from the UCI Machine Learning Repository (found [here](https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand)) for the purposes of **predicting bike rental demand at each hour for the stable supply of rental bikes** (regression modeling). I consider the following regressors (some with hyperparameter tuning via nested cross-validation):

* Multiple Linear Regression
* Support Vector Regression
* Decision Tree Regression
* Ensemble Method Regression (Random Forest)
* Neural Network Regression

**The winning regressor is a Random Forest with a R2 score of ~0.85.**

Please see [here](https://github.com/three14consulting/Python/blob/main/Seoul_Bike_Rental/Seoul_Bike_Rental.ipynb) for the notebook containing the analysis.