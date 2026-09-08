import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: 除数不能为0"
    return a / b

def square(a):
    return a ** 2

def sqrt(a):
    if a < 0:
        return "Error: 不能对负数开根号"
    return math.sqrt(a)

if __name__ == "__main__":
    print("计算器启动！")
    print(f"5 的平方 = {square(5)}")
    print(f"16 的平方根 = {sqrt(16)}")