import sys
import pandas as pd
from io import StringIO


def outlier_threshold(dataframe, col_name, q1=0.25, q3=0.75):
    quartile1 = dataframe[col_name].quantile(q1)
    quartile3 = dataframe[col_name].quantile(q3)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit


def remove_outliers(dataframe, col_name):
    if col_name == 'ALL':
        deleted_rows_total = 0
        for col in dataframe.columns:
            low_limit, up_limit = outlier_threshold(dataframe, col)
            initial_length = len(dataframe)

            df_without_outliers = dataframe[~(
                (dataframe[col] < low_limit) | (dataframe[col] > up_limit))]

            final_length = len(df_without_outliers)
            if final_length < initial_length:
                deleted_rows = initial_length - final_length
                deleted_rows_total += deleted_rows

    else:
        low_limit, up_limit = outlier_threshold(dataframe, col_name)
        initial_length = len(dataframe)

        df_without_outliers = dataframe[~(
            (dataframe[col_name] < low_limit) | (dataframe[col_name] > up_limit))]

        final_length = len(df_without_outliers)
        if final_length < initial_length:
            deleted_rows = initial_length - final_length
        

    return df_without_outliers


def fill_na_with_mean(df, col):
    if col == 'ALL':
        for col_name in df.columns:
            if df[col_name].isna().any():
                print(
                    f"{df[col_name].isna().sum()} row(s) filled with mean value in column '{col_name}' due to being NA.")
                df[col_name] = df[col_name].fillna(df[col_name].mean())
            else:
                print(
                    f"No rows filled with column mean value in column '{col_name}' due to being NA.")
    else:
        if df[col].isna().any():
            print(
                f"{df[col].isna().sum()} row(s) filled with mean value in column '{col}' due to being NA.")
            df[col] = df[col].fillna(df[col].mean())
        else:
            print(
                f"No rows filled with column mean value in column '{col}' due to being NA.")


if __name__ == "__main__":
    if sys.stdin.isatty():
        print("Running interactively.")
    else:
        csv_content = sys.stdin.read().strip()
        col = sys.argv[1]
        training_ratio = float(sys.argv[2])

        df = pd.read_csv(StringIO(csv_content))

        fill_na_with_mean(df, col)
        df = remove_outliers(df, col)

        sys.stdout.write(df.to_csv(index=False))
