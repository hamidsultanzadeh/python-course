alphabet = "abcdef"

print("z" in alphabet)

print("z" not in alphabet)

for z in alphabet:
    print(z, end=" ")

print()

# -------------
# is - as Java Object Equals method
# -------------

x = 5

print(id(x), id(5), sep="\n")

if x is 5:
    print(x, "is 5")
