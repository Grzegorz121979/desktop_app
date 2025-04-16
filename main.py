import csv
import pandas as pd
from window import Window

def main():

    path = "grocery.csv"
    
    window = Window(path)

    window.create_window()
    
if __name__ == "__main__":
    main()
