class Plane:
    name = ""
    def __init__(self, name = "Empty"):
        self.name = name
    def get_name(self):
        return self.name
    def up(self):
        raise NotImplementedError

class Piece(Plane):
    passenger = 0

    def alarm(self):
        pass
    def get_name(self):
        return "Looser"
    def landing(self):
        return "Landing"

class Battle(Plane):
    bomb = 0

    def active(self):
        print(f"{self.name} is active")

    def test_job(self):
        if hasattr(self, "job"):
            if self.job == "":
                print("Free")
            else:
                print("Worked")
        else:
            print("Free")

    def get_name(self):
        return self.name


class ColorChanger:
    color = 0
    def set_color(self, color):
        self.color = color


class MyPlane(ColorChanger, Battle, Piece):
    pass
W1 = MyPlane()
W1.test_job()
W1.landing()
print(W1.get_name())
print (MyPlane.__mro__)    # method resolution order


W1.set_color(23)