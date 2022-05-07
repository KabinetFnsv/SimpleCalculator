#simpleapp

print("Write first value" )
a = int(input())
#
print("Write second value")
b = int(input())
#
print("What operatoin you choose: +, -, *, /, **, %")
c = input()

def func(a, b, c):
    if c == '+':
        return  a + b
    elif c == '-':
        return  a - b
    elif c == '*':
        return  a * b
    elif c == '/':
        if b == 0:
            print("Cant devide on 0")
        else:
            return a / b
    elif c == '**':
        return  a ** b
    elif c == '%':
        return  a % b
    else:
        print("Write correct value's ")


result = func(a, b, c )
print(a, c, b, ", and result is:", result)
