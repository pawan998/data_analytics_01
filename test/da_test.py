import sys
sys.path.append('./src')
from da_function import addition

# # from src.da_function import load_csv

# loan_df, payment_df, variables_df = load_csv()

src_val = addition(2, 3)

def test_addition(a, b):
    return a + b

test_value = test_addition(2, 3)

print("source value:", src_val, test_value)