import pandas as pd
import numpy as np

def custom_info(df):
    # Get the number of rows and columns
    num_rows, num_cols = df.shape

    # Create a list to store the column information
    column_info = []

    # Iterate over each column
    for column in df.columns:
        # Get the data type of the column
        dtype = df[column].dtype

        # Replace 'None' with np.nan
        df[column] = df[column].replace('None', np.nan)

        # Get the number of non-null values in the column
        non_null_count = df[column].count()

        # Get the number of NaN values in the column
        nan_count = df[column].isnull().sum()

        # Get the number of unique values in the column
        unique_count = df[column].nunique()

        # Append the column information to the list
        column_info.append([column, non_null_count, nan_count, unique_count, dtype])

    # Create a DataFrame from the column information
    summary_df = pd.DataFrame(column_info, columns=['Column', 'Non-Null Count', 'Null Count', 'Unique Values', 'Dtype'])

    # Set the index of the summary DataFrame to the column names
    summary_df.set_index('Column', inplace=True)

    # Add a row for the total number of rows
    summary_df.loc['Total Rows'] = [num_rows, '', '', '']

    # Print the class and dimensions of the DataFrame
    print(f"<class 'pandas.core.frame.DataFrame'>")
    print(f"RangeIndex: {num_rows} entries, 0 to {num_rows - 1}")
    print(f"Data columns (total {num_cols} columns):")

    # Print the summary DataFrame
    print(summary_df)

    # Print the memory usage
    print(f"memory usage: {df.memory_usage().sum()} bytes")


