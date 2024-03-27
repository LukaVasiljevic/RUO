import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, root_mean_squared_error
import numpy as np


def prmse(y_true, y_pred):
    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
    range_y = np.max(y_true) - np.min(y_true)
    prmse_value = (rmse / range_y) * 100
    return prmse_value


if __name__ == "__main__":
    file_path = sys.argv[1]
    training_ratio = float(sys.argv[2])

    df = pd.read_csv(file_path)

    features = df.drop(columns=['MEDV'])
    target_variable = df['MEDV']

    X_train, X_test, y_train, y_test = train_test_split(
        features, target_variable, train_size=training_ratio, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = root_mean_squared_error(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"Root Mean Squared Error: {rmse}")

    prmse_value = prmse(y_test, y_pred)
    print("PRMSE:", prmse_value)
