#--------------------------x-rtSaurav-x--------------------------------#

from tkinter import *
import sqlite3
import os
root=Tk()
root.title('LOGIN PAGE')

#variables
USERNAME = StringVar()
PASSWORD = StringVar()
NAAM=StringVar()
EMAIL=StringVar()
CONTACT=StringVar()
PWD=StringVar()
ADMIN=StringVar()
PASSW=StringVar()
def power():
    #link to the next page after successful login
    print("login Successful")
    pass
    

def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("WELCOME To OUR WEB")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)
    
def Back():
    Home.destroy()
    root.deiconify()
#----------------------------------------------------------------------------------------------------------------------------
def register():
    if(NAAM.get()=="" or EMAIL.get=="" or CONTACT.get()=="" or PWD.get()==""):
        lbl_text2.config(text="Please complete the required field!", fg="red")
    global cursor,conn
    conn = sqlite3.connect('register.csv') #name of the csv file
    cursor = conn.cursor()
    
     # Insert a row of data
    try:
        cursor.execute('''INSERT INTO forms VALUES (?,?,?,?)''',(NAAM.get(),EMAIL.get(),CONTACT.get(),PWD.get()))
    except:
        # Create table 
        conn.execute('''CREATE TABLE forms (name text, email text,Contact real, password text)''') #should be created only if table does not exist
        cursor.execute('''INSERT INTO forms VALUES (?,?,?,?)''',(NAAM.get(),EMAIL.get(),CONTACT.get(),PWD.get()))
    # Save (commit) the changes 
    conn.commit() 
    # We can also close the connection if we are done with it.
     # Just be sure any changes have been committed or they will be lost.
    NAAM.set("")
    EMAIL.set("")
    CONTACT.set("")
    PWD.set("")
    
    




#------------------------------------------------------------------



#login functions

def Login(event=None):
    #register()
    print(USERNAME.get(),PASSWORD.get())
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        conn = sqlite3.connect('register.csv')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM forms WHERE `name` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("") 
        cursor.close()
        conn.close()
        
def welcome():
    if ADMIN.get()=='SAURAV' and PASSW.get()=='rt25': #made externally for admin login
        HomeWindow()
        ADMIN.set("")
        PASSW.set("")
    else:
        lbl_text3.config(text="Permission Denied", fg="red")
        ADMIN.set("")
        PASSW.set("")
    

#frames
Top = Frame(root, bd=2,borderwidth=5,relief=RAISED)
Top.pack(side=TOP, fill=X)

Form = Frame(root, height=15)
Form.pack(side=TOP, pady=20)

Form2 = Frame(root, height=150,width=150,borderwidth=5,relief=RAISED,bg='lavender')
Form2.pack(side=LEFT,anchor='nw',pady=35,padx=35,fill='y')

Form3=Frame(root,bd=5,height=150,width=150,borderwidth=5,relief=SUNKEN,bg='tomato')
Form3.pack(side=LEFT,anchor='n',pady=35,padx=35,fill='y')

Form4= Frame(root,bd=5,height=150,width=150,borderwidth=5,relief=RAISED,bg='light green')
Form4.pack(side=LEFT,anchor='s',pady=35,padx=35,fill='y')


#labels

#login

lbl_title = Label(Top, text = "JoinEvents.com", font=('Cooper Black', 24),fg='red',bg='lavender')
lbl_title.pack(fill=X)

lbl_logon=Label(Form2,text='Registered users',fg='blue',font=('Comic Sans MS',18),bg='lavender')
lbl_logon.grid(row=0)

lbl_username = Label(Form2, text = "Username:", font=('Comic Sans MS', 14), bd=10,bg='lavender')
lbl_username.grid(row=1, sticky="e")

lbl_password = Label(Form2, text = "Password:", font=('Comic Sans MS', 14), bd=10,bg='lavender')
lbl_password.grid(row=2, sticky="e")

lbl_text = Label(Form2,bg='lavender')
lbl_text.grid(row=3, columnspan=2)

#registration

lbl_reg=Label(Form3,text='Register here:',fg='blue',font=('Comic Sans MS',18),bg='tomato')
lbl_reg.grid(row=0)

lbl_name=Label(Form3,text="Name:",font=('Comic Sans MS',14),bd=15,bg='tomato')
lbl_name.grid(row=1,sticky='e')

lbl_email=Label(Form3,text="Email:",font=('Comic Sans MS',14),bd=15,bg='tomato')
lbl_email.grid(row=2,sticky='e')

lbl_cntact=Label(Form3,text="Contact No.:",font=('Comic Sans MS',14),bd=15,bg='tomato')
lbl_cntact.grid(row=3,sticky='e')

lbl_passw=Label(Form3,text="Password:",font=('Comic Sans MS',14),bd=15,bg='tomato')
lbl_passw.grid(row=4,sticky='e')

lbl_text2 = Label(Form3,bg='tomato',padx=2,pady=2)
lbl_text2.grid(row=8, columnspan=2)


#  ADMIN_LOGIN

lbl_adm=Label(Form4,text='Admin Login:',fg='blue',font=('Comic Sans MS',18),bg='light green')
lbl_adm.grid(row=0)


lbl_id=Label(Form4,text="Admin ID:",font=('Comic Sans MS',14),bd=10,bg='light green')
lbl_id.grid(row=1,sticky='e')

lbl_pass=Label(Form4,text="Password:",font=('Comic Sans MS',14),bd=10,bg='light green')
lbl_pass.grid(row=2,sticky='e')

lbl_text3 = Label(Form4,bg='light green',padx=2,pady=2)
lbl_text3.grid(row=8, columnspan=2)


#entry

username = Entry(Form2, textvariable=USERNAME, font=(14),bg='lavender')
username.grid(row=1, column=1,padx=10)

password = Entry(Form2, textvariable=PASSWORD, show="*", font=(14),bg='lavender')
password.grid(row=2, column=1)

name=Entry(Form3,textvariable=NAAM, font=(14),bg='lavender')
name.grid(row=1,column=2,padx=10)

email=Entry(Form3,textvariable=EMAIL, font=(14),bg='lavender')
email.grid(row=2,column=2,padx=10)

contact=Entry(Form3,textvariable=CONTACT, font=(14),bg='lavender')
contact.grid(row=3,column=2,padx=10)

password=Entry(Form3,textvariable=PWD,show='@', font=(10),bg='lavender')
password.grid(row=4,column=2,padx=10)

admn=Entry(Form4,textvariable=ADMIN, font=(14),bg='lavender')
admn.grid(row=1,column=2,padx=4,pady=4)

pas=Entry(Form4,textvariable=PASSW,show='*', font=(10),bg='lavender')
pas.grid(row=2,column=2,padx=4,pady=4)


# BUTTON

login=Button(Form2,text='LOGIN',font=('Arial Rounded MT Bold',10),bg='lime',fg='red',command=Login)
login.grid(row=4,column=1)

submit=Button(Form3,text='SUBMIT',font=('Arial Rounded MT Bold',10),bg='gold',fg='red',command=register)
submit.grid(row=7,column=2)

log=Button(Form4,text='LOGIN',font=('Arial Rounded MT Bold',10),bg='gold',fg='red',command=welcome)
log.grid(row=6,column=2)

root.mainloop()