def new_list():
    newlist = {
        "first":None,
        "last":None,
        "size":0
    }
    return newlist

def get_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
            raise Exception("IndexError: list index out of range")
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos+=1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count+=1
            
    if not is_in_array:
        count = -1
    return count

def is_empty(my_list):
    return my_list["size"] == 0

def size(my_list):
    return my_list["size"]

def last_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    
    size = size(my_list)
    return get_element(my_list, size-1)

def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception("IndexError: list index out of range")
    
    node = my_list["first"]

    if pos == 0:
        my_list["first"] = node["next"]
        if my_list["first"] is None:
            my_list["last"] = None
        return

    for i in range(pos - 1):
        node = node["next"]

    delete_node = node["next"]
    node["next"] = delete_node["next"]

    # Si borramos el último, actualizar "last"
    if node["next"] is None:
        my_list["last"] = node

def remove_first(my_list):
    delete_element(my_list, 0)

def remove_last(my_list):
    delete_element(my_list, size(my_list)-1)

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    
    new_node = {"info": element,
                "next": None}
    
    if pos == 0:
        new_node["next"] = my_list["first"]
        my_list["first"] = new_node
        if my_list["last"] is None:  # lista estaba vacía
            my_list["last"] = new_node
        my_list["size"] += 1
        return
    
    node = my_list["first"]
    
    for i in range(pos -1):
        node = node["next"]
    
    new_node["next"] = node["next"]
    node["next"] = new_node
    
    if new_node["next"] is None:
        my_list["last"] = new_node
    
    my_list["size"] += 1
    
def change_info(my_list, pos, new_info):
    node = get_element(my_list, pos)
    node["info"] = new_info

def exchange(my_list, pos_1, pos_2):
    if (pos_1 < 0 or pos_1 > size(my_list)) or (pos_2 < 0 or pos_2 > size(my_list)):
            raise Exception('IndexError: one or both list index out of range')
        
    if pos_1 == pos_2:
        return
    
    # Recorremos hasta pos1
    node_1 = my_list["first"]
    for i in range(pos_1):
        node_1 = node_1["next"]
    
    # Recorremos hasta pos2
    node_2 = my_list["first"]
    for i in range(pos_2):
        node_2 = node_2["next"]
    
    # Intercambiamos la info
    node_1["info"], node_2["info"] = node_2["info"], node_1["info"]
    
def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= size(my_list):
        raise Exception("IndexError: list index out of range")
    
    newlist = new_list()
    
    node = my_list["first"]
    for i in range(pos):
        node = node["next"]
    
    count = 0
    while node is not None and count < num_elements:
        
        new_node = {"info": node["info"], "next": None}
        
        if newlist["first"] is None:
            newlist["first"] = new_node
            newlist["last"] = new_node
        else:
            newlist["last"]["next"] = new_node
            newlist["last"] = new_node
        
        newlist["size"] += 1
        node = node["next"]
        count += 1
    
    return newlist
