class Car:
    wheel_count = 4
    speed = 0

    def __init__(self, name):
        self.name = name
    @classmethod
    def launch(cls, speed):
        cls.speed = speed
    def turbo(self, speed):
        if speed > 100:
            self.wheel_count +=2

car = Car("Lada")
car.launch(1000)
car.turbo(1000)
print (car.wheel_count)
print (Car.wheel_count)