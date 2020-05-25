class Person(object):

    def __init__(self,name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


hamid = Person("Hamid","Sultanzadeh",12)

print(hamid.name, hamid.surname, hamid.age)
