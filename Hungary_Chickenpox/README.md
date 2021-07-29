<h1 align="center">Forecasting Varicella (Chickenpox) Cases in Hungary<br>(County & Nationwide)</h1>
<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/Hungary_Chickenpox/images/VaricellaSquare.jpg?raw=true" height="300"><img src="https://github.com/three14consulting/Python/blob/main/Hungary_Chickenpox/images/hungary_counties.png?raw=true" height="300"></p>
<h1><a id='0.0'> Project Summary</a></h1>

In 2013 there were 140 million cases of [chickenpox](https://en.wikipedia.org/wiki/Chickenpox) (and shingles). Although a relatively mild disease, death occurs in about 1 per 60,000 cases and in 2015 chickenpox resulted in 6,400 deaths globally – down from 8,900 in 1990 (down 28%).

For any disease with significant prevalence, it is important for public health officials to understand how the disease is changing through the population so that they can plan resources accordingly (e.g. demand on healthcare resources whether that be manpower and/or medications such as vaccinations or other prevantative measures).

In this project, I use an openly available dataset of weekly chickenpox cases across Hungary (19 counties + Budapest) between 2005 and 2014 (~10,000 data points) to demonstrate and evaluate various forecasting models using methods from time series analysis (such as Exponential Smoothing, SARIMA, VAR) - heavily using the [statsmodels](https://www.statsmodels.org/stable/index.html) API.

Please see [**here**](https://github.com/three14consulting/Python/blob/main/Hungary_Chickenpox/Hungary_Chickenpox.ipynb) for the notebook containing the project.

<h2>Diagnostics (Sample)</h2>
<h3>SARIMA Model for Budapest</h3>
<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/Hungary_Chickenpox/plots/SARIMA%20Model%20for%20BUDAPEST_results.jpg?raw=true" width="3600"></p>
<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/Hungary_Chickenpox/plots/SARIMA%20Model%20for%20BUDAPEST_residuals.jpg?raw=true" height="600"></p>
<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/Hungary_Chickenpox/plots/SARIMA%20Model%20for%20BUDAPEST_validation.jpg?raw=true" width="1200"></p>
