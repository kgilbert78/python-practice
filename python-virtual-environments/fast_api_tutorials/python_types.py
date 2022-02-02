from typing import List, Set, Tuple, Dict, Union, Optional

class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

person1 = Person("Kyle")
print(get_person_name(person1))



def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
        #f is like js template literal: https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
    else:
        print("Hello World!")

say_hi("Kyle")
say_hi()



def process_item_union(item: Union[int, str]):
    print(item)

testing_union1 = "one"
testing_union2 = 1
process_item_union(testing_union1)
process_item_union(testing_union2)



def process_items_dict(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

testing_dict = {
    "ladder": 149.99,
    "headphones": 39.95
}
process_items_dict(testing_dict)



def process_items_tuple_set(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return items_t, items_s

testing_tuple = (1, 2, "three")
testing_set = {b"apple", b"banana", b"cherry"}
process_items_tuple_set(testing_tuple, testing_set)



def process_items_list(items: List[str]):
    for item in items:
        print(item)

testing_list = ["one", "two", "three", "four"]
process_items_list(testing_list)



def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age

def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e

person: str = get_full_name("john", "doe")
print(person)

person_with_age = get_name_with_age(person, 18)
print(person_with_age)

# https://fastapi.tiangolo.com/python-types/