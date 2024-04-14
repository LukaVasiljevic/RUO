import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error

if __name__ == "__main__":
    # Get the file path from environment variable
    file_path = os.environ.get('DATASET_PATH')
    # Get the k value from environment variable
    k = os.environ.get('RANDOM_STATE')

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
