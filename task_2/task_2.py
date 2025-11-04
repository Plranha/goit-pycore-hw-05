import re

def generator_numbers(text: str):
    pattern = r'\d+\.?\d*'

    for match in re.finditer(pattern, text):
        number_str = match.group()
        number = float(number_str)
        yield number
        

def sum_profit(text: str,func: callable):
    total = 0
    for number in func(text):
        total += number
    return total
    

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
result = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {result}")