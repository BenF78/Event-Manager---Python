from customtkinter import *
import sqlite3
from tools import *
import home
from datetime import datetime
import viewEvent
import accountView
import createEvent
import user
import viewEventList
from tkinter import messagebox

class viewEventList:
    def __init__(self, email):
        self.email = email
        self.root = CTk()
        self.root.title("Event Manager | View Events")
        self.root.geometry("1200x700")

        # Create a left frame
        self.leftFrame = CTkFrame(master=self.root, height=600, width=300)
        self.leftFrame.pack(side="left", fill="y")  # Use fill="y" to make the frame expand vertically

        self.navHeading = CTkLabel(master=self.leftFrame, text=f"Logged In As {get_account_name(email)}", font=("Arial", 22, "bold"))
        self.navHeading.pack(side="top", pady=20)

        self.navHomeBtn = CTkLabel(master=self.leftFrame, text="      Home", compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
        self.navHomeBtn.bind("<Button-1>", lambda e=None: self.callHomeModule())
        self.navHomeBtn.pack(pady=10)

        self.navCreateTaskBtn = CTkLabel(master=self.leftFrame, text="      Create Event", compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
        self.navCreateTaskBtn.bind("<Button-1>", lambda e=None : self.callCreateEventModule())
        self.navCreateTaskBtn.pack(pady=10)

        self.navViewAllEvents = CTkLabel(master=self.leftFrame, text="      View All Events", fg_color="#4f4e4e",compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
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

        self.heading = CTkLabel(master=self.root, text="All Your Events With The Due Dates Are Listed Below: ", font=("Arial", 32, "bold"))
        self.heading.pack(pady=20)

        self.label = CTkLabel(master=self.root, text="Simply Click On The Button To View The Task", font=("Arial", 18))
        self.label.pack(pady=10)

        allEvents = get_all_user_events(email)

        # If no events are in the db show a label to tell the user they have no events
        if not allEvents:
            self.noEventsLabel = CTkLabel(master=self.root, text="No Events Have Been Found", font=("Arial", 18), text_color="red")
            self.noEventsLabel.pack(pady=20)
        else:
            self.eventFrame = CTkScrollableFrame(master=self.root, orientation="vertical", scrollbar_button_color="white", width=500, height=400)
            self.eventFrame.pack(expand=True)

            currentDate = datetime.now().date()
            currentDate = datetime.now().strftime("%Y/%m/%d").replace("/", "")
            currentDate = int(currentDate)

            for data in allEvents:
                eventName, dueDate = data

                # Convert to string to replace the dashes with slashes
                formattedDueDate = str(dueDate).replace("-", "/")

                viewTaskBtn = CTkButton(master=self.eventFrame, width=400, height=30, font=("Arial", 18, "bold"), command=lambda n=eventName : self.callViewEventModule(n))
                viewTaskBtn.pack(pady=20)

                dueDate = formattedDueDate.replace("/", "")
                dueDate = int(dueDate)
                
                # larger number = future
                # smaller number = past

                if dueDate > currentDate:
                    viewTaskBtn.configure(fg_color="green", hover_color="darkgreen", text=f"{eventName}\n\n{formattedDueDate} (Not Due Yet)")
                elif dueDate < currentDate:
                    viewTaskBtn.configure(fg_color="red", hover_color="#9e1919", text=f"{eventName}\n\n{formattedDueDate} (Past Due)")
                elif dueDate == currentDate:
                    viewTaskBtn.configure(fg_color="orange", hover_color="#c2810a", text=f"{eventName}\n\n{formattedDueDate} (Due Today)")

    def callViewEventModule(self, eventName):
        self.root.withdraw()
        app = viewEvent.viewEvent(self.email, eventName)
        app.run()

    def callHomeModule(self):
        self.root.withdraw()
        app = home.home(self.email)
        app.run()

    def callAccoutModule(self):
        self.root.withdraw()
        app = accountView.accountView(self.email)
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
        self.root.mainloop()