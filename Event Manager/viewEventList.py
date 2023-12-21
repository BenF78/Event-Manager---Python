from customtkinter import *
import sqlite3
from tools import *
import home
from datetime import datetime
import viewEvent

class viewEventList:
    def __init__(self, email):
        self.email = email
        self.root = CTk()
        self.root.title("Event Manager | View Events")
        self.root.geometry("1000x700")

        self.heading = CTkLabel(master=self.root, text="All Your Events With The Due Dates Are Listed Below: ", font=("Arial", 32, "bold"))
        self.heading.pack(pady=20)

        self.label = CTkLabel(master=self.root, text="Simply Click On The Button To View The Task", font=("Arial", 18))
        self.label.pack(pady=10)

        allEvents = get_all_user_events(email)

        # If no events are in the db show a label to tell the user they have no events
        if not allEvents:
            self.noEventsLabel = CTkLabel(master=self.root, text="No Tasks Have Been Found", font=("Arial", 18), text_color="red")
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

                viewTaskBtn = CTkButton(master=self.eventFrame, width=400, height=30, font=("Arial", 18, "bold"), command=lambda t=eventName : self.callViewEventModule(t))
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

        self.goBackToHomeBtn = CTkLabel(master=self.root, text="Back To Home", font=("Arial", 16))
        self.goBackToHomeBtn.bind("<Button-1>", lambda event=None : self.callHomeModule())
        self.goBackToHomeBtn.pack(pady=10)

    def callViewEventModule(self, eventName):
        self.root.withdraw()
        app = viewEvent.viewEvent(self.email, eventName)
        app.run()

    def callHomeModule(self):
        self.root.withdraw()
        app = home.home(self.email)
        app.run()



    def run(self):
        self.root.mainloop()