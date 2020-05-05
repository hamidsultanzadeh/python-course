a = 3184
b = 37
d = 1
x = y = 1

p1 = -3184 * 18
p2 = 37 * 1549
res = p1 + p2
print("{} + {} = {}".format(p1,p2,res))

# -ax + by = d
# by - ax = d
# part1 + 1 == part2

while True:
    part1 = a*x
    part2 = b*y

    if part1 + 1 == part2:
        print("x : {}\ny : {}".format(x,y))
        break
    elif part1 > part2:
        y += 1
    else:
        x += 1


