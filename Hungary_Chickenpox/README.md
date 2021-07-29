<h1 align="center">Forecasting Varicella (Chickenpox) Cases in Hungary<br>(County & Nationwide)</h1>
<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/Hungary_Chickenpox/images/VaricellaSquare.jpg?raw=true" height="300"><img src="https://github.com/three14consulting/Python/blob/main/Hungary_Chickenpox/images/hungary_counties.png?raw=true" height="300"></p>
<h1><a id='0.0'> Project Summary</a></h1>

Forecasting cases of transmissible diseases ([varicella](https://en.wikipedia.org/wiki/Chickenpox) in this case, aka chickenpox) can help further public health understanding (such as increasing or decreasing prevalence) and plan accordingly (e.g. demand on healthcare resources whether that be manpower and/or medications such as vaccinations or other prevantative measures).

In this project, I attempt to forecast the cases of chickenpox in Hungary at county and national level, each week for 2014, by using methods from [Time-Series Analysis](https://en.wikipedia.org/wiki/Time_series) (such as Exponential Smoothing, SARIMA, VAR) - heavily using the [statsmodels](https://www.statsmodels.org/stable/index.html) API.

Please see [**here**](https://github.com/three14consulting/Python/blob/main/Hungary_Chickenpox/Hungary_Chickenpox.ipynb) for the notebook containing the project.

<h2>Diagnostics (Sample)</h2>
<h3>SARIMA Model for Budapest</h3>
<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/Hungary_Chickenpox/plots/SARIMA%20Model%20for%20BUDAPEST_results.jpg?raw=true" width="3600"></p>
<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/Hungary_Chickenpox/plots/SARIMA%20Model%20for%20BUDAPEST_residuals.jpg?raw=true" height="600"></p>
<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/Hungary_Chickenpox/plots/SARIMA%20Model%20for%20BUDAPEST_validation.jpg?raw=true" width="1200"></p>
