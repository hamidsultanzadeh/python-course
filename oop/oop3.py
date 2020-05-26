class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color


class BMW(Car):

    def __init__(self, model, year, speed, color):
        super().__init__(speed, color)
        self.model = model
        self.year = year


bmwM3 = BMW("M3","2005", 250, "Black")

print(bmwM3.model, bmwM3.year, bmwM3.speed, bmwM3.color)

