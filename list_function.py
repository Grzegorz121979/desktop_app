import csv
import pandas as pd

def open_csv(path: str) -> list[dict[str, int]] | None:
    """
    Function open csv file and adding values to list of dictionary.
    :param path: str
    return: list[dict[str, int]]
    """
    grocery_list = []
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row["product"]
            quantity = int(row["quantity"])
            grocery_list.append({"product": product, "quantity": quantity})

    return grocery_list


def save_value_to_csv(path: str, grocery: list[dict[str, int]]) -> None:
    df = pd.DataFrame(grocery)
    df.to_csv(path, index=False, encoding="utf-8")


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

