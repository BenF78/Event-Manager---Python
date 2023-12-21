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
                        dueDate TEXT,
                        completed BOOLEAN
                    )
                """)        
            
        self.heading = CTkLabel(master=self.root, text="Create Event", font=("Arial", 30, "bold"))
        self.heading.pack(pady=20)

        self.eventNameLabel = CTkLabel(master=self.root, text="Event Name:", font=("Arial", 18))
        self.eventNameLabel.pack(pady=10)
        self.eventNameInput = CTkEntry(master=self.root, width=200, border_color="white", border_width=1)
        self.eventNameInput.pack(pady=10)

        self.eventDescLabel = CTkLabel(master=self.root, text="Event Description:", font=("Arial", 18))
        self.eventDescLabel.pack(pady=10)
        self.eventDescInput = CTkTextbox(master=self.root, scrollbar_button_color="white", width=500, height=250, border_color="white", border_width=1)
        self.eventDescInput.pack(pady=10)

        self.eventDueDateLabel = CTkLabel(master=self.root, text="Event Due Date (DD/MM/YYYY):", font=("Arial", 18))
        self.eventDueDateLabel.pack(pady=10)
        self.eventDueDateInput = CTkEntry(master=self.root, width=100, border_color="white", border_width=1)
        self.eventDueDateInput.pack(pady=10)

        self.createEventBtn = CTkButton(master=self.root, text="Create Event", fg_color="green", hover_color="darkgreen", command=self.createEvent)
        self.createEventBtn.pack(pady=10)

        self.goBackToHomeBtn = CTkLabel(master=self.root, text="Back To Home", font=("Arial", 16))
        # Bind the label to a button so a command can be run when it is clicked
        self.goBackToHomeBtn.bind("<Button-1>", lambda event=None : self.callHomeModule())
        self.goBackToHomeBtn.pack(pady=10)

    def createEvent(self):
        # get the event info and remove white space
        eventName = self.eventNameInput.get().strip()
        # start at index 0 and go to the end 
        eventDesc = self.eventDescInput.get("0.0", "end")
        eventDueDateStr = self.eventDueDateInput.get().strip()

        # Validate the info entered
        if eventName == "" or eventDesc == "" or eventDueDateStr == "":
            messagebox.showerror(title="Fields Left Blank", message="Fields Cannot Be Left Blank.")
        elif event_name_exists(self.email, eventName):
            messagebox.showerror(title="Event Exists", message=f"An Event With The Name {eventName} Already Exists..")
        else:
            try:
                # Convert the input due date string to a datetime object
                eventDueDate = datetime.strptime(eventDueDateStr, "%d/%m/%Y").date()
            except ValueError:
                # If the data is in an unexpected format then raise an error and inform the user
                messagebox.showerror(title="Invalid Date Format", message="Please enter a valid date format.")
            else:
                # If everything is valid insert the event details into the table with the logged in email as key
                with sqlite3.connect("database.db") as conn:
                    c = conn.cursor()

                    c.execute("INSERT INTO events VALUES(?,?,?,?,?)", (self.email, eventName, eventDesc, eventDueDate, False))   

                messagebox.showinfo(title="Event Created", message=f"{eventName} Event Has Been Created.")  
                self.callHomeModule()

    def callHomeModule(self):
        # Withdraw the root and return to the home page when the btn clicked or an event is made
        self.root.withdraw()
        app = home.home(self.email)
        app.run()

    def run(self):
        self.root.mainloop()
            