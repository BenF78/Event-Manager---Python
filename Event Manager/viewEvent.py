from customtkinter import *
import home
import sqlite3
from tools import *
from tkinter import messagebox
from datetime import datetime


class viewEvent:
    def __init__(self, email, clickedEventName):
        self.email = email
        self.clickedEventName = clickedEventName

        self.root = CTk()
        self.root.geometry("800x700")
        self.root.title("Event Manager | View Event")

        self.heading = CTkLabel(master=self.root, text="Viewing Event", font=("Arial", 32, "bold"))
        self.heading.pack(pady=20)

        self.eventNameLabel = CTkLabel(master=self.root, text=f"Event Name", font=("Arial", 18))
        self.eventNameLabel.pack(pady=10)
        self.eventNameInput = CTkEntry(master=self.root, border_color="white", border_width=1)
        self.eventNameInput.insert(END, self.clickedEventName)
        self.eventNameInput.pack(pady=10)

        self.eventDescriptionLabel = CTkLabel(master=self.root, text=f"Event Description", font=("Arial", 18))
        self.eventDescriptionLabel.pack(pady=10)
        self.eventDescriptionInput = CTkTextbox(master=self.root, border_color="white", border_width=1, scrollbar_button_color="white", width=500, height=250)
        self.eventDescriptionInput.insert(END, get_event_description(self.email, self.clickedEventName))
        self.eventDescriptionInput.pack(pady=10)

        self.eventDueDateLabel = CTkLabel(master=self.root, text=f"Event Due Date", font=("Arial", 18))
        self.eventDueDateLabel.pack(pady=10)
        self.eventDueDateInput = CTkEntry(master=self.root, border_color="white", border_width=1)
        self.eventDueDateInput.insert(END, get_event_due_date(self.email, self.clickedEventName))
        self.eventDueDateInput.pack(pady=10)

        self.saveEventBtn = CTkButton(master=self.root, text="Save Changes", command=self.saveChanges)
        self.saveEventBtn.pack(pady=10)

        self.markEventAsDoneBtn = CTkButton(master=self.root, text="Mark As Done", fg_color="green", hover_color="darkgreen", command=self.markEventAsDone)
        self.markEventAsDoneBtn.pack(pady=10)

        self.deleteEventBtn = CTkButton(master=self.root, text="Delete Event", fg_color="red", command=self.deleteEvent)
        self.deleteEventBtn.pack(pady=10)

    def saveChanges(self):
        eventName = self.eventNameInput.get().strip()
        eventDesc = self.eventDescriptionInput.get("0.0", "end")
        eventDueDate = self.eventDueDateInput.get().strip()

        if eventName == "" or eventDesc == "" or eventDueDate == "":
            messagebox.showerror(title="Fields Left Blank", message="Fields Cannot Be Left Blank.")
        elif event_name_exists(self.email, eventName):
            messagebox.showerror(title="Event Exists", message=f"An Event With The Name {eventName} Already Exists..")
        else:
            try:
                # Convert the input due date string to a datetime object
                eventDueDate = datetime.strptime(eventDueDate, "%d/%m/%Y").date()
            except ValueError:
                # If the data is in an unexpected format then raise an error and inform the user
                messagebox.showerror(title="Invalid Date Format", message="Please enter a valid date format.")
            else:
                # If everything is valid insert the event details into the table with the logged in email as key
                with sqlite3.connect("database.db") as conn:
                    c = conn.cursor()

                    c.execute("UPDATE events SET name=?,description=?,dueDate=? WHERE email=? AND name=?", (eventName, eventDesc, eventDueDate, self.email, self.clickedEventName))   

                messagebox.showinfo(title="Event Updated", message=f"{eventName} Event Has Been Updated.")  
                self.callHomeModule()

    def deleteEvent(self):
        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()

            c.execute("DELETE FROM events WHERE name=? AND email=?", (self.clickedEventName, self.email))

        messagebox.showinfo(title="Event Deleted", message=f"The Event With The Name {self.clickedEventName} Has Been Deleted")

        self.callHomeModule()

    def markEventAsDone(self):
        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()

            c.execute("UPDATE events SET completed=? WHERE email=? AND name=?", (True, self.email, self.clickedEventName))

        messagebox.showinfo(title="Event Completed", message=F"The Event With The Name {self.clickedEventName} Has Been Completed.")


    def callHomeModule(self):
        self.root.withdraw()
        app = home.home(self.email)
        app.run()

        

    def run(self):
        pass