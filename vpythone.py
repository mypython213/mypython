import datetime
from datetime import date

def if_line(cond,V1,V2):
    if cond:
        return V1
    return V2

class Sugar1:
    avatar = ""
    premium = False
    def set_avatar(self, url:str):
        self.avatar = url
    def active_prem(self):
        self.premium = self.premium ^ True
        print(if_line(self.premium, "Premium access activated", "Premium access disactivated"))

class User (Sugar1):
    nam = ''
    birthday = 0
    friends = []

    def __str__(self):
        return self.nam
    def __init__(self, name, birthday):
        self.nam = name
        self.birthday = birthday
        self.friends = []

    def get_friends(self):
        r = [i.nam for i in self.friends]
        return r

    def get_age(self):
        # datetime.date()
        return date.today().year - self.birthday.year

    def add_friend(self, new):
        return self.friends.append(new)

    def __len__(self):
        return len (self.friends)

    def __le__(self, other):
        return len (self.friends) <= len (other.friends)

class Author(User):
    posts = []
    def add_post(self, content:str="Empty line"):
        self.posts.append(content)
    def remove_post(self, id:int=-1):
        self.posts.pop(id)
# **
V1 = Author("Anonim1", datetime.date(2016,5,30))
V2 = User("Anonim214", datetime.date(2006,5,1))
print(f"Возраст ", V1.get_age())
print(f"Список друзей одинокого пользователя {V1.nam}: {V1.get_friends()}" )
V1.add_friend(V2)
print(f"Список друзей пользователя {V1.nam} после добавления одного друга: {V1.get_friends()}" )

V1.active_prem()
V1.active_prem()
V1.active_prem()
V1.set_avatar('error')

print(f"Список постов {V1.nam} изначально: {V1.posts}" )
V1.add_post()
V1.add_post("How add post?")
V1.add_post("I'm super admin!")
print(f"Список постов {V1.nam} после добавления: {V1.posts}" )

V1.remove_post(1)
print(f"Список постов {V1.nam} конечно: {V1.posts}" )
V1.remove_post()
print(f"Список постов {V1.nam} совсем конечно: {V1.posts}" )


class Network:
    users = []
    def init(self):
        self.users.append( User("Anonim1", datetime.date(2016, 5, 30)) )
        self.users.append( User("Anonim2", datetime.date(1686, 1, 1)) )
        self.users.append( User("Adam", datetime.date(100, 1, 1)) )

        self.users[0].add_friend(self.users[1])
        self.users[0].add_friend(self.users[2])
        # V2 = User("Anonim214", datetime.date(2006, 5, 1))
    def __getitem__(self, item):
        for i in self.users:
            if i.nam == item:
                return i
                break
        return None

    def __gt__(self, other):
        return self.users.nam > other.users.nam



VPythone = Network()
VPythone.init()

t = VPythone['Anonim1']
print(f"Найден пользователь {t} (друзей {len (t)}) ")
print(f"Отношние первых двух: {VPythone.users[0]<=VPythone.users[1]}")


print (VPythone.users[0].get_friends())
print (f"Возраст второго {VPythone.users[1].get_age() }")
print ("Количество друзей первого ", len( VPythone.users[0].get_friends()))

# print(VPythone.users[0])
# print(VPythone.users[0])
