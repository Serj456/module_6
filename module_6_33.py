import random
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]
    def __init__(self, speed):

        self.speed = speed
    def move(self, dx, dy, dz):
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self._cords[0] = self.dx * self.speed
        self._cords[1] = self.dy * self.speed
        self._cords[2] = self.dz * self.speed
        if self._cords[2] < 0:
            print("It's too deep, i can't dive :(")
            self._cords[2] = self.dz * self.speed
    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")
    pass
class Bird(Animal):

    beak = True
    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1,4)} eggs for you")
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, number):
        self._cords[2] = self._cords[2] - abs(number*self.speed)
        if self._cords[2] < 0:
            print("It's too deep, i can't dive :(")
            self._cords[2] = self.dz * self.speed



class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    def __init__(self, speed):
        super().__init__(speed)
    def speak(self):
        sound = "Click-click-click"
        print(sound)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()