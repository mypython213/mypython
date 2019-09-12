
import json

my_object = [{'foo': 'bar'}]
# json_string = json.json_string(my_object)
j = json.dumps (my_object)
with open('squad.json') as f:
    content = f.read()
my_object = json.loads(content)
print(my_object['members'])


import pickle
class Foo:
    bar =['1', 2, {3}]

foo = Foo
# j = json.dumps(foo)
with open('aaa.txt', 'wb') as f:
    pickle.dump(foo, f)

with open('aaa.txt', 'rb') as f:
    new_foo = pickle.load(f)
print(new_foo.bar)