def main():
    f = open("dictionary.txt", "r")

    arr = f.readlines()

    f.close()

    f = open("dictionary.txt", "w+")

    arr.sort()

    for pair in arr:
        f.write(pair)
        if pair[len(pair) - 1] != "\n":
            f.write("\n")
            print(pair)
        else:
            print(pair[:len(pair) - 1])


if __name__ == "__main__":
    main()
