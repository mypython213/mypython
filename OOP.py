class Plane:
    nam = ''
    engine = 0
    in_air = False

    def __init__(self, name):
        self.name = name

    def launch(self):
        self.in_air = True
        print("Launch")

    def fall(self):
        self.in_air = False
        print("Landing")
        self.engine -= 1

    @classmethod
    def add_wings(cls, count):
        cls.engine += count

    def get_engine_number(self):
        return self.engine
# **
car = Plane("Lada")
car.launch()
car.add_wings(10)
print (car.get_engine_number())
car.add_wings(10)
car.fall()
print (car.get_engine_number())

