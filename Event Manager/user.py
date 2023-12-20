from customtkinter import * #type: ignore
from tkinter import messagebox
import sqlite3
from tools import * 
import smtplib
import random
from home import *

class login:
    def __init__(self):
        # widgets
        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()

            c.execute("""CREATE TABLE IF NOT EXISTS users(
                        name TEXT,
                        email TEXT,
                        password TEXT
                    )
                """)

        self.root = CTk(fg_color="#242322")
        self.root.geometry("800x600")
        self.root.title("Event Manager | Login")

        self.frame = CTkFrame(master=self.root)
        self.frame.pack(pady=10, expand=True)

        self.heading = CTkLabel(master=self.frame, text="Log into your Account", font=("Arial", 24))
        self.heading.pack(pady=30, padx=50)

        self.emailInput = CTkEntry(master=self.frame, placeholder_text="Email", width=240)
        self.emailInput.pack(pady=10, padx=50)

        self.passwordInput = CTkEntry(master=self.frame, placeholder_text="Password", width=240)
        self.passwordInput.pack(pady=10, padx=50)

        self.forgotPasswordLink = CTkLabel(master=self.frame, text="Forgot Password?", text_color="skyblue")
        self.forgotPasswordLink.pack(pady=10)
        self.forgotPasswordLink.bind("<Button-1>", lambda event=None : self.callResetPasswordClass())

        self.rememberMeVar = IntVar() 
        self.rememberMeBtn = CTkCheckBox(master=self.frame, text="Remember Me?", corner_radius=50, variable=self.rememberMeVar, checkbox_width=20, checkbox_height=20, command=self.enableRememberMe)
        self.rememberMeBtn.pack(pady=10, padx=10)

        self.loginBtn = CTkButton(master=self.frame, text="Login", fg_color="green", hover_color="darkgreen", corner_radius=32, command=self.loginToAccount)
        self.loginBtn.pack(pady=10, padx=50)

        self.signUpLink = CTkLabel(master=self.frame, text="Or Sign Up?")
        self.signUpLink.pack(pady=10)
        self.signUpLink.bind("<Button-1>", lambda event=None : self.callSignUpClass())

    def enableRememberMe(self):
        # store ip in db
        if self.rememberMeVar.get() == 0:
            print("off")
        else:
            print("on")

    def loginToAccount(self):
        email = self.emailInput.get().strip()
        password = self.passwordInput.get().strip()

        if email == "" or password == "":
            messagebox.showerror(title="Fields blank", message="Fields cannot be left blank!")
        elif not account_in_db(email, password):
            messagebox.showerror(title="Account not found", message="Your account has not been found.")
        else:
            messagebox.showinfo(title="Account Found", message=f"Your account has been found {self.getAccountName(email)}.")
            app = home()
            app.run()

    def getAccountName(self, email):
        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()

            c.execute("SELECT name FROM users WHERE email=?", (email,))
            name = c.fetchall()
            for l in name:
                for t in l: # remove name from list and tuple
                    name = t

        return name

    def callSignUpClass(self):
        self.root.withdraw()
        signUpApp = signUp()
        signUpApp.run()

    def callResetPasswordClass(self):
        self.root.withdraw()
        resetPasswordApp = resetPassword()
        resetPasswordApp.run()

    def run(self):
        self.root.mainloop()

class resetPassword:
    def __init__(self):
        self.root = CTk(fg_color="#242322")
        self.root.geometry("800x600")
        self.root.title("Event Manager | Reset Password")

        self.frame = CTkFrame(master=self.root)
        self.frame.pack(pady=10, expand=True)

        self.heading = CTkLabel(master=self.frame, text="Reset Your Password", font=("Arial", 24))
        self.heading.pack(pady=30, padx=50)

        self.emailInput = CTkEntry(master=self.frame, placeholder_text="Email Associated With The Account", width=240)
        self.emailInput.pack(pady=10, padx=50)

        self.confirmEmailBtn = CTkButton(master=self.frame, text="Confirm Email", fg_color="green", hover_color="darkgreen", corner_radius=32, command=self.checkEmail)
        self.confirmEmailBtn.pack(pady=10, padx=50)

        self.verificationCodeInput = CTkEntry(master=self.frame, placeholder_text="Verification Code", width=240)

        self.confirmVerificationCodeBtn = CTkButton(master=self.frame, text="Confirm Verification Code", fg_color="green", hover_color="darkgreen", corner_radius=32, command=self.confirmVerificationCode)

        self.newPasswordInput = CTkEntry(master=self.frame, placeholder_text="New Password", width=240)

        self.confirmNewPasswordBtn = CTkButton(master=self.frame, text="Confirm New Password", fg_color="green", hover_color="darkgreen", corner_radius=32, command=self.storeNewPassword)

        self.backToLoginLink = CTkLabel(master=self.frame, text="Back To Login")
        self.backToLoginLink.pack(pady=10)
        self.backToLoginLink.bind("<Button-1>", lambda event=None : self.callLoginClass())

    def checkEmail(self):
        if not email_in_db(self.emailInput.get().strip()):
            messagebox.showerror(title="Email Error", message="Email Not Found")
        else:
            self.sendVerificationCode()

    def confirmVerificationCode(self):
        codeEntered = int(self.verificationCodeInput.get().strip())

        if codeEntered == self.verificationCode:
            messagebox.showinfo(title="Correct Code", message="The Verification Code Was Correct And You May Now Chnage Your Password.")
            self.newPasswordInput.pack(pady=10, padx=50)
            self.confirmNewPasswordBtn.pack(pady=10, padx=50)
        else:
            messagebox.showerror(title="Code Incorrect", message="The Verification Code Entered Was Incorrect.")

    def sendVerificationCode(self):
        # self.verificationCode = random.randint(100000, 999999)
        # smtpServer = "smtp.gmail.com"
        # smtpPort = 587
        # senderEmail = "taskmanagerpython@gmail.com"
        # senderPassword = "hmin ksas xtje ipwz"
        # receiverEmail = self.emailInput.get().strip()
        # subject = "Reset Password - Verification Code"
        # body = """
        #     Your Verification Code Is {}
        #     Please Do Not Share This With Anyone!
        # """.format(self.verificationCode)
        # message = "Subject: {}\n\n{}".format(subject, body) # Create the message in email format

        # # Establish a connection to the SMTP server
        # try:
        #     with smtplib.SMTP(smtpServer, smtpPort) as server:
        #         server.starttls()  # Upgrade the connection to a secure TLS connection
        #         server.login(senderEmail, senderPassword)   # login to the senders email
        #         server.sendmail(senderEmail, receiverEmail, message)    # Send the email
        # except Exception as ex:
        #     messagebox.showerror(title="An error has occured",  message=f"An error has occured. Are you connected to your internet? {type(ex)}")
        # else:
        self.verificationCode = 5
        messagebox.showinfo(title="Verification Code Sent", message=f"The Verification Code Has Been Sent To {self.emailInput.get()}")
        self.verificationCodeInput.pack(pady=10, padx=50)
        self.confirmVerificationCodeBtn.pack(pady=10, padx=50)

    def storeNewPassword(self):
        newPassword = self.newPasswordInput.get().strip()

        if not_valid_password(newPassword):
            messagebox.showerror(title="Password Error", message="Password must be at least 8 characters, not contain just symbols, not contain just numbers, not contain any spaces and must have a number in it!")
        elif newPassword == find_password_in_db(self.emailInput.get().strip(), newPassword):
            messagebox.showerror(title="Password Already Associated.", message="The Password You Entered Is Already Associated With The Account")
        else:
            with sqlite3.connect("database.db") as conn:
                c = conn.cursor()
                c.execute("UPDATE users SET password=? WHERE email=?", (newPassword, self.emailInput.get().strip()))

            messagebox.showinfo(title="Password Changed", message=f"You Password Has Been Changed to {newPassword}. You May Now Login.")
            self.callLoginClass()

    def callLoginClass(self):
        self.root.withdraw()
        main()

    def run(self):
        self.root.mainloop()

class signUp:
    def __init__(self):
        self.root = CTk(fg_color="#242322")
        self.root.geometry("800x600")
        self.root.title("Event Manager | Sign Up")
        
        self.frame = CTkFrame(master=self.root)
        self.frame.pack(pady=10, expand=True)

        self.heading = CTkLabel(master=self.frame, text="Create your Account", font=("Arial", 24))
        self.heading.pack(pady=30, padx=50)

        self.nameInput = CTkEntry(master=self.frame, placeholder_text="Name", width=240)
        self.nameInput.pack(pady=10, padx=50)

        self.emailInput = CTkEntry(master=self.frame, placeholder_text="Email", width=240)
        self.emailInput.pack(pady=10, padx=50)

        self.passwordInput = CTkEntry(master=self.frame, placeholder_text="Password", width=240)
        self.passwordInput.pack(pady=10, padx=50)

        self.confirmPasswordInput = CTkEntry(master=self.frame, placeholder_text="Confirm Password", width=240)
        self.confirmPasswordInput.pack(pady=10, padx=50)

        self.signUpBtn = CTkButton(master=self.frame, text="Sign Up", fg_color="green", hover_color="darkgreen", corner_radius=32, command=self.storeDetailsInDb)
        self.signUpBtn.pack(pady=10, padx=50)

        self.loginLink = CTkLabel(master=self.frame, text="Or Login?")
        self.loginLink.pack(pady=10)
        self.loginLink.bind("<Button-1>", lambda event=None: self.callLoginClass())

    def storeDetailsInDb(self):
        name = self.nameInput.get().strip()
        email = self.emailInput.get().strip()
        password = self.passwordInput.get().strip()
        confirmedPassword = self.confirmPasswordInput.get().strip()
        splitEmail = email[email.find("@"):]

        if name == "" or len(name) < 3 or is_all_symbols(name):
            messagebox.showerror(title="Name Error", message="Names must be at least 3 characters, not just contain symbols and not just contain numbers!")
        elif not is_valid_email(splitEmail) or email == "":
            messagebox.showerror(title="Email Error", message="Emails must include a name, provider and extension!")
        elif email_in_db(email):
            messagebox.showerror(title="Email Error", message="Emails is aleady in use!")
        elif not_valid_password(password):
            messagebox.showerror(title="Password Error", message="Password must be at least 8 characters, not contain just symbols, not contain just numbers, not contain any spaces and must have a number in it!")
        elif password != confirmedPassword:
            messagebox.showerror(title="Password Error", message="Password do not match!")
        else:
            with sqlite3.connect("database.db") as conn:
                c = conn.cursor()
                c.execute("INSERT INTO users VALUES(?,?,?)", [name, email, password])
            
            messagebox.showinfo(title="Account Created", message=f"Your account has been created {name}")

    def callLoginClass(self):   
        self.root.withdraw()
        main()

    def run(self):
        self.root.mainloop()

def main():
    # Used to show the login page which is the default page
    app = login()
    app.run()

if __name__ == "__main__":
    main()
    