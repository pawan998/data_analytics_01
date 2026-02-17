from src.da_function import load_csv

loan_df, payment_df, variables_df = load_csv()

print("Loan DataFrame:", loan_df.shape)
print("Payment DataFrame:", payment_df.shape)
print("Variable Descriptions DataFrame:", variables_df.shape)