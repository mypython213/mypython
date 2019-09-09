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



