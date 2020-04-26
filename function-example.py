def new_function_test():
    x = 5
    y = 10
    z = x + y
    print(z)


def all_calculator(number1, number2):
    print("==============")
    print(number1+number2)
    print(number1-number2)
    print(number1*number2)
    print(number1/number2)
    print("==============")


def increase_and_return(number):
    return "result " + str(number+1)
    # return number+1


all_calculator(9, 3)
all_calculator(12,4)

print(increase_and_return(10))

