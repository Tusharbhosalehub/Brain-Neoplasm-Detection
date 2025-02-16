#BRAIN STROKE PROJECT
from tkinter import *
import tkinter as tk
from tkvideo import tkvideo


root = tk.Tk()
root.configure(background="white")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Brain Stroke ")

video_label = tk.Label(root)
video_label.pack()

player = tkvideo("Brain Stock Video No Copyright Videos.mp4", video_label, loop=1, size=(w, h))
player.play()

# Create a label to overlay on top of the video
# overlay_label =Label(root, text="BRAIN STROKE DETECTION USING EFFECTIVE MACHINE LEARNING TECHNIQUE", font=("Bold", 28), bg="black",fg="white")
# #overlay_label.place(x=180, y=0)

frame=Frame(root,bg="black")
frame.place(x=0,y=0,height=60,width=1700)

overlay_label =Label(root, text="BRAIN NEOPLASM DETECTION USING  MACHINE LEARNING ", font=("Bold", 28), bg="black",fg="white")
#overlay_label.place(x=180, y=0)

# Function to update the label's position for the marquee effect
def update_marquee():
    current_x = overlay_label.winfo_x()
    label_width = overlay_label.winfo_width()
    
    if current_x < -label_width:
        new_x = w  # Reset the label to the right when it goes out of the screen
    else:
        new_x = current_x - 1  # Move the label one pixel to the left
        
    overlay_label.place(x=new_x, y=8)
    overlay_label.after(10, update_marquee)  # Call this function after 10 milliseconds

# Start the marquee effect
update_marquee()



def reg():
    from subprocess import call
    call(["python","REGISTRATION PAGE.py"])
    
def log():
    from subprocess import call
    call(["python","user login.py"])    

# Create buttons
registration_button = tk.Button(root, text="Registration",command=reg, font=("bold", 14), bg="white", fg="black", padx=20, pady=10)
registration_button.place(x=200, y=300, height=35, width=120)

login_button = tk.Button(root, text="Login",command=log, font=("bold", 14), bg="white", fg="black", padx=20, pady=10)
login_button.place(x=200, y=400, height=35, width=120)

exit_button = tk.Button(root, text="Exit", font=("bold", 14), bg="white", fg="black", padx=20, pady=10,command=root.quit)
exit_button.place(x=200, y=500,height=35, width=120)

# help_button = tk.Button(root,text="Help", font=("bold", 14), bg="orange", fg="black", padx=20, pady=10)
# help_button.place(x=640, y=470, height=35, width=120)

# frame=Frame(root,bg="black")
# frame.place(x=0,y=50,height=30,width=1700)

# home_button = tk.Button(root, text="Home", font=("bold", 14), bg="white", fg="black", padx=20, pady=10)
# home_button.place(x=950, y=50, height=30, width=70)

# home_button = tk.Button(root, text="About", font=("bold", 14), bg="white", fg="black", padx=20, pady=10)
# home_button.place(x=1050, y=50, height=30, width=70)


root.mainloop()
