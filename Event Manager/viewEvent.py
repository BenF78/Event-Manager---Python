from customtkinter import *
import home
import sqlite3
from tools import *


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

        self.saveEventBtn = CTkButton(master=self.root, text="Save Changes")
        self.saveEventBtn.pack(pady=10)
        

    def run(self):
        pass