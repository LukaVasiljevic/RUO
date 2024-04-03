import sys
import pandas as pd
from io import StringIO
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, root_mean_squared_error
import numpy as np



if __name__ == "__main__":
    file_path = sys.argv[1]
    k = sys.argv[2]
    df = pd.read_csv(file_path)

    features = df.drop(columns=['MEDV'])
    target_variable = df['MEDV']

    r_state = 42 + int(k)

    X_train, X_test, y_train, y_test = train_test_split(
        features, target_variable, train_size=0.8, random_state=r_state)

    model = RandomForestRegressor(n_estimators=100, random_state=r_state)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    rmse = root_mean_squared_error(y_test, y_pred)
    print(rmse)