"""Example script 01 - Demonstrate usage of package features."""

# First party modules
from verdant import verdant

num, result = verdant.get_config()
exp_result = [True for i in range(num)]
print(f"Result from function 'get_config': {result}")


result = verdant.fizzbuzz(16)
print(f"Result from function 'fizzbuzz(16)': {result}")


result = verdant.fibonacci(10)
print(f"Result from function 'fibonacci(10)': {result}")
