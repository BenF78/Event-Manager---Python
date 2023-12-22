from customtkinter import *

def showNav():
    # Create a left frame
    leftFrame = CTkFrame(master=root, height=600, width=300)
    leftFrame.pack(side="left", fill="y")  # Use fill="y" to make the frame expand vertically

    navHeading = CTkLabel(master=leftFrame, text="Logged In As Admin", font=("Arial", 22, "bold"))
    navHeading.pack(side="top", pady=20)

    navHomeBtn = CTkLabel(master=leftFrame, text="      Home", fg_color="#4f4e4e", compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
    navHomeBtn.bind("<Button-1>", lambda event: print("Home clicked"))
    navHomeBtn.pack(pady=10)

    navCreateTaskBtn = CTkLabel(master=leftFrame, text="      Create Event", compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
    navCreateTaskBtn.bind("<Button-1>", lambda event: print("Create Event clicked"))
    navCreateTaskBtn.pack(pady=10)

    navViewPendingTasksBtn = CTkLabel(master=leftFrame, text="      View Pending Events", compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
    navViewPendingTasksBtn.bind("<Button-1>", lambda event: print("View Pending Events clicked"))
    navViewPendingTasksBtn.pack(pady=10)

    navViewCompletedTasksBtn = CTkLabel(master=leftFrame, text="      View Completed Events", compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
    navViewCompletedTasksBtn.bind("<Button-1>", lambda event: print("View Completed Events clicked"))
    navViewCompletedTasksBtn.pack(pady=10)

    navViewAccountBtn = CTkLabel(master=leftFrame, text="      Account Details", compound="left", font=("Arial", 18, "bold"), width=300, height=60, anchor="w")
    navViewAccountBtn.bind("<Button-1>", lambda event: print("Account Details clicked"))
    navViewAccountBtn.pack(pady=10)

    navSignOutBtn = CTkButton(master=leftFrame, text=" Sign Out", font=("Arial", 18, "bold"), command=lambda: print("Sign Out clicked"), width=250, height=40)
    navSignOutBtn.pack(pady=10)

    rightHeading = CTkLabel(master=root, text="Event Manager", font=("Arial", 32, "bold"))
    rightHeading.pack(pady=40)

    notificationsHeading = CTkLabel(master=root, text="Your Notifications:", font=("Arial", 20))
    notificationsHeading.pack(pady=10)

    notificationsFrame = CTkScrollableFrame(master=root, scrollbar_button_color="skyblue", orientation="horizontal", width=500)
    notificationsFrame.pack(pady=20)

    for i in range(10):
        testNotification = CTkButton(master=notificationsFrame, text="Test Event Due Today!", fg_color="red", height=170)
        testNotification.pack(pady=10, padx=10, side="left")

root = CTk()
root.geometry("1000x600")

showNav()

root.mainloop()
