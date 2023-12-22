

def contains_digit(string) -> bool:
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for digit in digits:
        if digit in string:
            return True
        
    return False

def contains_symbols(string) -> bool:
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', ':', ';', '<', '>', '/', '\\', '|', ',', '.', '?', '~', '`']

    for symbol in symbols:
        if symbol in string:
            return True
        
    return False

def is_all_symbols(string) -> bool:
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', ':', ';', '<', '>', '/', '\\', '|', ',', '.', '?', '~', '`']

    for char in string:
        if char not in symbols:
            return False
        
    if string != "":
        return True
    else:
        return False

def contains_spaces(string) -> bool:
    if string.find(" ") in range(len(string)):
        return True
    else:
        return False
    
def is_NaN(string) -> bool:
    if type(string) == int or type(string) == float:
        return False
    else:
        return True
    
def index_of(string, List):
    i = 0
    for item in List:
        if string == item:
            return i
        
        i += 1

        if string != item and i == len(List):
            return "Error: Item Not In List!"
        
def strip_start(string):
    for char in string:
        if char != " ":
            first_char = index_of(char, string)
            return string[first_char:]
        
def contains_number(string):
    return any(char.isdigit() for char in string)

def not_valid_password(password) -> bool:
    if len(password) < 8 or contains_spaces(password) or is_all_symbols(password) or password == "" or password.isdigit() or not contains_number(password):
        return True
    else:
        return False
    
def is_valid_email(email) -> bool:
    validEmailProvider = [
        "@gmail.com",
        "@yahoo.com",
        "@hotmail.com",
        "@outlook.com",
        "@aol.com",
        "@icloud.com",
        "@protonmail.com",
        "@student.runshaw.ac.uk",
        "@googlemail.com"
    ]

    if email not in validEmailProvider:
        return False
    else:
        return True
    
def email_in_db(email) -> bool:
    import sqlite3

    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()

        c.execute("SELECT * FROM users WHERE email=?", (email,))
        emailInDb = c.fetchall()
        emailInDb = [email[0] for email in emailInDb]
    
    if emailInDb:
        return True
    else:
        return False
    

def account_in_db(email, password):
    import sqlite3
    
    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()

        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        userData = c.fetchall()

    if userData:
        return True
    else:
        return False
    
def find_password_in_db(email, password):
    import sqlite3
    
    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()

        c.execute("SELECT password FROM users WHERE email=? AND password=?", (email, password))
        password = c.fetchall()

    for l in password:
        for t in l:
            password = t
            return password
        
def event_name_exists(email, eventName):
    import sqlite3
    
    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()

        c.execute("SELECT * FROM events WHERE email=? AND name=?", (email, eventName))
        eventInDb = c.fetchall()

    if eventInDb:
        return True
    else:
        return False
    
def get_all_user_events(email):
    import sqlite3

    try:
        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()

            c.execute("SELECT name,dueDate FROM events WHERE email=?", (email,))

            allEvents = c.fetchall()

            return allEvents
    except sqlite3.OperationalError:
        return False
    

def get_email(email):
    import sqlite3

    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()

        c.execute("SELECT email FROM users WHERE email=?", (email,))
        email = c.fetchall()

        for l in email:
            for t in l:
                email = t
                return email
            
def get_account_details(email):
    import sqlite3

    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()

        c.execute("SELECT name,email,password FROM users WHERE email=?", (email,))

        accountDetails = c.fetchall()

        for details in accountDetails:
            print(list(details))
            return list(details)
        
def get_event_description(email, eventName):
    import sqlite3

    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()

        c.execute("SELECT description FROM events WHERE email=? AND name=?", (email,eventName))
        eventDesc = c.fetchall()
        
        for l in eventDesc:
            for t in l:
                eventDesc = t
                return eventDesc
            
def get_event_due_date(email, eventName):
    import sqlite3

    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()

        c.execute("SELECT dueDate FROM events WHERE email=? AND name=?", (email,eventName))
        dueDate = c.fetchall()
        
        for l in dueDate:
            for t in l:
                dueDate = t
                return dueDate
            

def get_account_name(email):
        import sqlite3

        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()

            c.execute("SELECT name FROM users WHERE email=?", (email,))
            name = c.fetchall()

            for t in name:
                for l in t:
                    name = l
                    return str(name).capitalize()

def sign_out(email):
    import sqlite3

    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()

        c.execute("UPDATE users SET ip=? WHERE email=?", (None,email))

