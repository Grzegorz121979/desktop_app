import tkinter as tk

def create_window() -> None:

	window = tk.Tk()
	window.title("Grocery List")
	window.geometry("520x400")

	label = tk.Label(window, text="Grocery List", font=("Consolas", 25, "bold", "italic"))
	label.pack(pady=15)

	frame = tk.Frame(window)
	frame.pack(fill="both", expand=True, padx=10, pady=10)

	left_panel = tk.Frame(frame)
	left_panel.pack(side="left", padx=10)

	label = tk.Label(window, text="Grocery List", font=("Consolas", 25, "bold", "italic"))
	label.pack(pady=15)

	button_width = 20
	button_height = 2

	button_text = ["Add Item", "Remove Item", "Clear Item", "Print List"]

	for text in button_text:
		button = tk.Button(left_panel, text=text, 
									width=button_width, 
									height=button_height, 
									font=("Consolas", 13, "bold", "italic"), 
									bd=5, 
									relief="groove",)
		button.pack(pady=5)

	text_area = tk.Text(frame, width=50, height=10)
	text_area.pack(side="left", padx=10)

	window.mainloop()
