from customtkinter import *
import sqlite3
from tools import *
import home

class viewEventList:
    def __init__(self, email) -> None:
        self.email = email
        self.root = CTk()
        self.root.title("Event Manager | View Events")
        self.root.geometry("1000x700")

        self.heading = CTkLabel(master=self.root, text="All Your Events Are Listed Below: ", font=("Arial", 32, "bold"))
        self.heading.pack(pady=40)

        self.eventKey = CTkLabel(master=self.root, text="Name \t\t Due Date", font=("Arial", 24))
        self.eventKey.pack(pady=10)

        allEvents = get_all_user_events(email)

        # If no events are in the db 
        if not allEvents:
            self.noEventsLabel = CTkLabel(master=self.root, text="No Tasks Have Been Found", font=("Arial", 18), text_color="red")
            self.noEventsLabel.pack(pady=20)
        else:
            name = [i[0] for i in allEvents]
            dueDate = [i[2] for i in allEvents]

            self.eventFrame = CTkScrollableFrame(master=self.root, orientation="vertical", scrollbar_button_color="white", width=400, height=400)
            self.eventFrame.pack(expand=True)


            for event in allEvents:
                self.eventBtn = CTkButton(master=self.eventFrame, text=f"{name[0]} : {dueDate[0]}", fg_color="green", hover_color="darkgreen", font=("Arial", 20, "bold"), width=200, height=40)
                self.eventBtn.pack(pady=20)

        self.goBackToHomeBtn = CTkLabel(master=self.root, text="Back To Home", font=("Arial", 16))
        self.goBackToHomeBtn.bind("<Button-1>", lambda event=None : self.callHomeModule())
        self.goBackToHomeBtn.pack(pady=10)

    def callHomeModule(self):
        self.root.withdraw()
        app = home.home(self.email)
        app.run()



    def run(self):
        self.root.mainloop()