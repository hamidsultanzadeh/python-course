number1 = float(input("number1: "))

number2 = float(input("number2: "))

try:
    print(number1 / number2)
except ZeroDivisionError as ex:
    print("/ by zero exception",ex,sep="\n")
# finally:
#     print("close")


# raise

inp = int(input("inp: "))

if inp == 5:
    raise Exception(":(")

