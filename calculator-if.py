print("""
1. +
2. -
3. *
4. /
5. ^
""", end="")

sign = input("Operator: ")

number1 = float(input("Number1: "))
number2 = float(input("Number2: "))
result = 0

if sign == "+" or sign == "1":
    result = number1 + number2
elif sign == "-" or sign == "2":
    result = number1 - number2
elif sign == "*" or sign == "3":
    result = number1 * number2
elif sign == "/" or sign == "4":
    result = number1 / number2 if number2 != 0 else "/ by zero"
elif sign == "^" or sign == "5":
    result = number1 ** number2
else:
    print("Wrong operation")

print("Result is", result, sep="=")
