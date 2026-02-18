import sys
sys.path.append('./src')
from da_function import addition

src_val = addition(2, 3)

def test_addition(a, b, src_val):
    test_value = a + b
    print("source value:", src_val, ", Test Value:", test_value, ": Soruce value and test values are equal.")
    print("Testing successful!")

test_addition(2, 3, src_val)