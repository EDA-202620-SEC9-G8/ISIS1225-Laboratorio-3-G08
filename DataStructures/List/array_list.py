
from DataStructures.List import array_list as al
def new_list():
    newlist = {
        "elements": [],
        "size": 0
    }
    return newlist
def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1
def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list
def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list
def size(my_list):
    return my_list["size"]
def first_element(my_list):
    return my_list["elements"][0]
def last_element(my_list):
    return my_list["elements"][my_list["size"] - 1]
def is_empty(my_list):
    return my_list["size"] == 0
def get_elements(my_list, pos):
    return my_list["elements"][pos]      
def delete_element(my_list, pos):
    del my_list["elements"][pos]
    my_list["size"] -= 1
    return my_list
def remove_first(my_list):
    if my_list["size"] == 0 or not my_list["elements"]:
        return None
    elemento_eliminado = my_list["elements"].pop(0)
    my_list["size"] -= 1
    return elemento_eliminado
def remove_last(my_list):
    if my_list["size"] == 0 or not my_list["elements"]:
        return None
    elemento_eliminado = my_list["elements"].pop()
    my_list["size"] -= 1
    return elemento_eliminado
def insert_element(my_list, pos, element):
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list
def change_info(my_list, pos, element):
    my_list["elements"][pos] = element
    return my_list
def exchange(my_list, pos1, pos2):
    my_list["elements"][pos1], my_list["elements"][pos2] = my_list["elements"][pos2], my_list["elements"][pos1]
    return my_list
def sub_list(my_list, pos1, pos2):
    sublist = new_list()
    for i in range(pos1, pos2 + 1):
        add_last(sublist, get_element(my_list, i))
    return sublist

