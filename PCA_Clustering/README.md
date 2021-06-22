<h1 align="center">Feature Extraction & Customer Segmentation</h1>
<p align="center"><img src="https://github.com/three14consulting/Python/blob/main/PCA_Clustering/images/pca_cluster.JPG?raw=true" height="500"></p>


# <a id='0.0'> Project Summary</a>

The dataset used in this project consists of close to 9,000 customers with 17 different measures (largely consisting of spend behaviour). The goals are:

1. To reduce the number of features in this dataset (via a dimensional reduction technique)
2. Find any natural groupings among the customers (via an unsupervised learning algorithm)

**Principal Components** and **k-means Clustering** were chosen as the algorithms to achieve the above goals.

The dataset was reduced **from 17 variables to 6 principal components** and **3 clusters** of customers were found via k-means clustering (used after principal components).

These three clusters can be further used for marketing initiatives, providing a behavioural descriptions of the clusters and what marketing efforts they may be susceptible too.

Please see [here](https://github.com/three14consulting/Python/blob/main/PCA_Clustering/pca_clustering.ipynb) for the notebook containing the analysis.
