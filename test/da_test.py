import sys
sys.path.append('./src')
from da_function import addition

def test_addition():
    assert addition(2, 3) == 5