from window import Window
# from list_function import append_item, remove_item, clear_list, print_grocery_list, add_value_to_list

def main():

    path = "todo.txt";
    
    window = Window(path)

    window.create_window()

    # print("Grocery List")

    # answer = input("Do you want add item (a), remove item (r), clear list (c), print list (p) or exit (e)?: ").lower().strip()

    # while True:
    #     if answer == "a".lower():
    #         user_input = input("Enter new item: ").strip()
    #         append_item(path, user_input)
    #         answer = input("Do you want add item (a), remove item (r), clear list (c), print list (p) or exit (e)?: ").lower().strip()
    #     elif answer == "p".lower():
    #         grocery_list = add_value_to_list(path)
    #         print_grocery_list(grocery_list)
    #         answer = input("Do you want add item (a), remove item (r), clear list (c), print list (p) or exit (e)?: ").lower().strip()
    #     elif answer == "r".lower():
    #         user_input = input("Enter new item: ").strip()
    #         remove_item(path, user_input)
    #         answer = input("Do you want add item (a), remove item (r), clear list (c), print list (p) or exit (e)?: ").lower().strip()
    #     elif answer == "c".lower():
    #         clear_list(path)
    #         print("List clear")
    #         answer = input("Do you want add item (a), remove item (r), clear list (c), print list (p) or exit (e)?: ").lower().strip()
    #     else:
    #         print("Goodbye")
    #         break


if __name__ == "__main__":
    main()
