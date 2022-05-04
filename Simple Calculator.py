#simpleapp

print("Write first value" )
a = int(input())
#
print("Write second value")
b = int(input())
#
print("What operatoin you choose: +, -, *, /, **, %")
c = input()
if c == "+":
    print(a, c, b, ", and resuls: ", a + b)
elif c== "-":
    print(a, c, b, ", and resuls: ", a - b)
elif c== "*":
    print(a, c, b, ", and resuls: ", a * b)
elif c == "/":
    if b == 0:
        print("Cant devide on 0")
    else:
        print(a, c, b, ", and resuls:", a / b)
elif c == "**":
    print(a, c, b, ", and resuls: ", a ** b)
elif c == "%":
    print(a, c, b, ", and resuls: ", a % b)
else:
    print("Write correct value's ")
