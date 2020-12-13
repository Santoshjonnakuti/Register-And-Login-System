from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import sqlite3
root=Tk()
screen=Tk()
class login():
	def __init__(self,screen):
		self.screen=screen
		self.screen.title("LOGIN WINDOW")
		self.screen.geometry("500x500+800+0")
		title=Label(self.screen,text="LOGIN HERE",bd=0,font=("times new roman",20,"bold"),bg="white",fg="blue").place(x=140,y=10)
		email=Label(self.screen,text="EMAIL ADDRESS",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=40,y=70)
		self.txt_email=Entry(self.screen,font=("times new roman",15),bg="lightgray",width="27")
		self.txt_email.place(x=40,y=110)

		passw=Label(self.screen,text="PASSWORD",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=40,y=170)
		self.txt_passw=Entry(self.screen,font=("times new roman",15),bg="lightgray",width="27")
		self.txt_passw.place(x=40,y=210)

		btn_reg=Button(self.screen,text="Dont have an account?,register here..",cursor="hand2",bd=0,fg="red",bg="white",command=self.new_account).place(x=40,y=250)
		btn_login=Button(self.screen,text="LOGIN",fg="green",bg="white",width="15",cursor="hand2",command=self.login_data).place(x=40,y=300)

	def login_data(self):
		if self.txt_email.get()=="" or self.txt_passw.get()=="":
			messagebox.showerror("Error","email and password are compulsory",parent=self.screen)
		else:
			try:
				con=sqlite3.connect("database.db")
				cur=con.cursor()
				cur.execute("SELECT * FROM user_table WHERE email=? and password=?",(self.txt_email.get(),self.txt_passw.get()))
				row=cur.fetchone()
				if row==None:
					messagebox.showerror("Error","invalid email or password",parent=self.screen)
					self.wipe()
				else:
					messagebox.showinfo("Success","welcome, your login attempt is sucessful",parent=self.screen)
					con.close()
					self.wipe()

			except Exception as e:
				messagebox.showerror("Error",e,parent=self.screen)
	def wipe(self):
		self.txt_email.delete(0,END)
		self.txt_passw.delete(0,END)

	def new_account(self):
		self.screen.destroy()

class Register(login):
    def __init__(self,root):
        self.root=root
        self.root.title("REGISTRATION WINDOW")
        self.root.geometry("1000x700+0+0")
        title=Label(self.root,text="REGISTRATION FORM",bd=0,font=("times new roman",20,"bold"),bg="white",fg="blue").place(x=300,y=30)
        #adding background image
        #bg = ImageTk.photoImage(file="camera roll/bg.jpg")
        #img=Label(root,image=bg).place()

        #.........in row 1.....
        f_name = Label(self.root, text="First Name", font=("times new roman", 15, "bold"), bg="white",fg="black").place(x=150, y=90)
        self.txt_fname = Entry(self.root,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=150,y=130,width=250)

        last_name = Label(self.root, text="Last name",font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=550, y=90)
        self.txt_lname = Entry(self.root, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=550, y=130, width=250)

        # .........in row 2.....
        contact = Label(self.root, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="black").place( x=150, y=170)
        self.txt_contact = Entry(self.root, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=150, y=200, width=250)

        email = Label(self.root, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=550, y=170)
        self.txt_email = Entry(self.root, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=550, y=200, width=250)

        # .........in row 3.....
        question= Label(self.root, text="Security question", font=("times new roman", 15, "bold"), bg="white",fg="black").place(x=150, y=250)
        self.cmb_quest =ttk.Combobox(root, font=("times new roman", 13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("select","your pet name","your school name","your best friend name")
        self.cmb_quest.place(x=150, y=280, width=250)
        self.cmb_quest.current(0)

        answer = Label(self.root, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=550,y=250)
        self.txt_answer= Entry(self.root, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=550, y=280, width=250)

        # .........in row 4......
        password= Label(self.root, text="Password", font=("times new roman", 15, "bold"), bg="white",fg="black").place(x=150, y=330)
        self.txt_password =Entry(self.root, font=("times new roman", 13), bg="lightgray")
        self.txt_password.place(x=150, y=360, width=250)

        cpassword = Label(self.root, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=550,y=330)
        self.txt_cpassword= Entry(self.root, font=("times new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=550, y=360, width=250)
        register_button=Button(self.root,text="REGISTER HERE",font=("times new roman",15),cursor="hand2",bg="white",fg="red",command=self.register_data).place(x=350,y=450,width=250)

        account=Label(self.root,text="you can login by clicking the button below",font=("times new roman",15,"bold")).place(x=300,y=520)
        login_button=Button(self.root,text="LOGIN HERE",font=("times new roman",15),cursor="hand2",bg="white",fg="green",command=self.call).place(x=350,y=580,width=250)

    def call(self):
    	super().__init__(screen)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="select" or self.txt_contact.get()=="" or self.txt_answer.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("error","all fields are required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("error","password and confirm password must be same",parent=self.root)
        else:
            try:
                 con = sqlite3.connect("database.db")
                 #create a cursor
                 cur = con.cursor()
                 #create a table
                 cur.execute("""CREATE TABLE IF NOT EXISTS user_table(
                 f_name text,
                 last_name text,
                 contact int,
                 email text,
                 question text,
                 answer text,
                 password text)""")
                 cur.execute('''SELECT * FROM user_table WHERE email=?''',(self.txt_email.get(),))
                 row=cur.fetchone()
                 #print(row)
                 if row!=None:
                    messagebox.showerror("Error","user already exists,please use another email",parent=self.root)
                 else:
                    cur.execute("INSERT INTO user_table VALUES(?,?,?,?,?,?,?)",
                                   (self.txt_fname.get(),
                                    self.txt_lname.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.cmb_quest.get(),
                                    self.txt_answer.get(),
                                    self.txt_password.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","register successful",parent=self.root)
                    self.clear()
            except Exception as e:
                 messagebox.showerror("error",e,parent=self.root)
obj=Register(root)
root.mainloop()		