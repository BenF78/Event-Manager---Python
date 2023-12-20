from customtkinter import * #type: ignore
import sqlite3

class home:
    def __init__(self, email):
        self.email = email
        self.root = CTk()
        self.root.title("Event Manager | Home")
        self.root.geometry("800x600")

        self.greeting = CTkLabel(master=self.root, text=f"Hello {self.getAccountName()}")
        self.greeting.pack(pady=10)

        self.heading = CTkLabel(master=self.root, text="Home", font=("Arial", 32))
        self.heading.pack(pady=10)

        self.selectLabel = CTkLabel(master=self.root, text="Select An Option To Do From Below")
        self.selectLabel.pack(pady=10)

        self.createEventBtn = CTkButton(master=self.root, text="Create Event", corner_radius=32, hover_color="darkgreen", width=200, fg_color="green")
        self.createEventBtn.pack(pady=10)

        self.viewEventsBtn = CTkButton(master=self.root, text="Create Event", corner_radius=32, hover_color="darkgreen", width=200, fg_color="green")
        self.viewEventsBtn.pack(pady=10)

        self.viewProfileBtn = CTkButton(master=self.root, text="View Account Details", corner_radius=32, hover_color="darkgreen", width=200, fg_color="green")
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


        

    def run(self):
        self.root.mainloop()