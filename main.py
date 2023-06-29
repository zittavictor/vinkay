import numpy as np
import pandas as pd

def generate_random_table(n_rows, n_cols):
    np.random.seed(101)
    data = np.random.randn(n_rows, n_cols)
    df = pd.DataFrame(data)
    return df

def calculate_row_statistics(df):
    stats_df = pd.DataFrame(index=df.index)
    stats_df['Mean'] = df.mean(axis=1)
    stats_df['Std Dev'] = df.std(axis=1)
    stats_df['Q1'] = df.quantile(0.25, axis=1)
    stats_df['Q2'] = df.quantile(0.50, axis=1)
    stats_df['Q3'] = df.quantile(0.75, axis=1)
    return stats_df

def concatenate_functions(n_rows, n_cols):
    random_df = generate_random_table(n_rows, n_cols)
    stats_df = calculate_row_statistics(random_df)
    concatenated_df = pd.concat([random_df, stats_df], axis=1)
    return concatenated_df

result_df = concatenate_functions(n_rows=20, n_cols=5)
print(result_df)