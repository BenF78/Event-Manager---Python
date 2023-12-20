from customtkinter import * #type: ignore
import sqlite3
from create import * #type: ignore

class home:
    def __init__(self, email):
        self.email = email
        self.root = CTk()
        self.root.title("Event Manager | Home")
        self.root.geometry("800x600")

        self.heading = CTkLabel(master=self.root, text="Home", font=("Arial", 36, "bold"))
        self.heading.pack(pady=20)

        self.selectLabel = CTkLabel(master=self.root, text=f"Hello {self.getAccountName()}, Select An Option From Below:", font=("Arial", 24))
        self.selectLabel.pack(pady=20)

        self.createEventBtn = CTkButton(master=self.root, text="Create Event", corner_radius=32, hover_color="darkgreen", width=250, height=40, fg_color="green", font=("Arial", 20, "bold"),command=lambda event=None: self.callCreateEventClass())
        self.createEventBtn.pack(pady=10)

        self.viewEventsBtn = CTkButton(master=self.root, text="Create Event", corner_radius=32, hover_color="darkgreen", width=250, height=40, fg_color="green", font=("Arial", 20, "bold"))
        self.viewEventsBtn.pack(pady=10)

        self.viewProfileBtn = CTkButton(master=self.root, text="View Account Details", corner_radius=32, hover_color="darkgreen", width=250, height=40, fg_color="green", font=("Arial", 20, "bold"))
        self.viewProfileBtn.pack(pady=10)
    
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
        app = create(self.email)
        app.run()


        

    def run(self):
        self.root.mainloop()