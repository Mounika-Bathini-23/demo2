import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

df=pd.DataFrame(load_diabetes().data,columns=load_diabetes().feature_names)


X=df.iloc[:,:-1]
y=df.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size=0.2, random_state=42
)

model=DecisionTreeRegressor()
model.fit(X_train, y_train)
y_pred=model.predict(X_test)
accuracy=mean_squared_error(y_test, y_pred)
print(accuracy)
