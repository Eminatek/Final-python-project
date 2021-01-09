import sys, os # to open the dataset
import numpy as np # for the mse
import pandas as pd # to manage the data in a dataFrame
import joblib

from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier # for random forest model and adaboost
from sklearn.model_selection import train_test_split # to split data

# import the dataset
file_name = "/online_shoppers_intention.csv"
pathname = os.path.dirname(sys.argv[0])
dataset = pd.read_csv(pathname + file_name, engine = 'python')

# process the data
# keep only 4 features and the target variable
dataset = dataset[["PageValues","ExitRates","ProductRelated","ProductRelated_Duration","Revenue"]]
dataset['Revenue'] = pd.get_dummies(dataset['Revenue'])


# print(dataset.head())


# split the data
X = dataset.drop('Revenue', axis=1) # variable
y = dataset['Revenue'] # index
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=2, test_size=0.25, stratify = y)

# make the model
rf = RandomForestClassifier(max_depth=7, random_state=42, n_estimators=300)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
y_prob = rf.predict_proba(X_test)[:,1]

print(rf.score(X_train,y_train))
print(rf.score(X_test, y_test))

# save the model
joblib.dump(rf, "./model_saved")

# checking
reload_model = joblib.load("model_saved")
print(reload_model.predict([[5000,0.10,5,500]]))
print(reload_model.score(X_test, y_test))