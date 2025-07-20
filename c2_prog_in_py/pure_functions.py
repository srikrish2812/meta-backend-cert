my_list = [1,2,3]

def pure_f(lst,item):
    nl = lst.copy()
    nl.append(item)
    return nl

print(my_list)
print(pure_f(my_list,4))
