import datetime
from _datetime import date

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
