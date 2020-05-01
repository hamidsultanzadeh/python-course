x = int(input())

length = 2 * x + 1
row = length


def draw(beg, end):

    for j in range(beg, end):
        if j == i:
            print(j - 1, end="")
        else:
            print("{} ".format(j - 1), end="")

    for j in range(i - 1, 0, -1):
        print(" {}".format(j - 1), end="")


for i in range(1, x + 2):
    print(" " * (length - 1), end="")

    draw(1, i+1)

    print()

    length -= 2

length = 1


for i in range(x, 0, -1):
    print(" " * (length + 1), end="")

    draw(1, i + 1)

    print()

    length += 2
