#1
a_str = "Hello"
#2
b_int = 5
#3
c_float = 5.5
#4
d_bytes = b"Hello"
#5
e_list = [6, "Tanya", 3.2]
#6
f_tuple = ("pop", 7, 49.3)
#7
g_set = {"banana","hello"}
#8
h_frozenset = frozenset ({"apple", "pop"})
#9
j_dict ={"name" :"Tanya", "age" : 36}
#10
print(a_str, type(a_str))
print(b_int, type(b_int))
print(c_float, type(c_float))
print(d_bytes, type(d_bytes))
print(e_list, type(e_list))
print(f_tuple, type(f_tuple))
print(g_set, type(g_set))
print(h_frozenset, type(h_frozenset))
print(j_dict, type(j_dict))
#11
name_1, name_2 = "Tanya", "Hello"
name_3 = name_1 + name_2
print(name_3)
#12
name_4, name_5 = 6, 4
name_6 = name_4 + name_5
print("name_6 = ", name_6)
#13
name_7 = name_4 / name_5
print("name_7 = ", name_7)
#14
name_8 = name_4 * name_5
print("name_8 = ", name_8)
#15
name_9 = name_4 // name_5
print("name_9 = ",name_9)
#16
name_10 = name_4 % name_5
print("name_10 = ", name_10)