from tkinter import*
import tkinter as tk 
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import sqlite3
root= Tk()  

root.geometry('500x500')  
root.title("forget password")  
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

image2= Image.open("forgot3.jpeg")
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image

background_label.place(x=0,y=0)

email= tk.StringVar()
password = tk.StringVar()
confirmPassword = tk.StringVar()


def change_password():
    
    
    Email=email.get()
    new_password_entry = password.get()
    confirm_password_entry = confirmPassword.get()
    
    with sqlite3.connect('brain_stroke.db') as db:
        c = db.cursor()

    
    find_user = ('SELECT * FROM registration WHERE Email=?')
    c.execute(find_user, [(str(email.get()))])
    
    
    #find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
    #c.execute(find_entry, [(email.get()), (password.get())])
    
    result = c.fetchall()
    if result:
        if new_password_entry == confirm_password_entry:
            db = sqlite3.connect("brain_stroke.db")
            curs = db.cursor()
    
            curs.execute("update registration set password=? WHERE Email=? ",(str(new_password_entry),email.get()))
            #curs.execute(insert, [new_password_entry ])
            db.commit()
            db.close()
            ms.showinfo('Congrats', 'Password changed successfully')
    
    else:
            ms.showerror('Error!', "Passwords didn't match")







frame=Frame(root,bg="#4682B4")
frame.place(x=25,y=150,height=350,width=400)

labl_1 =tk.Label(root, text="forgot password",width=13,font=("bold", 40),bg="#4169E1")  
labl_1.place(x=25,y=75) 

labl_1 =tk.Label(root, text="Email",width=10,font=("bold", 13),bg="#4682B4")  
labl_1.place(x=25,y=180)  
  
entry_1 =tk.Entry(root,textvariable=email)  
entry_1.place(x=180,y=180,height=20,width=150)  

labl_2=tk.Label(root, text="New Password",width=12,font=("bold", 13),bg="#4682B4")  
labl_2.place(x=25,y=230)  

entry_2 =tk.Entry(root,textvariable=password)  
entry_2.place(x=180,y=230,height=20,width=150)


labl_2=tk.Label(root, text="Confirm Password",width=15,font=("bold", 13),bg="#4682B4")  
labl_2.place(x=25,y=280)  

entry_2 =tk.Entry(root,textvariable=confirmPassword)  
entry_2.place(x=180,y=280,height=20,width=150)

forget_button = tk.Button(root, text="Forgot Password", font=("bold", 14), bg="red", fg="black", padx=20, pady=10,command=change_password)
forget_button.place(x=180, y=350,height=40, width=160)









root.mainloop()