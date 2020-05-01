my_list = [1, 5, 4, 3]

my_list1 = list()

# print(my_list)
#
# my_list.sort()
#
# print(my_list)

print(my_list)

new_number = int(input("Type number : "))

my_list += [new_number]

my_list.append("12333")
my_list.append(True)
my_list.append(3.14)
my_list.append('c')
my_list.append([1, 2, 3])

print(my_list)
print("Index 3. ->", my_list[3])
print("Last element ->", my_list[-1])

# for i in my_list:
#     print(i, end=" ")
