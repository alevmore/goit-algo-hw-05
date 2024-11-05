from typing import Callable
from functools import reduce
import re

def generator_numbers(text: str):
    text= text.split (' ')
    numbers = map (float, filter (lambda n: re.match (r'[\.,]{0,1}\d+.', n),text))
    for num in numbers:
        yield num
   
    
def sum_profit(text: str, func: Callable):
    return reduce(lambda x,y:x+y, func(text))


if __name__=="__main__":

    text = "The employee's total income consists of several parts: 1000.01 as the main income, supplemented by additional income of 27.45 and 324.00 dollars."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

