hell = """dfsfs 
       dfsfsdfs 
       fdsfsf
       """
# ** base types
int_var = 1
float_var = 1.0
bool_var = False
string_var = "text"

# ** base conversion
bool(string_var)
float(int_var)
int(float_var)
str(float_var)

# ** list
my_list = [1, 2.0, '3', False, [1,2,3] ]
# -1    1:
l2 = [2,3,4,8,2,5,4]
l2.sort()
print(l2)
l2.pop(1)
print(l2)
print("Len:", l2.index(l2[-1])+1)
print("LenAlt:", len (l2))


# ** картеж tuple
my_tuple = (1, 2, 3)

# ** dictionary
my_dict = {
    'nom': 1,
    'name': "Admin",
    'index': 0
}
my_dict["appended"] = 99
my_dict[0] = 8
print (my_dict)
print (my_dict.items())

print (my_dict.keys(), "\n", my_dict.values())

# Example:
l1 = [1,2,3,4,5]
l2 = [i**2 for i in l1]
print (f"Example {l2} this")

# ** noname function
my_func = lambda x, y: (x,y,x**y)
print (f"{my_func(2, 3)}")
l3 = [(lambda x: x*2)(i) for i in l1]
print (l3)


# ** nammed function
def new_func(val_in: int) -> bool:
    r = val_in < 10
    return r

def new_func2(val_in: int) -> bool:
    if val_in < 10:
        return True
    elif val_in == 10:
        return True
    else:
        return False

print (new_func2(8))

def new_func3(val_in: int) -> bool:
    i = 0
    while i<5:
        i+=1
        print (i)
    for i in range(10,15):
        print (i)
    return True


new_func3(0)


def new_func4(self, *args):
     r = args[0]
     p = args[1]