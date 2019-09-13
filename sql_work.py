from peewee import SqliteDatabase, Model, CharField, DateField, BooleanField, ForeignKeyField
from datetime import date
db = SqliteDatabase('people.db')
class Person(Model):
    name = CharField()
    age = DateField()
    sex = BooleanField()

    class Meta:
        database = db

#
Person.create_table()
#
# P1 = Person(name='Pip1', age=date(2000,1,1), sex=True)
# P1.save()
#
# Person.create (name='Pip2', age=date(2020,2,1), sex=False)

for i in range(50):
    Person.create(name='Anonim'+str(i), age=date(2020, 2, 1), sex=False)

# bob = list (Person.select(Person.age).where(Person.name == 'Anonim4'))
bob = list (Person.select().where(Person.name == 'Anonim4'))
# bob = Person.select(Person.age).where(Person.name == 'Pip').get()
print (bob[0].name)


class Pet(Model):
    name = CharField()
    type = CharField()
    owner = ForeignKeyField(Person, related_name='pets')
    class Meta:
        database = db

Pet.create_table()

# for i in range(5):
Pet.create(name='lucy', type='cat', owner=bob[0])
# Pet.create(name='lucy', type='cat', owner=bob[0])