from tkinter import*
import tkinter as tk 
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re

root= tk.Tk()  

root.geometry('500x500')  
root.title("Registration Form")  
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

##################################### DATABASE CONNECTION #########################################################

Fullname = tk.StringVar()
address = tk.StringVar()
#username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
#password1 = tk.StringVar()



# database code
db = sqlite3.connect('brain_stroke.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
              "(Fullname TEXT, address TEXT, Email TEXT, Gender TEXT, age TEXT,Phoneno TEXT, password TEXT)")
db.commit()



def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
   fname = Fullname.get()
   addr = address.get()
   #un = username.get()
   email = Email.get()
   mobile = Phoneno.get()
   gender = var.get()
   time = age.get()
   pwd = password.get()
  # cnpwd = password1.get()

   with sqlite3.connect('brain_stroke.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    # find_user = ('SELECT * FROM registration WHERE username = ?')
    # c.execute(find_user, [(username.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
   regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
   if (re.search(regex, email)):
        a = True
   else:
        a = False
    # validation
   if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
   elif (addr == ""):
        ms.showinfo("Message", "Please Enter Address")
   elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
   elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    # elif ((time > 100) or (time == 0)):
    #     ms.showinfo("Message", "Please Enter valid age")
    # elif (c.fetchall()):
    #     ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
   elif (pwd == ""):
        ms.showinfo("Message", "Please Enter valid password")
   elif (var == False):
        ms.showinfo("Message", "Please Enter gender")
   elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    # elif (pwd != cnpwd):
    #     ms.showinfo("Message", "Password Confirm password must be same")
   else:
        conn = sqlite3.connect('brain_stroke.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO registration(Fullname, address,Email,age,Gender, Phoneno, password) VALUES(?,?,?,?,?,?,?)',
                (fname, addr,  email,time,gender, mobile, pwd))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
            # window.destroy()
            
            from subprocess import call
            call(["python", "user login.py"])
            root.destroy()

############################################## REGISTARION FORM #################################################

image2= Image.open("wallpaperflare.com_wallpaper (1).jpg")
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image

background_label.place(x=0,y=0)

  
labl_0 =tk. Label(root, text="Registration form",width=20,font=("bold", 40))  
labl_0.place(x=110,y=53)  
  
  
labl_1 =tk.Label(root, text="FullName",width=10,font=("bold", 13))  
labl_1.place(x=220,y=130)  
  
entry_1 =tk.Entry(root,textvar=Fullname)  
entry_1.place(x=350,y=130,height=20,width=150)  
  
labl_2 =tk.Label(root, text="Email",width=10,font=("bold", 13))  
labl_2.place(x=220,y=180)  
  
entry_02 =tk.Entry(root,textvar=Email)  
entry_02.place(x=350,y=180,height=20,width=150)  
  
labl_3 =tk.Label(root, text="Mobile no",width=10,font=("bold", 13))  
labl_3.place(x=220,y=230)  

entry_3 =tk.Entry(root,textvar=Phoneno)  
entry_3.place(x=350,y=230,height=20,width=150) 
  
labl_4 =tk.Label(root, text="Age",width=10,font=("bold", 13))  
labl_4.place(x=220,y=280)  
  
  
entry_4 =tk.Entry(root,textvar=age)  
entry_4.place(x=350,y=280,height=20,width=150)  

label_5 =tk.Label(root,text="Gender",width=10,font=("bold",13))
label_5.place(x=220,y=320)

label_6 =tk.Label(root,text="Address",width=10,font=("bold",13))
label_6.place(x=220,y=360)

entry_6 =tk.Entry(root,textvar=address)
entry_6.place(x=350,y=360,height=20,width=160)

labl_7=tk.Label(root, text="Password",width=10,font=("bold", 13))  
labl_7.place(x=220,y=400)  

entry_7 =tk.Entry(root,show="*",textvar=password)  
entry_7.place(x=350,y=400,height=20,width=160)
 
v=tk.StringVar(root,"1")

values={"Male":"1"
        
        }

for ( text,value)in values.items():
    tk.Radiobutton(root,text=text,variable=var,
                value = value).place(x=330,y=320 ,width=80,height=20)


#v=StringVar(root,"1")

values={"Female":"2"
    
        }

for ( text,value)in values.items():
    tk.Radiobutton(root,text=text,variable=v,
                value = value).place(x=430,y=320 ,width=80,height=20)
    
Submit_button=tk.Button(root, text='Submit',width=18,bg='green',fg='black',font=18,command=insert)
Submit_button.place(x=260,y=450)  
 
root.mainloop()  