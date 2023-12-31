from customtkinter import * #type: ignore
import sqlite3
import createEvent
import accountView
import viewEventList
from tools import *
import user
from tkinter import messagebox

class home:
    def __init__(self, email):
        self.email = email
        self.root = CTk()
        self.root.title("Event Manager | Home")
        self.root.geometry("1200x800")

        # Create a left frame
        self.leftFrame = CTkFrame(master=self.root, height=600, width=300)
        self.leftFrame.pack(side="left", fill="y")  # Use fill="y" to make the frame expand vertically

        self.navHeading = CTkLabel(master=self.leftFrame, text=f"Logged In As {get_account_name(email)}", font=("Arial", 22, "bold"))
        self.navHeading.pack(side="top", pady=20)

        self.navHomeBtn = CTkLabel(master=self.leftFrame, text="      Home", fg_color="#4f4e4e", compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
        self.navHomeBtn.bind("<Button-1>")
        self.navHomeBtn.pack(pady=10)

        self.navCreateTaskBtn = CTkLabel(master=self.leftFrame, text="      Create Event", compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
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

        self.rightHeading = CTkLabel(master=self.root, text="Event Manager", font=("Arial", 32, "bold"))
        self.rightHeading.pack(pady=40)

        self.notificationsHeading = CTkLabel(master=self.root, text="Your Notifications:", font=("Arial", 20))
        self.notificationsHeading.pack(pady=10)

        self.notificationsFrame = CTkScrollableFrame(master=self.root, scrollbar_button_color="skyblue", orientation="horizontal", width=500)
        self.notificationsFrame.pack(pady=20)

    # These 3 function creates an instance of the classes inside this module so they can be run from here when the user clicks the btn
    # Pass in the email to the class so all details linked to that account can be found
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