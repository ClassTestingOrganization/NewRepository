# pytest，只要寫函數，他就會自動測是test開頭的東西
# https://github.com/cccalg111a/alg111a

from factorial import *
def test_factorial():
    assert factorial(5) == 120