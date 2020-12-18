import sqlite3
import DB1
import datetime


def newUser(userName, fName, lName, mobile, dOB, sQues, sAns, password):
    conn = sqlite3.connect("Username_Passwords.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Username_Passwords_DB
                (Username text, Firstname text, Lastname text, Mobile text, Date_Of_Birth text, SecurityQuestion text, SQAnswer text, Password text, Last_Login text)''')
    cur.execute('''INSERT INTO Username_Passwords_DB VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''', (userName, fName, lName, mobile, dOB, sQues, sAns, password, "None"))
    conn.commit()
    conn.close()
    return


def deleteUser(userName):
    conn = sqlite3.connect("Username_Passwords.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Username_Passwords_DB
                (Username text, Password text)''')
    cur.execute('''DELETE FROM Username_Passwords_DB WHERE Username=?''', (userName,))
    conn.commit()
    conn.close()
    DB1.deleteData(userName)
    return


def updatePassword(userName, password):
    conn = sqlite3.connect("Username_Passwords.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Username_Passwords_DB
                (Username text, Password text)''')
    cur.execute('''UPDATE Username_Passwords_DB SET Password=? WHERE Username=?''', (password, userName))
    conn.commit()
    conn.close()
    return


def getDetails(userName):
    conn = sqlite3.connect("Username_Passwords.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Username_Passwords_DB
                (Username text, Password text)''')
    cur.execute('''SELECT * FROM Username_Passwords_DB WHERE Username=?''', (userName,))
    details = cur.fetchall()
    if len(details) == 0:
        return []
    else:
        return details[0]


def updateLastLogin(userName):
    conn = sqlite3.connect("Username_Passwords.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Username_Passwords_DB
                    (Username text, Password text)''')
    date = datetime.datetime.now()
    date = str(date)[:16]
    cur.execute('''UPDATE Username_Passwords_DB SET Last_Login=? WHERE Username=?''', (date, userName))
    conn.commit()
    conn.close()
    return
