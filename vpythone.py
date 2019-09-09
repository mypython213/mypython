import datetime
from datetime import date

class User:
    nam = ''
    birthday = 0;
    friends = []

    def __init__(self, name, birthday):
        self.nam = name
        self.birthday = birthday

    def get_friends(self):
        r = [i.nam for i in self.friends]
        return r

    def get_age(self):
        # datetime.date()
        return date.today().year - self.birthday.year

    def add_friend(self, new):
        return self.friends.append(new)


# **
V1 = User("Anonim1", datetime.date(2016,5,30))
V2 = User("Anonim214", datetime.date(2006,5,1))
print(f"Возраст ", V1.get_age())
print(f"Список друзей одинокого пользователя {V1.nam}: {V1.get_friends()}" )
V1.add_friend(V2)
print(f"Список друзей пользователя {V1.nam} после добавления одного друга: {V1.get_friends()}" )


class Network:
    users = []
    def init(self):
        self.users.append( User("Anonim1", datetime.date(2016, 5, 30)) )
        self.users.append( User("Anonim2", datetime.date(1686, 1, 1)) )
        self.users.append( User("Adam", datetime.date(100, 1, 1)) )

        self.users[0].add_friend(self.users[1])
        self.users[0].add_friend(self.users[2])
        # V2 = User("Anonim214", datetime.date(2006, 5, 1))


VPythone = Network()
VPythone.init()
print (VPythone.users[0].get_friends())
print (f"Возраст второго {VPythone.users[1].get_age() }")