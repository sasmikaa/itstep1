class Humen:
    def __init__(self, name="Humen"):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, humen):
        self.passengers.append(humen)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"not passengers{self.brand}")
petro = Humen("Petro")
zina = Humen("Zina")

car = Auto("vishnovaasemerka")
car.add_passengers(petro)
car.add_passengers(zina)
car.print_passengers_names()