from tkinter import *
from tkinter import ttk    #here ttk is a module of tkinter package
from tkinter import messagebox,simpledialog
import dbconnect as db
from datetime import datetime
from PIL import ImageTk,Image    # pip install pillow
from tkinter import filedialog
import os

win=Tk()
win.resizable(width=False,height=False)
win.state('zoomed')
bgclr='#00ff80'
win.configure(bg=bgclr)
title=Label(win,text='Bank Automation',font=('',50,'bold'),fg='black',bg=bgclr)
title.pack()

def homescreen(prvfrm=None):
    if(prvfrm!=None):
        prvfrm.destroy()
    frm=Frame(win,bg='yellow')
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    user_lbl=Label(frm,text='Username:',font=('',20,''),fg='blue',bg='yellow')
    user_lbl.place(x=400,y=100)

    pass_lbl=Label(frm,text='Password:',font=('',20,''),fg='blue',bg='yellow')
    pass_lbl.place(x=400,y=150)

    type_lbl=Label(frm,text='Usertype:',font=('',20,''),fg='blue',bg='yellow')
    type_lbl.place(x=400,y=200)

    user_entry=Entry(frm,bg='powderblue',bd=5,width=15,font=('',15,''))
    user_entry.place(x=580,y=100)
    user_entry.focus()

    pass_entry=Entry(frm,show='*',bg='powderblue',bd=5,width=15,font=('',15,''))
    pass_entry.place(x=580,y=150)

    type_dropdown=ttk.Combobox(frm,values=['User','Admin'],font=('',11,''))
    type_dropdown.current(0)
    type_dropdown.place(x=580,y=200)

    login_btn=Button(frm,text='login',command=lambda:validatehomescreen(frm,user_entry,pass_entry,type_dropdown),width=10,font=('',12,''),bg='powderblue',bd=5)
    login_btn.place(x=400,y=300)

    reset_btn=Button(frm,text='reset',command=lambda:resethome(user_entry,pass_entry),width=10,font=('',12,''),bg='powderblue',bd=5)
    reset_btn.place(x=550,y=300)

    newuser_btn=Button(frm,text='NewUser',command=lambda:newuserscreen(frm),width=10,font=('',12,''),bg='powderblue',bd=5)
    newuser_btn.place(x=700,y=300)

    fp_btn=Button(frm,text='Forgotpassword',command=lambda:forgotpassscreen(frm),width=25,font=('',12,''),bg='powderblue',bd=5)
    fp_btn.place(x=500,y=400)

def forgotpassscreen(prvfrm):
    prvfrm.destroy()
    frm=Frame(win,bg='yellow')
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    user_lbl=Label(frm,text='Username:',font=('',20,''),fg='blue',bg='yellow')
    user_lbl.place(x=400,y=100)
    
    email_lbl=Label(frm,text='Email:',font=('',20,''),fg='blue',bg='yellow')
    email_lbl.place(x=400,y=150)
    
    mob_lbl=Label(frm,text='Mobile:',font=('',20,''),fg='blue',bg='yellow')
    mob_lbl.place(x=400,y=200)
    
    user_entry=Entry(frm,bg='powderblue',bd=5,width=15,font=('',15,''))
    user_entry.place(x=580,y=100)
    user_entry.focus()
    
    email_entry=Entry(frm,bg='powderblue',bd=5,width=15,font=('',15,''))
    email_entry.place(x=580,y=150)

    mob_entry=Entry(frm,bg='powderblue',bd=5,width=15,font=('',15,''))
    mob_entry.place(x=580,y=200)
    
    rcvr_btn=Button(frm,text='Recover',command=lambda:recoverpass(frm,user_entry,email_entry,mob_entry),width=10,font=('',12,''),bg='powderblue',bd=5)
    rcvr_btn.place(x=500,y=300)
    
    reset_btn=Button(frm,text='reset',command=lambda:resetforgotpass(user_entry,email_entry,mob_entry),width=10,font=('',12,''),bg='powderblue',bd=5)
    reset_btn.place(x=650,y=300)
    
    back_btn=Button(frm,text='back',command=lambda:homescreen(frm),width=10,font=('',12,''),bg='powderblue',bd=5)
    back_btn.place(x=50,y=20)
    
def newuserscreen(prvfrm):
    prvfrm.destroy()
    frm=Frame(win,bg='yellow')
    frm.place(x=0,y=100,relwidth=1,relheight=1)
    user_lbl=Label(frm,text='Username:',font=('',20,''),fg='blue',bg='yellow')
    user_lbl.place(x=400,y=100)

    email_lbl=Label(frm,text='Email:',font=('',20,''),fg='blue',bg='yellow')
    email_lbl.place(x=400,y=150)
    
    mob_lbl=Label(frm,text='Mobile:',font=('',20,''),fg='blue',bg='yellow')
    mob_lbl.place(x=400,y=200)
    
    type_lbl=Label(frm,text='Account type:',font=('',20,''),fg='blue',bg='yellow')
    type_lbl.place(x=400,y=250)
    
    bal_lbl=Label(frm,text='Initial bal:',font=('',20,''),fg='blue',bg='yellow')
    bal_lbl.place(x=400,y=300)
   
   
    pass_lbl=Label(frm,text='Password:',font=('',20,''),fg='blue',bg='yellow')
    pass_lbl.place(x=400,y=350)
   
    user_entry=Entry(frm,bg='powderblue',bd=5,width=15,font=('',15,''))
    user_entry.place(x=580,y=100)
    user_entry.focus()
   
    email_entry=Entry(frm,bg='powderblue',bd=5,width=15,font=('',15,''))
    email_entry.place(x=580,y=150)
   
    mob_entry=Entry(frm,bg='powderblue',bd=5,width=15,font=('',15,''))
    mob_entry.place(x=580,y=200)
    
    type_dropdown=ttk.Combobox(frm,values=['Saving','Current'],font=('',11,''))
    type_dropdown.current(0)
    type_dropdown.place(x=580,y=253)
    
    bal_entry=Entry(frm,bg='powderblue',bd=5,width=15,font=('',15,''))
    bal_entry.place(x=580,y=300)
   
    pass_entry=Entry(frm,bg='powderblue',bd=5,width=15,font=('',15,''))
    pass_entry.place(x=580,y=350)

    open_btn=Button(frm,text='Open Account',command=lambda:validatenewuser(frm,user_entry,pass_entry,email_entry,mob_entry,type_dropdown,bal_entry),width=15,font=('',12,''),bg='powderblue',bd=5)
    open_btn.place(x=480,y=450)
    
    reset_btn=Button(frm,text='reset',command=lambda:resetnewuser(user_entry,pass_entry,mob_entry,email_entry,type_dropdown,bal_entry),width=15,font=('',12,''),bg='powderblue',bd=5)
    reset_btn.place(x=670,y=450)
    
    back_btn=Button(frm,text='back',command=lambda:homescreen(),width=10,font=('',12,''),bg='powderblue',bd=5)
    back_btn.place(x=50,y=20)
    
def resethome(eu,ep):
    eu.delete(0,END)
    ep.delete(0,END)
    eu.focus()
    
def resetnewuser(eu,ep,em,ee,et,eb):
    eu.delete(0,END)
    ep.delete(0,END)
    em.delete(0,END)
    ee.delete(0,END)
    et.current(0)
    eb.delete(0,END)
    eu.focus()
    
def resetforgotpass(eu,em,ee):
    eu.delete(0,END)
    em.delete(0,END)
    ee.delete(0,END)
    eu.focus()
def validatehomescreen(frm,eu,ep,et):
    u=eu.get()
    p=ep.get()
    t=et.get()
    if(len(u)==0 or len(p)==0):
        messagebox.showwarning('Validation Failed',"Username/Password can't be empty")
        return
    else:
        con=db.getCon()
        cur=con.cursor()
        cur.execute("select * from useraccount where username=%s and password=%s",(u,p))
        tup=cur.fetchone()
        if(tup!=None):
            if(t=='User'):
                messagebox.showinfo('Login Success',f"Welcome,{u}")
                welcomeuser(frm,u)

            else:
                messagebox.showerror('Login Failed',"Invalid User type")
        else:
            messagebox.showerror('Login Failed',"Invalid Username/Password")


def validatenewuser(frm,eu,ep,ee,em,et,eb):
    u=eu.get()
    p=ep.get()
    e=ee.get()
    m=em.get()
    b=eb.get()
    t=et.get()
    if(len(u)==0 or len(p)==0 or len(e)==0 or len(m)==0 or len(b)==0):
        messagebox.showwarning('Validation Failed',"Fields can't be empty")
        return

    else:
        con=db.getCon()
        cur=con.cursor()
        cur.execute("select max(acno) from useraccount")
        acno=cur.fetchone()[0]
        acno=acno+1
        try:
            cur.execute("insert into useraccount values(%s,%s,%s,%s,%s,%s,%s)",(u,p,e,m,acno,b,t))
            con.commit()
            messagebox.showinfo('Success',f"Account opened with acno:{acno}")
            homescreen(frm)
        except Exception as e:
            messagebox.showwarning('User name exists',str(e))
        con.close()

def recoverpass(frm,eu,ee,em):
    u=eu.get()
    e=ee.get()
    m=em.get()
    con=db.getCon()
    cur=con.cursor()
    cur.execute("select password from useraccount where username=%s and email=%s and mob=%s",(u,e,m))
    tup=cur.fetchone()
    if(tup!=None):
        p=tup[0]
        messagebox.showinfo('Password Recovery',f"Your Password is:{p}")
        homescreen(frm)

    else:
        messagebox.showinfo('Password Recovery',"Invalid details")

def welcomeuser(prvfrm,u):
    prvfrm.destroy()
    frm=Frame(win,bg='yellow')
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    if(os.path.exists(f'{u}.jpg')):
        img=ImageTk.PhotoImage(Image.open(f'{u}.jpg').resize((150,150)))
    else:
        img=ImageTk.PhotoImage(Image.open('default.jpg').resize((150,150)))

    lbl_img=Label(frm,image=img)
    lbl_img.image=img
    lbl_img.place(x=10,y=30)

    updatepic_btn=Button(frm,text='change profile picture',command=lambda:changepic(frm,u))
    updatepic_btn.place(x=170,y=30)


    withdraw_btn=Button(frm,text='withdraw',command=lambda:withdraw(u),width=15,font=(",12,"),bg='powder blue',bd=5)
    withdraw_btn.place(x=600,y=50)

    deposit_btn=Button(frm,text='deposit',command=lambda:deposit(u),width=15,font=(",12,"),bg='powder blue',bd=5)
    deposit_btn.place(x=600,y=120)

    bal_btn=Button(frm,text='check bal',command=lambda:checkbal(u),width=15,font=(",12,"),bg='powder blue',bd=5)
    bal_btn.place(x=600,y=190)

    txn_btn=Button(frm,text='txn history',command=lambda:txnhistory(u),width=15,font=(",12,"),bg='powder blue',bd=5)
    txn_btn.place(x=600,y=260)

    updatepass_btn=Button(frm,text='update pass',command=lambda:updatepass(u),width=15,font=(",12,"),bg='powder blue',bd=5)
    updatepass_btn.place(x=600,y=330)

    logout_btn=Button(frm,text='logout',command=lambda:logout(frm),width=15,font=(",12,"),bg='powder blue',bd=5)
    logout_btn.place(relx=.8,y=10)

    wel_label=Label(frm,text=f'Welcome,{u}',bg='yellow',font=(",12,"))
    wel_label.place(x=10,y=0)

def logout(frm):
    messagebox.showinfo('Logout',"you will be logged out!")
    homescreen(frm)

def checkbal(u):
    con=db.getCon()
    cur=con.cursor()
    cur.execute("select bal from useraccount where username=%s",(u,))
    tup=cur.fetchone()
    messagebox.showinfo('Check bal',f"Your Available Balance:{tup[0]}")
    con.close()

def withdraw(u):
    amt=simpledialog.askinteger('Withdraw','Enter Amount:')
    con=db.getCon()
    cur=con.cursor()
    cur.execute("select bal,acno from useraccount where username=%s",(u,))
    tup=cur.fetchone()
    avlbal=tup[0]
    acno=tup[1]
    dt=datetime.now()
    if(avlbal>=amt):
        cur.execute("update useraccount set bal=bal-%s where username=%s",(amt,u))
        con.commit()
        messagebox.showinfo('Withdraw',"Txn Done...")
        cur.execute("insert into txnhistory values(%s,%s,%s,%s,%s)",(acno,dt,amt,'Debit',avlbal-amt))
        con.commit()
        con.close()

    else:
        messagebox.showinfo('Withdraw',"Insufficient Bal")

def deposit(u):
    amt=simpledialog.askinteger('Deposit','Enter Amount:')
    con=db.getCon()
    cur=con.cursor()
    cur.execute("select bal,acno from useraccount where username=%s",(u,))
    tup=cur.fetchone()
    avlbal=tup[0]
    acno=tup[1]
    dt=datetime.now()
    if(amt>=0):
        cur.execute("update useraccount set bal=bal+%s where username=%s",(amt,u))
        con.commit()
        messagebox.showinfo('Deposit',"Txn Done...")
        cur.execute("insert into txnhistory values(%s,%s,%s,%s,%s)",(acno,dt,amt,'Credit',avlbal+amt))
        con.commit()
        con.close()

    else:
        messagebox.showinfo('Deposit',"Invalid amount")

def updatepass(u):
    np=simpledialog.askstring('Update Password','Enter New Password:')
    cp=simpledialog.askstring('Update Password','Enter Confirm Password:')
    if(np==cp ):
        con=db.getCon()
        cur=con.cursor()
        cur.execute("update useraccount set password=%s where username=%s",(np,u))
        con.commit()
        con.close()
        messagebox.showinfo('Update Password',"Password Changed Successfully")
    else:
        messagebox.showwarning('Update Password',"New and Confirm Password do not match")

def txnhistory(u):
    con=db.getCon()
    cur=con.cursor()
    cur.execute("select acno from useraccount where username=%s",(u,))
    acno=cur.fetchone()[0]
    cur.execute("select txndate,amt,txntype,updatebal from txnhistory where acno=%s",(acno,))
    history=cur.fetchall()
    msg="Date\t   Time\t\tAmount\tType\tUpdatebal\n"
    for row in history:
        msg=msg+str(row[0])+'\t '+str(row[1])+'\t'+(row[2])+'\t'+str(row[3])+'\n'
    messagebox.showinfo("Txn History",msg)

def changepic(frm,u):
    picpath=filedialog.askopenfilename()
    file1=open(picpath,'rb')
    data=file1.read()
    file2=open(f'{u}.jpg','wb')
    file2.write(data)
    file2.close()
    file1.close()
    img=ImageTk.PhotoImage(Image.open(f'{u}.jpg').resize((150,150)))
    lbl_img=Label(frm,image=img)
    lbl_img.image=img
    lbl_img.place(x=10,y=30)




homescreen()
win.mainloop()















































































































































    
                
    







    
        






        


            
        
        
                


    
    



    
