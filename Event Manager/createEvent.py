from customtkinter import * #type: ignore
import sqlite3
from tools import *
from tkinter import messagebox
from datetime import *
import home

class create:
    def __init__(self, email):
        self.root = CTk()
        self.root.title("Event Manager | Create")
        self.root.geometry("1000x700")
        self.email = email

        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS events(
                        email TEXT,
                        name TEXT,
                        description TEXT,
                        dueDate TEXT
                    )
                """)        
            
        self.heading = CTkLabel(master=self.root, text="Create Event", font=("Arial", 30, "bold"))
        self.heading.pack(pady=20)

        self.eventNameLabel = CTkLabel(master=self.root, text="Event Name:", font=("Arial", 18))
        self.eventNameLabel.pack(pady=10)
        self.eventNameInput = CTkEntry(master=self.root, width=200)
        self.eventNameInput.pack(pady=10)

        self.eventDescLabel = CTkLabel(master=self.root, text="Event Description:", font=("Arial", 18))
        self.eventDescLabel.pack(pady=10)
        self.eventDescInput = CTkTextbox(master=self.root, scrollbar_button_color="white", width=500, height=250)
        self.eventDescInput.pack(pady=10)

        self.eventDueDateLabel = CTkLabel(master=self.root, text="Event Due Date (DD/MM/YYYY):", font=("Arial", 18))
        self.eventDueDateLabel.pack(pady=10)
        self.eventDueDateInput = CTkEntry(master=self.root, width=100)
        self.eventDueDateInput.pack(pady=10)

        self.createEventBtn = CTkButton(master=self.root, text="Create Event", fg_color="green", hover_color="darkgreen", command=self.createEvent)
        self.createEventBtn.pack(pady=10)

        self.goBackToHomeBtn = CTkLabel(master=self.root, text="Back To Home", font=("Arial", 16))
        self.goBackToHomeBtn.bind("<Button-1>", lambda event=None : self.callHomeModule())
        self.goBackToHomeBtn.pack(pady=10)

    def createEvent(self):
        eventName = self.eventNameInput.get().strip()
        eventDesc = self.eventDescInput.get("0.0", "end")
        eventDueDateStr = self.eventDueDateInput.get().strip()

        if eventName == "" or eventDesc == "" or eventDueDateStr == "":
            messagebox.showerror(title="Fields Left Blank", message="Fields Cannot Be Left Blank.")
        elif event_name_exists(self.email, eventName):
            messagebox.showerror(title="Event Exists", message=f"An Event With The Name {eventName} Already Exists..")
        else:
            try:
                # Convert the input due date string to a datetime object
                eventDueDate = datetime.strptime(eventDueDateStr, "%d/%m/%Y").date()
            except ValueError:
                messagebox.showerror(title="Invalid Date Format", message="Please enter a valid date format.")
            else:
                with sqlite3.connect("database.db") as conn:
                    c = conn.cursor()

                    c.execute("INSERT INTO events VALUES(?,?,?,?)", (self.email, eventName, eventDesc, eventDueDate))   

                messagebox.showinfo(title="Event Created", message=f"{eventName} Event Has Been Created.")  
                self.callHomeModule()

    def callHomeModule(self):
        self.root.withdraw()
        app = home.home(self.email)
        app.run()

    def run(self):
        self.root.mainloop()
            