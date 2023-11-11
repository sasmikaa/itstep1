import random

class Pet:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 1
        self.alive = True

    def to_run_dog(self):
        print("time to run")
        self.gladness -= 3


    def to_sleep(self):
        print("time to sleep")
        self.gladness += 3
        self.progress += 0.01
    def to_play(self):
        print("time to play")
        self.gladness += 5

    def to_eat(self):
        print("time to eat")
        self.progress += 1

    def is_alive(self):
        if self.progress < 0:
            print("Murka ne virosla")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
        elif self.gladness > 705:
            print("Murka good")
            self.alive = False
        elif self.progress > 5:
            print("Murka virosla")
            self.alive = False
        # elif self.progress > 5:
        #     print("Murka virosla")
        #     self.alive = False

    def end_of_day(self):
        print(f"gladness = {self.gladness}")
        print(f"progress = {round(self.progress)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_run_dog()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_play()
        elif live_cube == 4:
            self.to_eat()

        self.end_of_day()
        self.is_alive()

murka = Pet("Murka")

for day in range(365):
    if murka.alive == False:
        break
    murka.live(day)