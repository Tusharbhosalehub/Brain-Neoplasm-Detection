from tkinter import*
import tkinter as tk 
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
root= tk.Tk()  

root.geometry('500x500')  
root.title("login page")  
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

def forget():
    from subprocess import call
    call(["python","forget password.py"])

email = tk.StringVar()
password = tk.StringVar()

def registration():
    from subprocess import call
    call(["python","REGISTRATION PAGE.py"])
    root.destroy()

def login():
        # Establish Connection

    with sqlite3.connect('brain_stroke.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('brain_stroke.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                        "(Fullname TEXT, address TEXT, Gender TEXT, age TEXT, Email TEXT, Phoneno TEXT, password TEXT)")
         find_entry = ('SELECT * FROM registration WHERE email = ? and password = ?')
         c.execute(find_entry, [(email.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            # ===========================================
            # root.destroy()

            # from subprocess import call
            # call(['python','GUI_Master_old.py'])
            
            # root.destroy()
            
         # ================================================
         
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')

######################################## LOGIN PAGE #############################################################

image2= Image.open("medical.jpeg")
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image

background_label.place(x=0,y=0)

img = Image.open(r'medical3.jpeg')
img = img.resize((100,100), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(root, image=logo_image,bg="#87CEFF")
logo_label.image = logo_image
logo_label.place(x=320, y=200)
# labl_0 = Label(root, text="USERLOGIN",width=10,font=("bold", 40),bg="light blue")  
# labl_0.place(x=230,y=250)  

  
labl_1 =tk.Label(root, text="Username",width=10,font=("bold", 13),bg="salmon")  
labl_1.place(x=230,y=330)  
  
entry_1 =tk.Entry(root,textvariable=email)  
entry_1.place(x=340,y=330,height=20,width=150)  

labl_2=tk.Label(root, text="Password",width=10,font=("bold", 13),bg="salmon")  
labl_2.place(x=230,y=370)  

entry_2 =tk.Entry(root,textvariable=password)  
entry_2.place(x=340,y=370,height=20,width=150)

Button(root, text='Submit',width=14,bg='green',fg='black',font=18,command=login).place(x=280,y=420)  
Button(root, text='Forget password',width=14,bg='mistyrose',fg='black',command=forget,font=18).place(x=280,y=470)
  

root.mainloop()