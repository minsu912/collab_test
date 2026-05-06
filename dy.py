def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2


def reverse (str):
    return str[::-1]

def is_even(n):
    if n % 2 == 0:
        return "even"
    else:
        return "not even"

result = is_even(20)
print(result)