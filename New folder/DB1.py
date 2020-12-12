import sqlite3


def updateUser(user, application, username, password):
    conn = sqlite3.connect("Passwords.sqlite")
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Passwords WHERE ApplicationOrWebsiteName=? AND User=?''',
                (application.lower(), user))
    d = cur.fetchall()
    if len(d) == 0:
        return "Application Not found..."
    if application != "" and username != "" and password != "":
        cur.execute('''UPDATE Passwords set Username=?, Password=? WHERE ApplicationOrWebsiteName=? AND User=?''',
                    (username, password, application.lower(), user))
        conn.commit()
        conn.close()
        return "Successfully Updated..."

    else:
        return "Credinals Cannot be Empty..."


def showAll(user):
    conn = sqlite3.connect("Passwords.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Passwords
                        (User text, ApplicationOrWebsiteName text, Username text, Password text)''')
    cur.execute('''SELECT * FROM Passwords WHERE User=?''', (user,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    string = "Application" + (" "*29) + "Username" + (" "*32) + "Password" + (" "*32) + "\n"
    for row in rows:
        application = str(row[1])
        application = application + " "*(40-len(application))
        username = str(row[2])
        username = username + " "*(40-len(username))
        password = str(row[3])
        password = password + " "*(40-len(password))
        string = string + application + username + password + "\n"
    return string


def addUser(user, application, username, password):
    conn = sqlite3.connect("Passwords.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Passwords
            (User text, ApplicationOrWebsiteName text, Username text, Password text)''')
    cur.execute('''SELECT * FROM Passwords;''')
    if application != "" and username != "" and password != "":
        cur.execute('''INSERT INTO Passwords VALUES(?, ?, ?, ?);''',
                    (user, application.lower(), username, password))
        conn.commit()
        conn.close()
        return "Successfully Added..."
    else:
        return "Credinals Cannot be empty.."


def deleteUser(user, application):
    conn = sqlite3.connect("Passwords.sqlite")
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Passwords WHERE ApplicationOrWebsiteName=? AND User=?''',
                (application.lower(), user))
    d = cur.fetchall()
    if len(d) == 0:
        return "Application Not found..."
    elif len(application) == 0:
        return "Credinals Cannot be empty"
    else:
        cur.execute('''CREATE TABLE IF NOT EXISTS Passwords
                            (User text, ApplicationOrWebsiteName text, Username text, Password text)''')
        cur.execute('''DELETE FROM Passwords WHERE ApplicationOrWebsiteName=? AND User=?''',
                    (application.lower(), user))
        conn.commit()
        conn.close()
        return "Successfully Deleted..."


def deleteData(user):
    conn = sqlite3.connect("Passwords.sqlite")
    cur = conn.cursor()
    cur.execute('''DELETE FROM Passwords WHERE User=?''', (user, ))
    conn.commit()
    conn.close()
    return
