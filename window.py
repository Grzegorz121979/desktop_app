import tkinter as tk

def create_window() -> None:

	window = tk.Tk()
	window.geometry("520x400")
	window.title("Grocery List")

	label = tk.Label(window, text="Grocery List", font=("Consolas", 25, "bold", "italic"))
	label.pack(pady=15)

	button_width = 20
	button_height = 2

	button_text = ["Add Item", "Remove Item", "Clear Item", "Print List"]

	for text in button_text:
		button = tk.Button(window, text=text, 
									width=button_width, 
									height=button_height, 
									font=("Consolas", 13, "bold", "italic"), 
									bd=5, 
									relief="groove",)
		button.pack(anchor="w", padx=10, pady=5)

	window.mainloop()
