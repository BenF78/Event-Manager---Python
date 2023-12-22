from customtkinter import * #type: ignore
import sqlite3
from tools import *
from tkinter import messagebox
from datetime import *
import home
import accountView
import createEvent
import user
import viewEventList

class create:
    def __init__(self, email):
        self.root = CTk()
        self.root.title("Event Manager | Create")
        self.root.geometry("1200x800")
        self.email = email

        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()
            # Integar due date to order the due date numerically
            c.execute("""CREATE TABLE IF NOT EXISTS events(
                        email TEXT,
                        name TEXT,
                        description TEXT,
                        dueDate TEXT,
                        intDueDate INTEGAR, 
                        completed BOOLEAN
                    )
                """)        
            
        # Create a left frame
        self.leftFrame = CTkFrame(master=self.root, height=600, width=300)
        self.leftFrame.pack(side="left", fill="y")  # Use fill="y" to make the frame expand vertically

        self.navHeading = CTkLabel(master=self.leftFrame, text=f"Logged In As {get_account_name(email)}", font=("Arial", 22, "bold"))
        self.navHeading.pack(side="top", pady=20)

        self.navHomeBtn = CTkLabel(master=self.leftFrame, text="      Home", compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
        self.navHomeBtn.bind("<Button-1>", lambda e=None: self.callHomeModule())
        self.navHomeBtn.pack(pady=10)

        self.navCreateTaskBtn = CTkLabel(master=self.leftFrame, text="      Create Event", fg_color="#4f4e4e", compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
        self.navCreateTaskBtn.bind("<Button-1>", lambda e=None : self.callCreateEventModule())
        self.navCreateTaskBtn.pack(pady=10)

        self.navViewAllEvents = CTkLabel(master=self.leftFrame, text="      View All Events", compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
        self.navViewAllEvents.bind("<Button-1>", lambda e=None : self.callViewEventModule())
        self.navViewAllEvents.pack(pady=10)

        self.navViewPendingTasksBtn = CTkLabel(master=self.leftFrame, text="      View Pending Events", compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
        self.navViewPendingTasksBtn.bind("<Button-1>", lambda e=None:  None)
        self.navViewPendingTasksBtn.pack(pady=10)

        self.navViewCompletedTasksBtn = CTkLabel(master=self.leftFrame, text="      View Completed Events", compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
        self.navViewCompletedTasksBtn.bind("<Button-1>", lambda e=None : print("View Completed Events clicked"))
        self.navViewCompletedTasksBtn.pack(pady=10)

        self.navViewAccountBtn = CTkLabel(master=self.leftFrame, text="      Account Details", compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
        self.navViewAccountBtn.bind("<Button-1>", lambda e=None : self.callAccoutModule())
        self.navViewAccountBtn.pack(pady=10)

        self.navSignOutBtn = CTkButton(master=self.leftFrame, text=" Sign Out", font=("Arial", 18, "bold"), command=lambda e=None: sign_out(self.email) + self.callUserModule(), width=250, height=40)
        self.navSignOutBtn.pack(pady=10)
            
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
                eventDueDate = eventDueDate.strftime("%d/%m/%Y")
                intDueDate = int(eventDueDate.replace("/", ""))
                with sqlite3.connect("database.db") as conn:
                    c = conn.cursor()

                    c.execute("INSERT INTO events VALUES(?,?,?,?,?,?)", (self.email, eventName, eventDesc, eventDueDate, intDueDate, False))   

                messagebox.showinfo(title="Event Created", message=f"{eventName} Event Has Been Created.")  
                self.callViewEventModule()

    def callHomeModule(self):
        # Withdraw the root and return to the home page when the btn clicked or an event is made
        self.root.withdraw()
        app = home.home(self.email)
        app.run()

    def callAccoutModule(self):
        self.root.withdraw()
        app = accountView.accountView(self.email)
        app.run()

    def callViewEventModule(self):
        self.root.withdraw()
        app = viewEventList.viewEventList(self.email)
        app.run()

    def callCreateEventModule(self):
        self.root.withdraw()
        app = createEvent.create(self.email)
        app.run()        

    def callUserModule(self):
        messagebox.showinfo(title="Signed Out", message=f"You Have Been Signed Out {get_account_name(self.email)}")
        self.root.withdraw()
        app = user.login()
        app.run()

    def run(self):
        # self.root.attributes("-fullscreen", True)
        self.root.mainloop()
            