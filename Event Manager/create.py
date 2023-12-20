from customtkinter import * #type: ignore
import sqlite3
from tools import *
from tkinter import messagebox

class create():
    def __init__(self, email):
        self.root = CTk()
        self.root.title("Event Manager | Create")
        self.root.geometry("800x600")
        self.email = email


        self.enterName = CTkEntry(master=self.root, placeholder_text="Event Name", width=240)
        self.enterName.pack(pady=10, padx=50)

        self.enterDescription = CTkEntry(master=self.root, placeholder_text="Event Description", width=240)
        self.enterDescription.pack(pady=10, padx=50)

        self.enterDate = CTkEntry(master=self.root, placeholder_text="Event Date", width=240)
        self.enterDate.pack(pady=10, padx=50)

        self.createBtn = CTkButton(master=self.root, text="Create Event", fg_color="green", hover_color="darkgreen", corner_radius=32, command=self.storeDetailsInDb)
        self.createBtn.pack(pady=10, padx=50)



        





        def run(self):
            self.root.mainloop()
            