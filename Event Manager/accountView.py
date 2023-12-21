from customtkinter import *
import sqlite3
import home
from tools import *
from tkinter import messagebox

class accountView:
    def __init__(self, email):
        # Create all widgets fot account view
        self.email = email
        self.root = CTk()
        self.root.title("Event Manager | View Account")
        self.root.geometry("1000x700") 

        self.heading = CTkLabel(master=self.root, text="Account Details", font=("Arial", 36, "bold"))
        self.heading.pack(pady=20)

        self.nameLabel = CTkLabel(master=self.root, text="Name:", font=("Arial", 22, "bold"))
        self.nameLabel.pack(pady=10)
        self.showName = CTkEntry(master=self.root, width=300, height=40, border_color="white", border_width=1)

        # Insert the name into the entry box
        self.showName.insert(END, self.getAccountName())
        self.showName.pack(pady=10)

        self.emailLabel = CTkLabel(master=self.root, text="Email:", font=("Arial", 22, "bold"))
        self.emailLabel.pack(pady=10)
        self.showEmail = CTkEntry(master=self.root, width=300, height=40, border_color="white", border_width=1)
        self.showEmail.insert(END, self.email)
        self.showEmail.pack(pady=10)

        self.passwordLabel = CTkLabel(master=self.root, text="Password:", font=("Arial", 22, "bold"))
        self.passwordLabel.pack(pady=10)
        self.showPassword = CTkEntry(master=self.root, width=300, height=40, border_color="white", border_width=1)
        self.showPassword.insert(END, self.getAccountPassword())
        self.showPassword.pack(pady=10) 

        self.saveChangesBtn = CTkButton(master=self.root, text="Save Changes", fg_color="green", hover_color="darkgreen", corner_radius=20, font=("Arial", 18), width=150, height=30,command=self.updateDetails)
        self.saveChangesBtn.pack(pady=10)

        self.goBackToHomeBtn = CTkLabel(master=self.root, text="Back To Home", font=("Arial", 16))
        self.goBackToHomeBtn.bind("<Button-1>", lambda event=None : self.callHomeModule())
        self.goBackToHomeBtn.pack(pady=10)


    def getAccountName(self):
        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()

            # Find the name associated with the email
            c.execute("SELECT name FROM users WHERE email=?", (self.email,))
            self.name = c.fetchall()
            
            # Loop through the returned name to remove it from the list and tuple
            for l in self.name: 
                for t in l:
                    self.name = t
                    # Return the name to insert it in the entry
                    return self.name

    def getAccountPassword(self):
        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()

            # Find the password associated with the email
            c.execute("SELECT password FROM users WHERE email=?", (self.email,))
            self.password = c.fetchall()
            
            # Loop through [()] -> XYZ
            for l in self.password:
                for t in l:
                    self.password = t
                    return self.password 
                
    def updateDetails(self):
        # Get all account details and remove the white space
        name = self.showName.get().strip()
        email = self.showEmail.get().strip()
        password = self.showPassword.get().strip()
        detailsList = [name,email,password]
        # Get the email extension by indexing from the @ symbol
        splitEmail = email[email.find("@"):]

        # Call the validation functions inside the tools.py to ensure everything is valid.
        if not is_valid_email(splitEmail):
            messagebox.showerror(title="Email Error", message="Email Not Found")
        # If they keep their email the same do not alert them that the email exists
        elif email_in_db(email) and get_email(self.email) != email:
            messagebox.showerror(title="Email Already Exists", message="The Email You Entered Already Exists.")
        elif name == "" or len(name) < 3 or is_all_symbols(name):
            messagebox.showerror(title="Name Error", message="Names must be at least 3 characters, not just contain symbols and not just contain numbers!")
        elif not_valid_password(password):
            messagebox.showerror(title="Password Error", message="Password must be at least 8 characters, not contain just symbols, not contain just numbers, not contain any spaces and must have a number in it!")
        # If all the details are the same alert them that no changes where made
        elif detailsList == get_account_details(email):
            messagebox.showerror(title="No Changes", message="No Changes Have Been Made To Your Account.")
        else:
            # If changes where made connect to the db and update the name,email,password
            with sqlite3.connect("database.db") as conn:
                c = conn.cursor()
                # update details in the events table
                c.execute("UPDATE users SET name=?,email=?,password=?", (name,email,password))
                # self.email is the original email
                c.execute("UPDATE events SET email=? WHERE email=?", (email, self.email))

                messagebox.showinfo(title="Details Changed", message="Your Accont Details Have Been Changed")
                
    def callHomeModule(self):
        # Withdraw the current root and run the home module so they return back to the home when the btn is clicked
        self.root.withdraw()
        app = home.home(self.email)
        app.run()

    def run(self):
        self.root.mainloop()