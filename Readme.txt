dataset : https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset

Goal :
The goal is to find among the available variables, the most important to predict whether a user will complete a transaction or not on the site and to create the most efficient prediction model possible with the data from the dataset.

Consclusion :
Among the variables used to predict whether or not a user will purchase on the site, the most important is "PageValues" which is the average value for a page that a user visited before landing on the goal page or completing an Ecommerce transaction.
So it is essential to allocate value to pages that are most likely to persuade users to buy.
Creating a model with 90% correct prediction using a Random Forest model but with low sensitivity. This low sensitivity can maybe be explained because high values have been allocated to pages that are probably of little or no interest for the user.

JupiterNootBook :

For the JupiterNotebook, you need to download the dataset and provide the correct path to make it work.
The parameter search part takes time for the random forest.