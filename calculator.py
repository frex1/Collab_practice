def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '%':
        return a % b
    else:
        return 'Invalid operator'

def test_hello():
    print('Just trying to create a conflict here. Working on our GitHub magic is fun.')