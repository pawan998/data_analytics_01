import pandas as pd

def load_csv():
    
    loan_file_path = r"C:\Users\User\OneDrive\Data Analytics Project\data\input\loan.csv"
    pay_file_path = r"C:\Users\User\OneDrive\Data Analytics Project\data\input\payment.csv"
    var_file_path = r"C:\Users\User\OneDrive\Data Analytics Project\data\input\clarity_underwriting_variables.csv"

    loan_df = pd.read_csv(loan_file_path)
    payment_df = pd.read_csv(pay_file_path)
    variables_df = pd.read_csv(var_file_path, low_memory=False)

    print("Loan DataFrame:", loan_df.shape)
    print("Payment DataFrame:", payment_df.shape)
    print("Variable Descriptions DataFrame:", variables_df.shape)

    return loan_df, payment_df, variables_df

# Convert columns containing 'date' in their name to datetime format
def convert_to_datetime(df):
    for column_name in df.columns:
        if 'date' in column_name.lower():
            df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
    return df

# Extract text after the last dot and rename columns
def rename_columns_by_last_dot(df):
    df.columns = df.columns.str.split('.').str[-1]
    return df

# Merge loan_df and variables_df on the specified keys
def join_loan_tables(df1, df2):
    merged_df = pd.merge(
            df1, 
            df2, 
            left_on='anon_ssn', 
            right_on='underwritingid',
            how='left',
            validate='many_to_one'
        )
    return merged_df

def addition(a, b):
    return a + b