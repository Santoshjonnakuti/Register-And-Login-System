import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3
from tkcalendar import DateEntry
import DB
global name


def signUpFunction():
    firstNameEntry.delete(0, tk.END)
    lastNameEntry.delete(0, tk.END)
    emailIdEntry.delete(0, tk.END)
    mobileEntry.delete(0, tk.END)
    dateOfBirthEntry.delete(0, tk.END)
    securityQuestions.delete(0, tk.END)
    securityQuesAnsEntry.delete(0, tk.END)
    passwordEntry1.delete(0, tk.END)
    reEntryPasswordEntry.delete(0, tk.END)
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
    forgetSQuesLabel.place_forget()
    forgetSAnsEntry.place_forget()
    forgetOkButton.place_forget()
    confirmLabel.place_forget()
    forgetBackButton.place_forget()
    firstNameLabel.place(x=455, y=150, anchor=tk.CENTER)
    firstNameEntry.place(x=645, y=150, anchor=tk.CENTER)
    lastNameLabel.place(x=455, y=200, anchor=tk.CENTER)
    lastNameEntry.place(x=645, y=200, anchor=tk.CENTER)
    emailIdLabel.place(x=470, y=250, anchor=tk.CENTER)
    emailIdEntry.place(x=645, y=250, anchor=tk.CENTER)
    mobileLabel.place(x=455, y=300, anchor=tk.CENTER)
    mobileEntry.place(x=645, y=300, anchor=tk.CENTER)
    dateOfBirthLabel.place(x=450, y=350, anchor=tk.CENTER)
    dateOfBirthEntry.place(x=645, y=350, anchor=tk.CENTER)
    securityQuestionsLabel.place(x=435, y=400, anchor=tk.CENTER)
    securityQuestions.place(x=655, y=400, anchor=tk.CENTER)
    securityQuesAnsLabel.place(x=470, y=450, anchor=tk.CENTER)
    securityQuesAnsEntry.place(x=645, y=450, anchor=tk.CENTER)
    passwordLabel.place(x=460, y=500, anchor=tk.CENTER)
    passwordEntry1.place(x=645, y=500, anchor=tk.CENTER)
    reEntryPasswordLabel.place(x=427, y=550, anchor=tk.CENTER)
    reEntryPasswordEntry.place(x=645, y=550, anchor=tk.CENTER)
    registerButton.place(x=600, y=600, anchor=tk.CENTER)
    backButton.place(x=500, y=600, anchor=tk.CENTER)


def logInButtonFunction():
    uName = userNameEntry.get()
    pWord = passwordEntry.get()
    if len(uName) == 0:
        logInErrorLabel["text"] = "Username cannot be Empty..."
        logInErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
        return
    elif len(pWord) == 0:
        logInErrorLabel["text"] = "Password cannot be Empty..."
        logInErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
        return
    conn = sqlite3.connect("Username_Passwords.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Username_Passwords_DB
                (Username text, Password text)''')
    cur.execute('''SELECT * FROM Username_Passwords_DB WHERE Username=?''', (uName, ))
    credinals = cur.fetchall()
    print(credinals)
    if len(credinals) == 0:
        logInErrorLabel["text"] = "User not Found..."
        logInErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
        return
    elif credinals[0][0] == uName and credinals[0][7] != pWord:
        logInErrorLabel["text"] = "Incorrect Password..."
        logInErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
        return
    elif credinals[0][0] == uName and credinals[0][7] == pWord:
        logInLabel.place_forget()
        logInButton.place_forget()
        userNameEntryLabel.place_forget()
        userNameEntry.place_forget()
        passwordEntryLabel.place_forget()
        passwordEntry.place_forget()
        forgetPasswordButton.place_forget()
        confirmLabel.place_forget()
        logInErrorLabel.place_forget()
        newUserLabel.place_forget()
        signUpButton.place_forget()
        forgetSQuesLabel.place_forget()
        forgetSAnsEntry.place_forget()
        forgetOkButton.place_forget()
        forgetBackButton.place_forget()
        print("Login Successful...")
        print(credinals)
        message = '''Welcome {} {}!\nMobile : {}\nDate of Birth : {}\nE-mail id : {}'''.format(credinals[0][1], credinals[0][2], credinals[0][3], credinals[0][4], credinals[0][0])
        print(message)
        logInMessageLabel["text"] = message
        logInMessageLabel.place(x=800, y=400, anchor=tk.CENTER)
        logOutButton.place(x=800, y=550, anchor=tk.CENTER)
        deleteAccountButton.place(x=1400, y=700, anchor=tk.CENTER)
        return


def signUpBackFunction():
    firstNameLabel.place_forget()
    firstNameEntry.place_forget()
    lastNameLabel.place_forget()
    lastNameEntry.place_forget()
    emailIdLabel.place_forget()
    emailIdEntry.place_forget()
    mobileLabel.place_forget()
    mobileEntry.place_forget()
    dateOfBirthLabel.place_forget()
    dateOfBirthEntry.place_forget()
    securityQuestionsLabel.place_forget()
    securityQuestions.place_forget()
    securityQuesAnsLabel.place_forget()
    securityQuesAnsEntry.place_forget()
    registerButton.place_forget()
    backButton.place_forget()
    passwordLabel.place_forget()
    passwordEntry1.place_forget()
    reEntryPasswordLabel.place_forget()
    reEntryPasswordEntry.place_forget()
    registerErrorLabel.place_forget()
    deleteAccountButton.place_forget()
    sQuesLabel.place_forget()
    sAnsEntry.place_forget()
    okButton.place_forget()
    okButtonErrorLabel.place_forget()
    deleteBackButton.place_forget()
    forgetSQuesLabel.place_forget()
    forgetSAnsEntry.place_forget()
    forgetOkButton.place_forget()
    forgetBackButton.place_forget()
    forgetOkButtonErrorLabel.place_forget()
    logInLabel.place(x=330, y=250, anchor=tk.CENTER)
    userNameEntryLabel.place(x=350, y=300, anchor=tk.CENTER)
    userNameEntry.place(x=485, y=350, anchor=tk.CENTER)
    userNameEntry.delete(0, tk.END)
    passwordEntryLabel.place(x=350, y=400, anchor=tk.CENTER)
    passwordEntry.place(x=485, y=450, anchor=tk.CENTER)
    passwordEntry.delete(0, tk.END)
    forgetPasswordButton.place(x=608, y=500, anchor=tk.CENTER)
    logInButton.place(x=330, y=550, anchor=tk.CENTER)
    newUserLabel.place(x=340, y=600, anchor=tk.CENTER)
    signUpButton.place(x=400, y=600, anchor=tk.CENTER)


def signUpRegisterFunction():
    registerErrorLabel.place_forget()
    fName = firstNameEntry.get()
    lName = lastNameEntry.get()
    eMail = emailIdEntry.get()
    mobile = mobileEntry.get()
    dob = dateOfBirthEntry.get()
    sQues = securityQuestions.get()
    sAns = securityQuesAnsEntry.get()
    pwd = passwordEntry1.get()
    rePwd = reEntryPasswordEntry.get()
    forgetSQuesLabel.place_forget()
    forgetSAnsEntry.place_forget()
    forgetOkButton.place_forget()
    forgetBackButton.place_forget()
    mbStr = str(mobile)
    print(len(fName), len(lName), len(eMail), len(mbStr), len(sAns), len(pwd), len(rePwd))
    print(fName, lName, eMail, mobile, dob, sQues, sAns, pwd, rePwd)
    if len(fName) == 0 or len(lName) == 0 or len(eMail) == 0 or len(mbStr) == 0 or len(sQues) == 0 or len(sAns) == 0 or len(pwd) == 0 or len(rePwd) == 0:
        print("Hello")
        registerErrorLabel["text"] = "Please Fill all the above Entries..."
        registerErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
        return
    if len(mbStr) != 10:
        registerErrorLabel["text"] = "Invalid Mobile Number..."
        registerErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
        return
    try:
        mbStr = int(mbStr)
        pass
    except ValueError:
        registerErrorLabel["text"] = "Invalid Mobile Number..."
        registerErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
        return
    if pwd != rePwd:
        registerErrorLabel["text"] = "Password does not match"
        registerErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
        return
    if len(pwd) < 8:
        registerErrorLabel["text"] = "Minimum password length should be greater than 8..."
        registerErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
        return
    count = 0
    for c in range(32, 65):
        if chr(c) in pwd:
            count += 1
            break
    if count == 0:
        for c in range(91, 97):
            if chr(c) in pwd:
                count += 1
                break
    if count == 0:
        registerErrorLabel["text"] = "Please Include Special Character in Password..."
        registerErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
        return
    count = 0
    for c in range(65, 91):
        if chr(c) in pwd:
            count += 1
            break
    if count == 0:
        registerErrorLabel["text"] = "Please Include Uppercase Character in Password..."
        registerErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
        return
    count = 0
    for c in range(97, 123):
        if chr(c) in pwd:
            count += 1
            break
    if count == 0:
        registerErrorLabel["text"] = "Please Include Lowercase Character in Password..."
        registerErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
        return
    fName = fName[0].upper() + fName[1:]
    lName = lName[0].upper() + lName[1:]
    DB.newUser(eMail, fName, lName, mbStr, dob, sQues, sAns, pwd)
    registerErrorLabel["text"] = "Successfully Registered...\nPleas go back and Log in..."
    registerErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
    print("Successfully Registered...")


def logOutButtonFunction():
    logInMessageLabel.place_forget()
    logOutButton.place_forget()
    deleteAccountButton.place_forget()
    forgetSQuesLabel.place_forget()
    forgetSAnsEntry.place_forget()
    forgetOkButton.place_forget()
    forgetBackButton.place_forget()
    logInLabel.place(x=330, y=250, anchor=tk.CENTER)
    userNameEntryLabel.place(x=350, y=300, anchor=tk.CENTER)
    userNameEntry.place(x=485, y=350, anchor=tk.CENTER)
    userNameEntry.delete(0, tk.END)
    passwordEntryLabel.place(x=350, y=400, anchor=tk.CENTER)
    passwordEntry.place(x=485, y=450, anchor=tk.CENTER)
    passwordEntry.delete(0, tk.END)
    forgetPasswordButton.place(x=608, y=500, anchor=tk.CENTER)
    logInButton.place(x=330, y=550, anchor=tk.CENTER)
    newUserLabel.place(x=340, y=600, anchor=tk.CENTER)
    signUpButton.place(x=400, y=600, anchor=tk.CENTER)


def deleteAccountFunction():
    details = logInMessageLabel["text"]
    lst = details.split("\n")
    userName = lst[3][12:]
    data = DB.getDetails(userName)
    print(data)
    logInMessageLabel.place_forget()
    logOutButton.place_forget()
    deleteAccountButton.place_forget()
    forgetSQuesLabel.place_forget()
    forgetSAnsEntry.place_forget()
    forgetOkButton.place_forget()
    forgetBackButton.place_forget()
    sQues = data[5]
    sQuesLabel["text"] = sQues
    sQuesLabel.place(x=800, y=400, anchor=tk.CENTER)
    sAnsEntry.place(x=800, y=450, anchor=tk.CENTER)
    okButton.place(x=800, y=500, anchor=tk.CENTER)
    deleteBackButton.place(x=750, y=500, anchor=tk.CENTER)

    return


def deleteOkButtonFunction():
    details = logInMessageLabel["text"]
    lst = details.split("\n")
    userName = lst[3][12:]
    data = DB.getDetails(userName)
    print(data)
    logInMessageLabel.place_forget()
    logOutButton.place_forget()
    deleteAccountButton.place_forget()
    forgetSQuesLabel.place_forget()
    forgetSAnsEntry.place_forget()
    forgetOkButton.place_forget()
    forgetBackButton.place_forget()
    sAns = data[6]
    ans = sAnsEntry.get()
    if ans == sAns:
        DB.deleteUser(userName)
        logInLabel.place(x=330, y=250, anchor=tk.CENTER)
        userNameEntryLabel.place(x=350, y=300, anchor=tk.CENTER)
        userNameEntry.place(x=485, y=350, anchor=tk.CENTER)
        userNameEntry.delete(0, tk.END)
        passwordEntryLabel.place(x=350, y=400, anchor=tk.CENTER)
        passwordEntry.place(x=485, y=450, anchor=tk.CENTER)
        passwordEntry.delete(0, tk.END)
        forgetPasswordButton.place(x=608, y=500, anchor=tk.CENTER)
        logInButton.place(x=330, y=550, anchor=tk.CENTER)
        newUserLabel.place(x=340, y=600, anchor=tk.CENTER)
        signUpButton.place(x=400, y=600, anchor=tk.CENTER)
        deleteAccountButton.place_forget()
        sQuesLabel.place_forget()
        sAnsEntry.place_forget()
        okButton.place_forget()
        okButtonErrorLabel.place_forget()
        deleteBackButton.place_forget()
    else:
        okButtonErrorLabel.place(x=800, y=550, anchor=tk.CENTER)


def forgetPasswordFunction():
    global name
    uName = userNameEntry.get()
    if len(uName) == 0:
        return
    name = uName
    data = DB.getDetails(uName)
    sQues = data[5]
    sQuesLabel["text"] = sQues
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
    forgetSQuesLabel["text"] = sQues
    forgetSQuesLabel.place(x=800, y=400, anchor=tk.CENTER)
    forgetSAnsEntry.place(x=800, y=450, anchor=tk.CENTER)
    forgetOkButton.place(x=800, y=500, anchor=tk.CENTER)
    forgetBackButton.place(x=750, y=500, anchor=tk.CENTER)


def forgetOkButtonFunction():
    ans = forgetSAnsEntry.get()
    data = DB.getDetails(name)
    sAns = data[6]
    if ans == sAns:
        forgetSQuesLabel.place_forget()
        forgetSAnsEntry.place_forget()
        forgetOkButton.place_forget()
        forgetBackButton.place_forget()
        confirmLabel.place(x=800, y=350, anchor=tk.CENTER)
        forgetPwdEntry.place(x=800, y=400, anchor=tk.CENTER)
        forgetRPwdEntry.place(x=800, y=450, anchor=tk.CENTER)
        confirmButton.place(x=800, y=500, anchor=tk.CENTER)
        return
    else:
        forgetOkButtonErrorLabel["text"] = "Wrong Answer..."
        forgetOkButtonErrorLabel.place(x=800, y=550, anchor=tk.CENTER)


def confirmButtonFunction():
    forgetOkButtonErrorLabel.place_forget()
    pwd = forgetPwdEntry.get()
    rPwd = forgetRPwdEntry.get()
    if pwd != rPwd:
        forgetOkButtonErrorLabel["text"] = "Password does not match"
        forgetOkButtonErrorLabel.place(x=800, y=550, anchor=tk.CENTER)
        return
    if len(pwd) < 8:
        forgetOkButtonErrorLabel["text"] = "Minimum password length should be greater than 8..."
        forgetOkButtonErrorLabel.place(x=800, y=550, anchor=tk.CENTER)
        return
    count = 0
    for c in range(32, 65):
        if chr(c) in pwd:
            count += 1
            break
    if count == 0:
        for c in range(91, 97):
            if chr(c) in pwd:
                count += 1
                break
    if count == 0:
        forgetOkButtonErrorLabel["text"] = "Please Include Special Character in Password..."
        forgetOkButtonErrorLabel.place(x=800, y=550, anchor=tk.CENTER)
        return
    count = 0
    for c in range(65, 91):
        if chr(c) in pwd:
            count += 1
            break
    if count == 0:
        forgetOkButtonErrorLabel["text"] = "Please Include Uppercase Character in Password..."
        forgetOkButtonErrorLabel.place(x=800, y=550, anchor=tk.CENTER)
        return
    count = 0
    for c in range(97, 123):
        if chr(c) in pwd:
            count += 1
            break
    if count == 0:
        forgetOkButtonErrorLabel["text"] = "Please Include Lowercase Character in Password..."
        forgetOkButtonErrorLabel.place(x=800, y=550, anchor=tk.CENTER)
        return
    print(name)
    if pwd == rPwd:
        DB.updatePassword(name, pwd)
        firstNameLabel.place_forget()
        firstNameEntry.place_forget()
        lastNameLabel.place_forget()
        lastNameEntry.place_forget()
        emailIdLabel.place_forget()
        emailIdEntry.place_forget()
        mobileLabel.place_forget()
        mobileEntry.place_forget()
        dateOfBirthLabel.place_forget()
        dateOfBirthEntry.place_forget()
        securityQuestionsLabel.place_forget()
        securityQuestions.place_forget()
        securityQuesAnsLabel.place_forget()
        securityQuesAnsEntry.place_forget()
        registerButton.place_forget()
        backButton.place_forget()
        passwordLabel.place_forget()
        passwordEntry1.place_forget()
        reEntryPasswordLabel.place_forget()
        reEntryPasswordEntry.place_forget()
        registerErrorLabel.place_forget()
        deleteAccountButton.place_forget()
        sQuesLabel.place_forget()
        sAnsEntry.place_forget()
        okButton.place_forget()
        okButtonErrorLabel.place_forget()
        deleteBackButton.place_forget()
        forgetSQuesLabel.place_forget()
        forgetSAnsEntry.place_forget()
        forgetOkButton.place_forget()
        forgetBackButton.place_forget()
        forgetOkButtonErrorLabel.place_forget()
        confirmLabel.place_forget()
        forgetPwdEntry.place_forget()
        forgetRPwdEntry.place_forget()
        confirmButton.place_forget()
        logInLabel.place(x=330, y=250, anchor=tk.CENTER)
        userNameEntryLabel.place(x=350, y=300, anchor=tk.CENTER)
        userNameEntry.place(x=485, y=350, anchor=tk.CENTER)
        userNameEntry.delete(0, tk.END)
        passwordEntryLabel.place(x=350, y=400, anchor=tk.CENTER)
        passwordEntry.place(x=485, y=450, anchor=tk.CENTER)
        passwordEntry.delete(0, tk.END)
        forgetPasswordButton.place(x=608, y=500, anchor=tk.CENTER)
        logInButton.place(x=330, y=550, anchor=tk.CENTER)
        newUserLabel.place(x=340, y=600, anchor=tk.CENTER)
        signUpButton.place(x=400, y=600, anchor=tk.CENTER)
        return
    else:
        forgetOkButtonErrorLabel["text"] = "Password didn't matched..."
        forgetOkButtonErrorLabel.place(x=800, y=550, anchor=tk.CENTER)
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
logInLabel.place(x=330, y=250, anchor=tk.CENTER)
userNameEntryLabel = tk.Label(root, text="Username", bg="white", fg="black", font=("Helvetica", 15))
userNameEntryLabel.place(x=350, y=300, anchor=tk.CENTER)
userNameEntry = tk.Entry(root, width=40, font=("Helvetica", 13))
userNameEntry.place(x=485, y=350, anchor=tk.CENTER)
passwordEntryLabel = tk.Label(root, text="Password", bg="white", fg="black", font=("Helvetica", 15))
passwordEntryLabel.place(x=350, y=400, anchor=tk.CENTER)
passwordEntry = tk.Entry(root, width=40, font=("Helvetica", 13))
passwordEntry.place(x=485, y=450, anchor=tk.CENTER)
forgetPasswordButton = tk.Button(root, text="Forgot Password?", bg="white", fg="blue", font=("Helvetica", 10, "bold"), cursor="hand2", command=forgetPasswordFunction)
forgetPasswordButton.place(x=608, y=500, anchor=tk.CENTER)
logInButton = tk.Button(root, text="Log in", bg="white", fg="black", cursor="hand2", command=logInButtonFunction)
logInButton.place(x=330, y=550, anchor=tk.CENTER)
logInErrorLabel = tk.Label(root, text="User not found...", bg="white", fg="red", font=("Helvetica", 15, "bold"))
newUserLabel = tk.Label(root, text="New User", bg="white", fg="blue", font=("Helvetica", 10))
newUserLabel.place(x=340, y=600, anchor=tk.CENTER)
signUpButton = tk.Button(root, text="Sign Up", bg="white", fg="black", font=("Helvetica", 8), cursor="hand2", command=signUpFunction)
signUpButton.place(x=400, y=600, anchor=tk.CENTER)
firstNameLabel = tk.Label(root, text="Firstname", bg="white", fg="black", font=("Helvetica", 12))
firstNameEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
lastNameLabel = tk.Label(root, text="Lastname", bg="white", fg="black", font=("Helvetica", 12))
lastNameEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
emailIdLabel = tk.Label(root, text="Email", bg="white", fg="black", font=("Helvetica", 12))
emailIdEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
mobileLabel = tk.Label(root, text="Mobile No.", bg="white", fg="black", font=("Helvetica", 12))
mobileEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
dateOfBirthLabel = tk.Label(root, text="Date of Birth", bg="white", fg="black", font=("Helvetica", 12))
dateOfBirthEntry = DateEntry(root, width=42, bg="black", fg="white", year=2000)
securityQuestionsLabel = tk.Label(root, text="Security Question", bg="white", fg="black", font=("Helvetica", 12))
securityQuestions = ttk.Combobox(root, width=30, state="readonly", font=("Helvetica", 12))
securityQuestions["values"] = tuple(["What is your lastname?", "What is your Pet name?", "What is your nickname?"])
securityQuestions.current(0)
passwordLabel = tk.Label(root, text="Password", bg="white", fg="black", font=("Helvetica", 12))
passwordEntry1 = tk.Entry(root, width=30, font=("Helvetica", 12))
reEntryPasswordLabel = tk.Label(root, text="Re-enter Password", bg="white", fg="black", font=("Helvetica", 12))
reEntryPasswordEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
registerButton = tk.Button(root, text="Register", bg="white", fg="black", font=("Helvetica", 12), cursor="hand2", command=signUpRegisterFunction)
backButton = tk.Button(root, text="Back", fg="black", bg="white", font=("Helvetica", 12), cursor="hand2", command=signUpBackFunction)
securityQuesAnsLabel = tk.Label(root, text="Answer", fg="black", bg="white", font=("Helvetica", 12))
securityQuesAnsEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
registerErrorLabel = tk.Label(root, text="", bg="white", fg="red", font=("Helvetica", 12))
logInMessageLabel = tk.Label(root, text="", bg="white", fg="black", font=("Helvetica", 30))
logOutButton = tk.Button(root, text="Log Out", bg="white", fg="black", font=("Helvetica", 12), cursor="hand2", command=logOutButtonFunction)
deleteAccountButton = tk.Button(root, text="Delete Account", bg="white", fg="red", font=("Helvetica", 12), cursor="hand2", command=deleteAccountFunction)
sQuesLabel = tk.Label(root, text="", bg="white", fg="black", font=("Helvetica", 12))
sAnsEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
okButton = tk.Button(root, text="Ok", bg="white", fg="black", font=("Helvetica", 12), cursor="hand2", command=deleteOkButtonFunction)
okButtonErrorLabel = tk.Label(root, text="Incorrect Answer", bg="white", fg="black", font=("Helvetica", 12))
deleteBackButton = tk.Button(root, text="Back", bg="white", fg="black", font=("Helvetica", 12), cursor="hand2", command=signUpBackFunction)
forgetSQuesLabel = tk.Label(root, text="", bg="white", fg="black", font=("Helvetica", 12))
forgetSAnsEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
forgetOkButton = tk.Button(root, text="Ok", bg="white", fg="black", font=("Helvetica", 12), cursor="hand2", command=forgetOkButtonFunction)
forgetOkButtonErrorLabel = tk.Label(root, text="Incorrect Answer", bg="white", fg="red", font=("Helvetica", 12))
forgetBackButton = tk.Button(root, text="Back", bg="white", fg="black", font=("Helvetica", 12), cursor="hand2", command=signUpBackFunction)
forgetPwdEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
forgetRPwdEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
confirmLabel = tk.Label(root, text="Enter your password in the places given below", bg="white", fg="black", font=("Helvetica", 12))
confirmButton = tk.Button(root, text="Confirm", bg="white", fg="black", font=("Helvetica", 12), cursor="hand2", command=confirmButtonFunction)
root.mainloop()
