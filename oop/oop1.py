class Person:
    name = ''
    surname = ''
    age = 0

# static variables or class variables


hamid = Person()
hamid.name = "Hamid"
hamid.surname = "Sultanzadeh"
hamid.age = 20


print(hamid)
print(hamid.name, hamid.surname, hamid.age)

john = Person()
john.name = "John"
john.surname = "Travolta"
john.age = 60

print(john)
print(john.name, john.surname, john.age)
