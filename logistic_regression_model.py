from sklearn import datasets
from sklearn import linear_model
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd

# read in data and merge into one
electronics = pd.read_csv('electronics.csv')
profiles = pd.read_csv('profile.csv')
df = pd.merge(electronics, profiles, on='clients')

# feature selection
x = ['amount_financing', 'LT_clients', 'promotions_used', 'require_financing', 'prize_won']
y = ['got_a_TV']
model = LogisticRegression()
rfe = RFE(model, 3)
rfe = rfe.fit(df[x], df[y])
print(rfe.support_)
print(rfe.ranking_)

model = LogisticRegression()
nof = np.arange(1,12)
for n in range(1,12):
    rfe = RFE(model, n)
    rfe = rfe.fit(df[x], df[y])
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=11)
    regression_model = linear_model.LogisticRegression()
    regression_model.fit(X_train, y_train)
    regression_model.predict(X_test)


# select columns to be used in model
x_cols = ['promotions_used', 'require_financing', 'prize_won']
X = df[x_cols]
Y = df[y]

# split data into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=11)

# create the model using train data
regression_model = linear_model.LogisticRegression()
regression_model.fit(X_train, y_train)

# validate/evaluate accuracy of model
predicted = regression_model.predict(X_test)
print(metrics.accuracy_score(y_test, predicted))
# 0.90076 accuracy on test model