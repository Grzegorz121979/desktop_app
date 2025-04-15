import csv

def open_csv(path: str) -> list[dict[str, int]] | None:
    """
    Function open csv file and adding values to list of dictionary.
    :param path: str
    return: list[dict[str, int]]
    """
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        grocery_list = [dict(row) for row in reader]

    return grocery_list


def add_value_to_list(path: str) -> list[str] | None:
    """
    Function add value from txt file to list
    :param path: str
    :return: list[str]
    """
    with open(path, "r", encoding="utf-8") as f:
        grocery_list = [line.strip() for line in f]

    return grocery_list


def append_item(path: str, user_input: str) -> None:
    """
    Function adding new elemet to the list
    :param user_input: str
    :path: str
    """
    grocery_list = add_value_to_list(path)

    if user_input in grocery_list:
        print("This element is on the grocery list")
    else:
        grocery_list.append(user_input)

    with open(path, "w", encoding="utf-8") as f:
        for item in grocery_list:
            f.write(item + "\n")


def remove_item(path: str, user_input: str) -> None:
    """
    Function removing elemet to the list
    :param user_input: str
    :path: str
    """
    grocery_list = add_value_to_list(path)

    if user_input in grocery_list:
        grocery_list.remove(user_input)
    else:
        print("There is no such element is on the grocery list")

    with open(path, "w", encoding="utf-8") as f:
        for item in grocery_list:
            f.write(item + "\n")


def clear_list(path: str) -> None:
    """
    Function clear the elemets of the list
    :path: str
    """
    grocery_list = add_value_to_list(path)

    grocery_list.clear()

    with open(path, "w", encoding="utf-8") as f:
        for item in grocery_list:
            f.write(item + "\n")


def print_grocery_list(grocery_list: list[str]) -> None:
    """
    Function ptint list of elements
    :param grocery_list: list[str]
    """
    for el in grocery_list:
        print(el)

