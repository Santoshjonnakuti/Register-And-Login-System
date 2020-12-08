from tkinter import *
import sqlite3

root = Tk()
root.title('Home_page')
root.geometry('300x300')

# Make a database of usernames and passwords

# # create a Database or connect to one
# conn = sqlite3.connect('my_database.db')
# # create cursor
# c = conn.cursor()
# # create table
#     # c.execute("""CREATE TABLE UsernamePassword(
#     #         username text,
#     #         password text
#     #         )""")
# # commit changes
# conn.commit()
# # close connection
# conn.close()

def DB_entries():
    global x
    # to print the values stored in the database

    # create a Database or connect to one
    conn = sqlite3.connect('my_database.db')
    # create cursor
    c = conn.cursor()

    # Query the database
    c.execute('SELECT *,oid FROM UsernamePassword')
    records = c.fetchall()  # OR .fetchone, .fetchmany(n)
    # print(records)

    # Loop through results
    x = ''
    for record in records:
        x += str(record)+'\n'

    print(x)
    conn.commit()
    conn.close()

def register_user():
    user = username.get()
    pasw = password.get()
    if len(user)<5 or len(pasw)<5:
        Label(screen1,text='len(inputs) should be >=5',fg='red').grid(row=5,column=1,columnspan=2)
        return

    # check if a record exists with the same username

    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()

    # Query the database
    c.execute('SELECT *,oid FROM UsernamePassword')
    records = c.fetchall()  # OR .fetchone, .fetchmany(n)

    # Loop through records
    for record in records:
        if record[0] == user:
            Label(screen1,text='__________User already exists___________',fg='red').grid(row=5,column=1)
            print('User already exists')
            return

    # if there exists, go back
    # else submit a record in the database
    c.execute('INSERT INTO UsernamePassword VALUES (:username,:password)',
        {
            'username':user,
            'password':pasw
        })
    Label(screen1,text='_________User successfully registered_________',fg='green').grid(row=5,column=1)
    conn.commit()
    conn.close()

    #clear the textboxes
    username.delete(0,END)
    password.delete(0,END)

def login_user():
    pass

def register():
    global username
    global password
    global screen1

    screen1 = Toplevel()
    screen1.title('Register_page')
    screen1.geometry('300x300')

    #create text boxes
    username = Entry(screen1,width=30)
    username.grid(row=1,column=1,padx=20)
    password = Entry(screen1,width=30)
    password.grid(row=2,column=1,padx=20)

    #create textbox labels
    Label(screen1,text='Enter your details:').grid(row=0,column=0,columnspan=2)
    Label(screen1,text='Username').grid(row=1,column=0)
    Label(screen1,text='Password').grid(row=2,column=0)

    # create register button
    Button(screen1,text='Register',command=register_user,width=20,).grid(row=3,column=0,columnspan=2)

    Button(screen1,text='Go Back',command=screen1.destroy,width=20).grid(row=4,column=0,columnspan=2)

def login():
    pass

frame = LabelFrame(root,padx=10,pady=10)
frame.pack(padx=10,pady=10)

Label(frame,text='Welcome').pack()
Label(frame,text='').pack() # to give a line in between
Button(frame,text='Log in',width=30,command=login).pack()
Label(frame,text='').pack()
Button(frame,text='register',width=30,command=register).pack()

Button(root,text='view entries(in the command prompt)',command=DB_entries).pack()

root.mainloop()
