import tkinter as tk
from PIL import ImageTk, Image
import sqlite3
from tkcalendar import DateEntry


def signUpFunction():
    logInLabel.place_forget()
    logInButton.place_forget()
    userNameEntryLabel.place_forget()
    userNameEntry.place_forget()
    passwordEntryLabel.place_forget()
    passwordEntry.place_forget()
    forgetPasswordButton.place_forget()
    logInErrorLabel.place_forget()
    newUserLabel.place_forget()
    signUpButton.place_forget()
    firstNameLabel = tk.Label(root, text="Firstname", bg="white", fg="black", font=("Helvetica", 12))
    firstNameLabel.place(relx=0.3, rely=0.2, anchor=tk.CENTER)
    firstNameEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
    firstNameEntry.place(relx=0.43, rely=0.2, anchor=tk.CENTER)
    lastNameLabel = tk.Label(root, text="Lastname", bg="white", fg="black", font=("Helvetica", 12))
    lastNameLabel.place(relx=0.3, rely=0.25, anchor=tk.CENTER)
    lastNameEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
    lastNameEntry.place(relx=0.43, rely=0.25, anchor=tk.CENTER)
    emailIdLabel = tk.Label(root, text="Email", bg="white", fg="black", font=("Helvetica", 12))
    emailIdLabel.place(relx=0.3, rely=0.3, anchor=tk.CENTER)
    emailIdEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
    emailIdEntry.place(relx=0.43, rely=0.3, anchor=tk.CENTER)
    mobileLabel = tk.Label(root, text="Mobile No.", bg="white", fg="black", font=("Helvetica", 12))
    mobileLabel.place(relx=0.3, rely=0.35, anchor=tk.CENTER)
    mobileEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
    mobileEntry.place(relx=0.43, rely=0.35, anchor=tk.CENTER)
    dateOfBirthLabel = tk.Label(root, text="Date of Birth", bg="white", fg="black", font=("Helvetica", 12))
    dateOfBirthLabel.place(relx=0.3, rely=0.4, anchor=tk.CENTER)
    dateOfBirthEntry = DateEntry(root, width=42, bg="black", fg="white", year=2000)
    dateOfBirthEntry.place(relx=0.43, rely=0.4, anchor=tk.CENTER)


def logInButtonFunction():
    uName = userNameEntry.get()
    pWord = passwordEntry.get()
    if len(uName) == 0:
        logInErrorLabel["text"] = "Username cannot be Empty..."
        logInErrorLabel.place(relx=0.3, rely=0.7, anchor=tk.CENTER)
        return
    elif len(pWord) == 0:
        logInErrorLabel["text"] = "Password cannot be Empty..."
        logInErrorLabel.place(relx=0.3, rely=0.7, anchor=tk.CENTER)
        return
    conn = sqlite3.connect("Username_Passwords.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Username_Passwords_DB
                (Username text, Password text)''')
    cur.execute('''SELECT * FROM Username_Passwords_DB WHERE Username=?''', (uName, ))
    credinals = cur.fetchall()
    if len(credinals) == 0:
        logInErrorLabel["text"] = "User not Found..."
        logInErrorLabel.place(relx=0.3, rely=0.7, anchor=tk.CENTER)
        return
    elif credinals[0][0] == uName and credinals[0][1] == pWord:
        logInLabel.place_forget()
        logInButton.place_forget()
        userNameEntryLabel.place_forget()
        userNameEntry.place_forget()
        passwordEntryLabel.place_forget()
        passwordEntry.place_forget()
        forgetPasswordButton.place_forget()
        logInErrorLabel.place_forget()
        newUserLabel.place_forget()
        signUpButton.place_forget()
        print("Login Successful...")
        return
    elif credinals[0][0] == uName and credinals[0][1] != pWord:
        logInErrorLabel["text"] = "Incorrect Password..."
        logInErrorLabel.place(relx=0.3, rely=0.7, anchor=tk.CENTER)
        return


root = tk.Tk()
root.geometry("1500x800")
root.title("My Space")
root.iconbitmap("Icon.ico")
bgImage = Image.open('Background.jpg')
img = ImageTk.PhotoImage(bgImage)
label1 = tk.Label(root, image=img)
label1.pack()
logInLabel = tk.Label(root, text="Log in", bg="white", fg="black", font=("Helvetica", 15))
logInLabel.place(relx=0.219, rely=0.3, anchor=tk.CENTER)
userNameEntryLabel = tk.Label(root, text="Username", bg="white", fg="black", font=("Helvetica", 15))
userNameEntryLabel.place(relx=0.231, rely=0.365, anchor=tk.CENTER)
userNameEntry = tk.Entry(root, width=40, font=("Helvetica", 13))
userNameEntry.place(relx=0.32, rely=0.41, anchor=tk.CENTER)
passwordEntryLabel = tk.Label(root, text="Password", bg="white", fg="black", font=("Helvetica", 15))
passwordEntryLabel.place(relx=0.231, rely=0.46, anchor=tk.CENTER)
passwordEntry = tk.Entry(root, width=40, font=("Helvetica", 13))
passwordEntry.place(relx=0.32, rely=0.505, anchor=tk.CENTER)
forgetPasswordButton = tk.Button(root, text="Forgot Password?", bg="white", fg="blue", font=("Helvetica", 10, "bold"), cursor="hand2")
forgetPasswordButton.place(relx=0.4, rely=0.55, anchor=tk.CENTER)
logInButton = tk.Button(root, text="Log in", bg="white", fg="black", cursor="hand2", command=logInButtonFunction)
logInButton.place(relx=0.212, rely=0.6, anchor=tk.CENTER)
logInErrorLabel = tk.Label(root, text="User not found...", bg="white", fg="red", font=("Helvetica", 15, "bold"))
newUserLabel = tk.Label(root, text="New User", bg="white", fg="blue", font=("Helvetica", 10))
newUserLabel.place(relx=0.218, rely=0.65, anchor=tk.CENTER)
signUpButton = tk.Button(root, text="Sign Up", bg="white", fg="black", font=("Helvetica", 8), cursor="hand2", command=signUpFunction)
signUpButton.place(relx=0.261, rely=0.65, anchor=tk.CENTER)
root.mainloop()
