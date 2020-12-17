import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
from tkcalendar import DateEntry

import DB
import DB1

global name, data, string


def Function(button):
    global name, data, string
    text = button["text"]
    if text == "Forgot Password?":
        string = "Forgot Password?"
        name = Entry1.get()
        if len(name) == 0:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Username cannot be empty..."
            ErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
            return
        else:
            data = DB.getDetails(name)
            if len(data) == 0:
                ErrorLabel["fg"] = "red"
                ErrorLabel["text"] = "User not found..."
                ErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
                return
            else:
                Label2.place_forget()
                Label3.place_forget()
                Entry2.place_forget()
                Button3.place_forget()
                ErrorLabel.place_forget()
                Label1["text"] = data[5]
                Label1.place(x=800, y=400, anchor=tk.CENTER)
                Entry1.delete(0, tk.END)
                Entry1.place(x=800, y=450, anchor=tk.CENTER)
                Button1["text"] = "Ok"
                Button1.place(x=800, y=500, anchor=tk.CENTER)
                Button2["text"] = "Back"
                Button2["font"] = ("Helvetica", 10)
                Button2["fg"] = "black"
                Button2.place(x=750, y=500, anchor=tk.CENTER)
                return
    elif text == "Delete Account":
        string = "Delete Account"
        showPasswordButton.place_forget()
        recentLoginLabel.place_forget()
        cancelButton.place_forget()
        detailsLabel.place_forget()
        Label2.place_forget()
        Label3.place_forget()
        Entry2.place_forget()
        Button3.place_forget()
        ErrorLabel.place_forget()
        messageListBox.place_forget()
        applicationLabel.place_forget()
        applicationEntry.place_forget()
        addButton.place_forget()
        updateButton.place_forget()
        deleteButton.place_forget()
        ErrorLabel1.place_forget()
        searchButton.place_forget()
        searchEntry.place_forget()
        Label1["text"] = data[5]
        Label1.place(x=800, y=400, anchor=tk.CENTER)
        Entry1.delete(0, tk.END)
        Entry1.place(x=800, y=450, anchor=tk.CENTER)
        Button1["text"] = "Ok"
        Button1.place(x=800, y=500, anchor=tk.CENTER)
        Button2["text"] = "Back"
        Button2["font"] = ("Helvetica", 10)
        Button2["fg"] = "black"
        Button2.place(x=750, y=500, anchor=tk.CENTER)
        return
    elif text == "Back" or text == "Logout":
        recentLoginLabel.place_forget()
        ErrorLabel.place_forget()
        cancelButton.place_forget()
        detailsLabel.place_forget()
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
        passwordLabel.place_forget()
        passwordEntry1.place_forget()
        reEntryPasswordLabel.place_forget()
        reEntryPasswordEntry.place_forget()
        addButton.place_forget()
        updateButton.place_forget()
        deleteButton.place_forget()
        applicationLabel.place_forget()
        applicationEntry.place_forget()
        ErrorLabel1.place_forget()
        messageListBox.place_forget()
        searchEntry.place_forget()
        searchButton.place_forget()
        backGroundLabel["image"] = bgImage
        Label1["text"] = "Log in"
        Label1.place(x=332, y=250, anchor=tk.CENTER)
        Label2["text"] = "Email"
        Label2.place(x=330, y=300, anchor=tk.CENTER)
        Entry1.delete(0, tk.END)
        Entry1.place(x=485, y=350, anchor=tk.CENTER)
        Label3["text"] = "Password"
        Label3.place(x=350, y=400, anchor=tk.CENTER)
        Entry2.delete(0, tk.END)
        Entry2.place(x=485, y=450, anchor=tk.CENTER)
        showPasswordButton["text"] = "Show Password"
        showPasswordButton.place(x=700, y=450, anchor=tk.CENTER)
        Button1["text"] = "Log in"
        Button1.place(x=327, y=550, anchor=tk.CENTER)
        Button2["text"] = "Forgot Password?"
        Button2["font"] = ("Helvetica", 10, "bold")
        Button2["fg"] = "blue"
        Button2.place(x=608, y=500, anchor=tk.CENTER)
        Button3["text"] = "Don't have an account? Sign Up"
        Button3.place(x=400, y=600, anchor=tk.CENTER)
        if text == "Logout":
            message = DB1.showAll(data[0])
            message = message.split("\n")
            messageListBox.delete(0, len(message))
            DB.updateLastLogin(data[0])
        return
    elif text == "Ok":
        ans = Entry1.get()
        if ans == data[6]:
            if string == "Forgot Password?":
                ErrorLabel.place_forget()
                Label1["text"] = "Enter your password in the places given below"
                Label1.place(x=800, y=350, anchor=tk.CENTER)
                Entry1.delete(0, tk.END)
                Entry1.place(x=800, y=400, anchor=tk.CENTER)
                Entry2.delete(0, tk.END)
                Entry2.place(x=800, y=450, anchor=tk.CENTER)
                Button1["text"] = "Confirm"
                Button1.place(x=800, y=500, anchor=tk.CENTER)
                Button2["text"] = "Back"
                Button2.place(x=740, y=500, anchor=tk.CENTER)
                return
            elif string == "Delete Account":
                DB.deleteUser(data[0])
                ErrorLabel["text"] = "Successfully Deleted your Account...\nPlease go back..."
                ErrorLabel.place(x=800, y=550, anchor=tk.CENTER)
        else:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Wrong Answer..."
            ErrorLabel.place(x=800, y=550, anchor=tk.CENTER)
            return
    elif text == "Confirm":
        ErrorLabel.place_forget()
        pwd = Entry1.get()
        rePwd = Entry2.get()
        if pwd != rePwd:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Password does not match"
            ErrorLabel.place(x=800, y=550, anchor=tk.CENTER)
            return
        if len(pwd) < 8:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Minimum password length should be greater than 8..."
            ErrorLabel.place(x=800, y=550, anchor=tk.CENTER)
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
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Please Include Special Character in Password..."
            ErrorLabel.place(x=800, y=550, anchor=tk.CENTER)
            return
        count = 0
        for c in range(65, 91):
            if chr(c) in pwd:
                count += 1
                break
        if count == 0:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Please Include Uppercase Character in Password..."
            ErrorLabel.place(x=800, y=550, anchor=tk.CENTER)
            return
        count = 0
        for c in range(97, 123):
            if chr(c) in pwd:
                count += 1
                break
        if count == 0:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Please Include Lowercase Character in Password..."
            ErrorLabel.place(x=800, y=550, anchor=tk.CENTER)
            return
        if pwd == rePwd:
            DB.updatePassword(name, pwd)
            ErrorLabel["fg"] = "green"
            ErrorLabel["text"] = "Password Updated Successfully...\nGo back and Please Login again..."
            Entry1.delete(0, tk.END)
            Entry2.delete(0, tk.END)
            ErrorLabel.place(x=800, y=550, anchor=tk.CENTER)
            return
    elif text == "Log in":
        uName = Entry1.get()
        pWord = Entry2.get()
        if len(uName) == 0:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Username cannot be Empty..."
            ErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
            return
        elif len(pWord) == 0:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Password cannot be Empty..."
            ErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
            return
        data = DB.getDetails(uName)
        if len(data) == 0:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "User not Found..."
            ErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
            return
        elif data[0] == uName and data[7] != pWord:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Incorrect Password..."
            ErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
            return
        elif data[0] == uName and data[7] == pWord:
            backGroundLabel["image"] = bgImage2
            backGroundLabel.pack()
            Label1.place_forget()
            Label2.place_forget()
            Label3.place_forget()
            Entry1.place_forget()
            Entry2.place_forget()
            ErrorLabel.place_forget()
            Button3.place_forget()
            showPasswordButton.place_forget()
            Entry2["show"] = ""
            searchEntry.place(x=200, y=280, anchor=tk.CENTER)
            searchButton.place(x=370, y=280, anchor=tk.CENTER)
            addButton.place(x=80, y=200, anchor=tk.CENTER)
            updateButton.place(x=180, y=200, anchor=tk.CENTER)
            deleteButton.place(x=280, y=200, anchor=tk.CENTER)
            applicationLabel.place(x=150, y=50, anchor=tk.CENTER)
            applicationEntry.place(x=450, y=50, anchor=tk.CENTER)
            Label2["text"] = "Username"
            Label2.place(x=200, y=100, anchor=tk.CENTER)
            Entry1.delete(0, tk.END)
            Entry1.place(x=450, y=100, anchor=tk.CENTER)
            Label3.place(x=200, y=150, anchor=tk.CENTER)
            Entry2.delete(0, tk.END)
            Entry2.place(x=450, y=150, anchor=tk.CENTER)
            message = DB1.showAll(data[0])
            message = message.split("\n")
            for i in range(len(message)):
                messageListBox.insert(i, message[i])
            messageListBox.place(x=350, y=550, anchor=tk.CENTER)
            Button1["text"] = "Logout"
            Button1.place(x=1400, y=100, anchor=tk.CENTER)
            Button2["text"] = "Delete Account"
            Button2["fg"] = "red"
            Button2["command"] = lambda: Function(Button2)
            Button2.place(x=1400, y=700, anchor=tk.CENTER)
            detailsLabel["text"] = "Welcome {} {}!\nDate of Birth : {}\nMobile : {}\nEmail : {}".format(data[1], data[2], data[4], data[3], data[0])
            detailsLabel.place(x=1000, y=400, anchor=tk.CENTER)
            recentLoginLabel["text"] = "Recent Login : " + data[8]
            recentLoginLabel.place(x=1380, y=50, anchor=tk.CENTER)
            return
    elif text == "Don't have an account? Sign Up":
        backGroundLabel.pack_forget()
        backGroundLabel["image"] = bgImage1
        backGroundLabel.pack()
        ErrorLabel.place_forget()
        Label2.place_forget()
        Label3.place_forget()
        Entry1.place_forget()
        Entry2.place_forget()
        Button3.place_forget()
        Label1["text"] = "Please Enter Your Details Below"
        Label1.place(x=600, y=100, anchor=tk.CENTER)
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
        Button1["text"] = "Register"
        Button1.place(x=600, y=600, anchor=tk.CENTER)
        Button2["fg"] = "black"
        Button2["text"] = "Back"
        Button2.place(x=500, y=600, anchor=tk.CENTER)
        return
    elif text == "Register":
        fName = firstNameEntry.get()
        lName = lastNameEntry.get()
        eMail = emailIdEntry.get()
        mobile = mobileEntry.get()
        dob = dateOfBirthEntry.get()
        sQues = securityQuestions.get()
        sAns = securityQuesAnsEntry.get()
        pwd = passwordEntry1.get()
        rePwd = reEntryPasswordEntry.get()
        mbStr = str(mobile)
        if len(fName) == 0 or len(lName) == 0 or len(eMail) == 0 or len(mbStr) == 0 or len(sQues) == 0 or len(
                sAns) == 0 or len(pwd) == 0 or len(rePwd) == 0:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Please Fill all the above Entries..."
            ErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
            return
        if len(mbStr) != 10:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Invalid Mobile Number..."
            ErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
            return
        try:
            mbStr = int(mbStr)
            pass
        except ValueError:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Invalid Mobile Number..."
            ErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
            return
        if pwd != rePwd:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Password does not match"
            ErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
            return
        if len(pwd) < 8:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Minimum password length should be greater than 8..."
            ErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
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
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Please Include Special Character in Password..."
            ErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
            return
        count = 0
        for c in range(65, 91):
            if chr(c) in pwd:
                count += 1
                break
        if count == 0:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Please Include Uppercase Character in Password..."
            ErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
            return
        count = 0
        for c in range(97, 123):
            if chr(c) in pwd:
                count += 1
                break
        if count == 0:
            ErrorLabel["fg"] = "red"
            ErrorLabel["text"] = "Please Include Lowercase Character in Password..."
            ErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
            return
        fName = fName[0].upper() + fName[1:]
        lName = lName[0].upper() + lName[1:]
        DB.newUser(eMail, fName, lName, mbStr, dob, sQues, sAns, pwd)
        ErrorLabel["fg"] = "green"
        ErrorLabel["text"] = "Successfully Registered...\nPlease go back and Log in..."
        firstNameEntry.delete(0, tk.END)
        lastNameEntry.delete(0, tk.END)
        emailIdEntry.delete(0, tk.END)
        mobileEntry.delete(0, tk.END)
        dateOfBirthEntry.delete(0, tk.END)
        securityQuestions.delete(0, tk.END)
        securityQuesAnsEntry.delete(0, tk.END)
        passwordEntry1.delete(0, tk.END)
        reEntryPasswordEntry.delete(0, tk.END)
        ErrorLabel.place(x=500, y=650, anchor=tk.CENTER)
    elif text == "Add":
        application = applicationEntry.get().lower()
        uname = Entry1.get()
        pwd = Entry2.get()
        user = data[0]
        message = DB1.addUser(user, application, uname, pwd)
        msg = DB1.showAll(data[0])
        msg = msg.split("\n")
        messageListBox.delete(0, len(msg))
        for i in range(len(msg)):
            messageListBox.insert(i, msg[i])
        messageListBox.place(x=350, y=550, anchor=tk.CENTER)
        if message == "Successfully Added...":
            applicationEntry.delete(0, tk.END)
            Entry1.delete(0, tk.END)
            Entry2.delete(0, tk.END)
            ErrorLabel1["fg"] = "green"
        else:
            ErrorLabel1["fg"] = "red"
        ErrorLabel1["text"] = message
        ErrorLabel1.place(x=300, y=250, anchor=tk.CENTER)
        return
    elif text == "Update":
        application = applicationEntry.get().lower()
        uname = Entry1.get()
        pwd = Entry2.get()
        user = data[0]
        message = DB1.updateUser(user, application, uname, pwd)
        msg = DB1.showAll(data[0])
        msg = msg.split("\n")
        messageListBox.delete(0, len(msg))
        for i in range(len(msg)):
            messageListBox.insert(i, msg[i])
        messageListBox.place(x=350, y=550, anchor=tk.CENTER)
        if message == "Successfully Updated...":
            applicationEntry.delete(0, tk.END)
            Entry1.delete(0, tk.END)
            Entry2.delete(0, tk.END)
            ErrorLabel1["fg"] = "green"
        else:
            ErrorLabel1["fg"] = "red"
        ErrorLabel1["text"] = message
        ErrorLabel1.place(x=300, y=250, anchor=tk.CENTER)
        return
    elif text == "Delete":
        application = applicationEntry.get()
        user = data[0]
        message = DB1.deleteUser(user, application.lower())
        msg = DB1.showAll(data[0])
        msg = msg.split("\n")
        messageListBox.delete(0, len(msg))
        for i in range(len(msg)):
            messageListBox.insert(i, msg[i])
        messageListBox.place(x=350, y=550, anchor=tk.CENTER)
        if message == "Successfully Deleted...":
            applicationEntry.delete(0, tk.END)
            Entry1.delete(0, tk.END)
            Entry2.delete(0, tk.END)
            ErrorLabel1["fg"] = "green"
        else:
            ErrorLabel1["fg"] = "red"
        ErrorLabel1["text"] = message
        ErrorLabel1.place(x=300, y=250, anchor=tk.CENTER)
        return
    elif text == "Search":
        ErrorLabel1.place_forget()
        app = searchEntry.get().lower()
        if app == "":
            ErrorLabel1["fg"] = "red"
            ErrorLabel1["text"] = "Application name cannot be empty..."
            ErrorLabel1.place(x=300, y=250, anchor=tk.CENTER)
            return
        searchButton.place(x=400, y=280, anchor=tk.CENTER)
        cancelButton.place(x=370, y=280, anchor=tk.CENTER)
        msg = DB1.showAll(data[0])
        msg = msg.split("\n")
        stri = "Application" + (" "*29) + "Username" + (" "*32) + "Password" + (" "*32) + "\n"
        for line in msg[1:]:
            if app in line:
                stri += line + "\n"
            else:
                continue
        if stri == "Application" + (" "*29) + "Username" + (" "*32) + "Password" + (" "*32) + "\n":
            stri += "Not found..."
        stri = stri.split("\n")
        messageListBox.delete(0, len(msg))
        for i in range(len(stri)):
            messageListBox.insert(i, stri[i])
        messageListBox.place(x=350, y=550, anchor=tk.CENTER)
        return
    elif text == "Cancel":
        cancelButton.place_forget()
        searchEntry.delete(0, tk.END)
        searchButton.place(x=370, y=280, anchor=tk.CENTER)
        msg = DB1.showAll(data[0])
        msg = msg.split("\n")
        messageListBox.delete(0, len(msg))
        for i in range(len(msg)):
            messageListBox.insert(i, msg[i])
        messageListBox.place(x=350, y=550, anchor=tk.CENTER)
        return
    elif text == "Show Password":
        button["text"] = "Hide Password"
        button["image"] = HidePasswordImage
        Entry2["show"] = ""
        return
    elif text == "Hide Password":
        Entry2["show"] = "*"
        button["text"] = "Show Password"
        button["image"] = showPasswordImage
        return


root = tk.Tk()
root.title("My Space")
root.iconbitmap("Icon.ico")
root.geometry("1500x800")
bgImage = ImageTk.PhotoImage(Image.open('Background.jpg'))
bgImage1 = ImageTk.PhotoImage(Image.open('Background1.jpg'))
bgImage2 = ImageTk.PhotoImage(Image.open('Background2.jpg'))
backGroundLabel = tk.Label(root, image=bgImage)
backGroundLabel.pack()
Label1 = tk.Label(root, text="Log in", bg="white", fg="black", font=("Helvetica", 15))
Label1.place(x=332, y=250, anchor=tk.CENTER)
Label2 = tk.Label(root, text="Email", bg="white", fg="black", font=("Helvetica", 15))
Label2.place(x=330, y=300, anchor=tk.CENTER)
Entry1 = tk.Entry(root, width=40, font=("Helvetica", 13))
Entry1.place(x=485, y=350, anchor=tk.CENTER)
Label3 = tk.Label(root, text="Password", bg="white", fg="black", font=("Helvetica", 15))
Label3.place(x=350, y=400, anchor=tk.CENTER)
Entry2 = tk.Entry(root, width=40, font=("Helvetica", 13), show="*")
Entry2.place(x=485, y=450, anchor=tk.CENTER)
Button1 = tk.Button(root, text="Log in", bg="white", fg="black", compound="left", cursor="hand2", command=lambda: Function(Button1))
Button1.place(x=327, y=550, anchor=tk.CENTER)
Button2 = tk.Button(root, text="Forgot Password?", bg="white", fg="blue", cursor="hand2", font=("Helvetica", 10, "bold"), command=lambda: Function(Button2))
Button2.place(x=608, y=500, anchor=tk.CENTER)
Button3 = tk.Button(root, text="Don't have an account? Sign Up", fg="blue", bg="white", font=("Helvetica", 10), cursor="hand2", command=lambda: Function(Button3))
Button3.place(x=400, y=600, anchor=tk.CENTER)
showPasswordImage = tk.PhotoImage(file="ShowPassword.png")
HidePasswordImage = tk.PhotoImage(file="HidePassword.png")
showPasswordButton = tk.Button(root, text="Show Password", bg="white", fg="black", image=showPasswordImage, command=lambda: Function(showPasswordButton))
showPasswordButton.place(x=700, y=450, anchor=tk.CENTER)
ErrorLabel = tk.Label(root, text="", fg="red", bg="white", font=("Helvetica", 15, "bold"))
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
securityQuesAnsLabel = tk.Label(root, text="Answer", fg="black", bg="white", font=("Helvetica", 12))
securityQuesAnsEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
passwordLabel = tk.Label(root, text="Password", bg="white", fg="black", font=("Helvetica", 12))
passwordEntry1 = tk.Entry(root, width=30, font=("Helvetica", 12))
reEntryPasswordLabel = tk.Label(root, text="Re-enter Password", bg="white", fg="black", font=("Helvetica", 12))
reEntryPasswordEntry = tk.Entry(root, width=30, font=("Helvetica", 12))
addButton = tk.Button(root, text="Add", bg="white", fg="green", font=("Helvetica", 12), cursor="hand2", command=lambda: Function(addButton))
updateButton = tk.Button(root, text="Update", bg="white", fg="blue", font=("Helvetica", 12), cursor="hand2", command=lambda: Function(updateButton))
deleteButton = tk.Button(root, text="Delete", bg="white", fg="red", font=("Helvetica", 12), cursor="hand2", command=lambda: Function(deleteButton))
applicationLabel = tk.Label(root, text="Application/Website Name", fg="black", bg="white", font=("Helvetica", 12))
applicationEntry = tk.Entry(root, width="40", fg="black", bg="white", font=("Helvetica", 12))
ErrorLabel1 = tk.Label(root, text="", bg="white", fg="red", font=("Helvetica", 12, "bold"))
messageListBox = tk.Listbox(root, bg="white", fg="black", font=("Helvetica", 10), height=28, width=80)
searchEntry = tk.Entry(root, width=30, font=("Helvetica", 12), bg="white", fg="black")
searchImage = tk.PhotoImage(file="Search.png")
searchButton = tk.Button(root, text="Search", bg="white", fg="black", font=("Helvetica", 10), cursor="hand2", image=searchImage, command=lambda: Function(searchButton))
cancelImage = tk.PhotoImage(file="Cancel.png")
cancelButton = tk.Button(root, text="Cancel", bg="white", fg="black", font=("Helvetica", 10), cursor="hand2", image=cancelImage, command=lambda: Function(cancelButton))
detailsLabel = tk.Label(root, text="", bg="white", fg="green", font=("Brush Script M7", 20))
recentLoginLabel = tk.Label(root, text="Recent Login : None", bg="white", fg="black", font=("Helvetica", 12))
root.mainloop()
