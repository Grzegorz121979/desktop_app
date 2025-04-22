import csv
import pandas as pd
from list_function import remove_item, clear_list, print_grocery_list, open_csv, save_value_to_csv
import tkinter as tk


def main():

    path = "grocery.csv"

    def closed_win():
        window.destroy()

    def closed():
        root = tk.Toplevel(window)
        root.title("Exit")
        root.geometry("220x140")
        root.configure(bg="lightblue")
        root.resizable(False, False)

        label = tk.Label(root, 
                        text="Do you want exit?", 
                        font=("Victor Mono", 16, "bold", "italic"), 
                        bg="lightblue")
        label.pack(pady=20)

        yes_button = tk.Button(root, 
                                text="Ok", 
                                width=8, 
                                height=1, 
                                font=("Victor Mono", 13, "bold", "italic"),
                                command=closed_win)
        yes_button.pack(padx=10, pady=5)

        root.mainloop()

    window = tk.Tk()
    window.title("Grocery List")
    window.geometry("620x500")
    window.configure(bg="lightblue")
    window.resizable(False, False)

    label = tk.Label(window, text="Grocery List", font=("Victor Mono", 25, "bold", "italic"), bg="lightblue")
    label.pack(pady=15)

    frame = tk.Frame(window, bg="lightblue")
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    left_panel = tk.Frame(frame, bg="lightblue")
    left_panel.pack(side="left", padx=10)

        
    def add_item() -> None:
        grocery_list = open_csv(path)
        value = entry.get()
        item = any(product["product"] == value for product in grocery_list)
        if item:
            index = next(index for index, product in enumerate(grocery_list) if product["product"] == value)
            grocery_list[index]["quantity"] += 1
            entry.delete(0, tk.END)
            save_value_to_csv(path, grocery_list)
            print_item()
        else:
            grocery_list.append(dict(product=value, quantity=1))
            entry.delete(0, tk.END)
            save_value_to_csv(path, grocery_list)
            print_item()


    def re_item():
        grocery_list = add_value_to_list(path)
        value = entry.get()

        remove_item(path, value)
        entry.delete(0, tk.END)

        print_item()


    def print_item():
        text_area.delete("1.0", tk.END)
        grocery_list = open_csv(path)

        if len(grocery_list) == 0:
            text_area.insert(tk.END, "The grocery list is empty!")
        else:
            for row in grocery_list:
                text_area.insert(tk.END, f"{row["product"]}: {row["quantity"]}" + "\n")


    def clear_item():
        text_area.delete("1.0", tk.END)
        clear_list(path)


    add_button = tk.Button(left_panel, 
                            text="Add Item", 
                            width=20, 
                            height=1, 
                            font=("Victor Mono", 13, "bold", "italic"), 
                            bd=5, 
                            relief="groove",
                            command=add_item)
    add_button.pack(pady=10)

    clear_button = tk.Button(left_panel, 
                            text="Remove Item", 
                            width=20, 
                            height=1, 
                            font=("Victor Mono", 13, "bold", "italic"), 
                            bd=5, 
                            relief="groove",
                            command=re_item)
    clear_button.pack(pady=10)

    print_button = tk.Button(left_panel, 
                            text="Print List", 
                            width=20, 
                            height=1, 
                            font=("Victor Mono", 13, "bold", "italic"), 
                            bd=5, 
                            relief="groove",
                            command=print_item)
    print_button.pack(pady=10)

    clear_button = tk.Button(left_panel, 
                            text="Clear List", 
                            width=20, 
                            height=1, 
                            font=("Victor Mono", 13, "bold", "italic"), 
                            bd=5, 
                            relief="groove",
                            command=clear_item)
    clear_button.pack(pady=10)

    exit_button = tk.Button(left_panel, 
                            text="Exit", 
                            width=20, 
                            height=1, 
                            font=("Victor Mono", 13, "bold", "italic"), 
                            bd=5, 
                            relief="groove", command=closed)
    exit_button.pack(pady=10)

    right_panel = tk.Frame(frame, bg="lightblue")
    right_panel.pack(side="left", padx=20)

    entry = tk.Entry(right_panel, width=50, font=("Victor Mono", 13, "bold", "italic"))
    entry.pack(padx=10, pady=(0, 10), ipady=10)

    text_area = tk.Text(right_panel, width=50, height=11, font=("Victor Mono", 13, "bold", "italic"))
    text_area.pack(padx=10)

    window.mainloop()

if __name__ == "__main__":
    main()
