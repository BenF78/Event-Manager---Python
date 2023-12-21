from customtkinter import * #type: ignore
import sqlite3
import createEvent
import accountView
import viewEventList

class home:
    def __init__(self, email):
        self.email = email
        self.root = CTk()
        self.root.title("Event Manager | Home")
        self.root.geometry("1000x700")

        self.heading = CTkLabel(master=self.root, text="Home", font=("Arial", 36, "bold"))
        self.heading.pack(pady=20)

        self.selectLabel = CTkLabel(master=self.root, text=f"Hello {self.getAccountName()}, Select An Option From Below:", font=("Arial", 24))
        self.selectLabel.pack(pady=20)

        self.createEventBtn = CTkButton(master=self.root, text="Create Event", corner_radius=32, hover_color="darkgreen", width=250, height=40, fg_color="green", font=("Arial", 20, "bold"),command=lambda event=None: self.callCreateEventClass())
        self.createEventBtn.pack(pady=10)

        self.viewEventsBtn = CTkButton(master=self.root, text="View Events", corner_radius=32, hover_color="darkgreen", width=250, height=40, fg_color="green", font=("Arial", 20, "bold"), command=self.callViewEventModule)
        self.viewEventsBtn.pack(pady=10)

        self.viewProfileBtn = CTkButton(master=self.root, text="View Account Details", corner_radius=32, hover_color="darkgreen", width=250, height=40, fg_color="green", font=("Arial", 20, "bold"), command=lambda event=None: self.callAccoutModule())
        self.viewProfileBtn.pack(pady=10)

        self.notificationLabel = CTkLabel(master=self.root, text="Your Notifications:", font=("Arial", 24, "bold"))
        self.notificationLabel.pack(pady=40)

        self.noficationFrame = CTkScrollableFrame(master=self.root, orientation="horizontal", scrollbar_button_color="black", width=800)
        self.noficationFrame.pack()

        self.testNotification = CTkButton(master=self.noficationFrame, text="Event due today", height=200)
        self.testNotification.pack(pady=10, padx=10, side="left")
        self.testNotification = CTkButton(master=self.noficationFrame, text="Event due today", height=200)
        self.testNotification.pack(pady=10, padx=10, side="left")
        self.testNotification = CTkButton(master=self.noficationFrame, text="Event due today", height=200)
        self.testNotification.pack(pady=10, padx=10, side="left")
        self.testNotification = CTkButton(master=self.noficationFrame, text="Event due today", height=200)
        self.testNotification.pack(pady=10, padx=10, side="left")
        self.testNotification = CTkButton(master=self.noficationFrame, text="Event due today", height=200)
        self.testNotification.pack(pady=10, padx=10, side="left")
        self.testNotification = CTkButton(master=self.noficationFrame, text="Event due today", height=200)
        self.testNotification.pack(pady=10, padx=10, side="left")
        self.testNotification = CTkButton(master=self.noficationFrame, text="Event due today", height=200)
        self.testNotification.pack(pady=10, padx=10, side="left")
        self.testNotification = CTkButton(master=self.noficationFrame, text="Event due today", height=200)
        self.testNotification.pack(pady=10, padx=10, side="left")
        
        

    def callAccoutModule(self):
        self.root.withdraw()
        app = accountView.accountView(self.email)
        app.run()

    def callViewEventModule(self):
        self.root.withdraw()
        app = viewEventList.viewEventList(self.email)
        app.run()
        
    
    def getAccountName(self):
        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()

            c.execute("SELECT name FROM users WHERE email=?", (self.email,))
            name = c.fetchall()

            for t in name:
                for l in t:
                    name = l
                    return name
                
    def callCreateEventClass(self):
        self.root.withdraw()
        app = createEvent.create(self.email)
        app.run()

    def run(self):
        self.root.mainloop()