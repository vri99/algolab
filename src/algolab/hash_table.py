from math import ceil

from algolab.linked_list import Node

default_load_factor: float = 0.7
type item_tuple_type = tuple[str, int | None]
type item_list_type = list[item_tuple_type | None | Node]

# Init default array with max 10 cells
def init_list(size: int | None = None) -> item_list_type:
    default: item_list_type = [None] * 10

    if size is None:
        return default

    return [None] * size

def calculate_total_items(current_list: item_list_type) -> int:
    # get all elements from the array that is not None
    total_items: list[item_tuple_type] = [i for i in current_list if i is not None]
    # get total number
    total_items_len: int = len(total_items)

    return total_items_len

def resize_list(list_to_resize: item_list_type, n_elements_to_add: int) -> None:
    # To resize a list with limited size we need to calculate
    # load factor = sum of used cells / total list size (n/m)
    current_list_size = len(list_to_resize)
    total_items_len: int = calculate_total_items(list_to_resize)

    # Resize either load factor >= 0.7 or if total of free cells is less than total elements about to add
    current_free_space: int = current_list_size - total_items_len
    load_factor: float = total_items_len / current_list_size

    if load_factor >= default_load_factor or current_free_space < n_elements_to_add:
        # (sum all existing and to add / load factor we want to follow) - current list size
        to_add = ceil((total_items_len + n_elements_to_add) / 0.7) - current_list_size

        list_to_resize += [None] * to_add

    return None

def add_items(list_to_add: item_list_type, items: list[item_tuple_type]) -> None:
    n_elements_to_add: int = len(items)

    # perform resizing before inserting items
    resize_list(list_to_add, n_elements_to_add)

    for item in items:
        # get a hash
        item_hash: int = hash_item(item, len(list_to_add))
        # find it from a list by hash
        current_item: item_tuple_type | None | Node = list_to_add[item_hash]

        # if an item by hash doesn't exist - insert
        if current_item is None:
            list_to_add[item_hash] = item

        if type(current_item) is tuple:
            # if an item exists and value for the same key is different - rewrite
            if current_item[0] == item[0]:
                list_to_add[item_hash] = item
                # else create a new Linked list
            else:
                # head will be previously stored key-value
                new_node: Node = Node(current_item)
                # next node - item we want to add now
                new_node.next = Node(item)

                #put newly created Linked list into a cell
                list_to_add[item_hash] = new_node

        # if an item is a Linked list and value is new - add next Node with new item to it
        # E.g. Linked list: 4 --> 8 --> 3
        # If a new item is 4, then skip it as it already exist
        if type(current_item) is Node:
            if current_item.find(item[0]) is None:
                current_item.append(item)

    return None

def get_item(value: item_tuple_type, items: item_list_type) -> int | None:
    if value is None:
        return None

    # get a hash
    item_hash: int = hash_item(value, len(items))
    current_item: int | Node | None = items[item_hash]

    # if item by hash is Linked list -> search into it
    if type(items[item_hash]) is Node:
        return current_item.find(value[0])
    # else get directly from cell
    return items[item_hash][1]

def hash_func(value: str) -> int:
    result: int = 0

    # for every character of a word get its Unicode
    for char in value:
        result = result * 31 + ord(char)

    return result

def hash_item(value: item_tuple_type, item_list_len: int) -> int:
    # get the right index in the range of a list by its length
    result: int = hash_func(value[0]) % item_list_len

    return result