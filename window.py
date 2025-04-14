from list_function import append_item, add_value_to_list, remove_item, clear_list, print_grocery_list
import tkinter as tk

class Window:

	def __init__(self, path: str):
		self.path = path

	def create_window(self) -> None:

		window = tk.Tk()
		window.title("Grocery List")
		window.geometry("620x500")

		label = tk.Label(window, text="Grocery List", font=("Victor Mono", 25, "bold", "italic"))
		label.pack(pady=15)

		frame = tk.Frame(window)
		frame.pack(fill="both", expand=True, padx=10, pady=10)

		left_panel = tk.Frame(frame)
		left_panel.pack(side="left", padx=10)

		entry = tk.Entry(frame, width=25)
		entry.pack(side="left", padx=10)


		def add_item():
			grocery_list = add_value_to_list(self.path)
			value = entry.get()

			if value and value not in grocery_list:
				append_item(self.path, value)
				entry.delete(0, tk.END)
			else:
				print(f"The {value} already exists on the list!")
				entry.delete(0, tk.END)


		def re_item():
			grocery_list = add_value_to_list(self.path)
			value = entry.get()

			remove_item(self.path, value)
			entry.delete(0, tk.END)


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

		window.mainloop()
