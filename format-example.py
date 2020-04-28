my_string = """
name = Hamid
about = {} {}
""".format("I am Hamid","Sultanzadeh")


print(my_string)


# 1.

# var1 = "Hamid"
# var2 = "Sultanzadeh"
#
# new_var = "{1} {0}".format(var1, var2)
#
# print(new_var)

# 2.

# var1 = "Hamid"
# var2 = "Sultanzadeh"
#
# new_var = "{surname} {name}".format(name = var1, surname = var2)
#
# print(new_var)

# 3.

# var1 = "Hamid Sultanzadeh"
#
# new_var1 = "|{:<30}|".format(var1)
# new_var2 = "|{:>30}|".format(var1)
# new_var3 = "|{:^30}|".format(var1)
#
# print(new_var1, new_var2, new_var3, sep="\n")

# 4.

# new_var1 = "{:s}".format("new string")
# new_var2 = "{:d}".format(12)
# new_var3 = "{:b}".format(12)
#
# print(new_var1, new_var2, new_var3, sep="\n")
