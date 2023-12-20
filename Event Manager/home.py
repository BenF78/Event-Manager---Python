from customtkinter import * #type: ignore
import sqlite3

class home:
    def __init__(self):
        self.root = CTk()
        self.root.title("Event Manager | Home")
        self.root.geometry("800x600")

    def run(self):
        self.root.mainloop()