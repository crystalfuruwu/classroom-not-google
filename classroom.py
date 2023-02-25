# Made by Christian Castellanos in SpenceHacks Hackathon
# Code for a better world!

from tkinter import *
from tkinter import ttk
import sv_ttk
class User:
    def __init__(self, username, name):
        self.__username = username
        self.__name = name
root = Tk()
root.geometry("480x360")
root.title('Classroom')
import cf_classroom_extension
def close_main_window():
   root.destroy()
# WINDOWS
def signup_window():
    cf_classroom_extension.signup()

#widgets
welcome_text = Label(root, text = "Welcome to Classroom!")
username_label = Label(root, text = "Username")
password_label = Label(root, text = "Password")
username = Text(root, height = 1, width = 25)
password = Text(root, height = 1, width = 25)
button = ttk.Button(root, text="Login")
signupbutton = ttk.Button(root, text= "Sign Up", command= signup_window)
exitButton = ttk.Button(root, text="Exit", command = close_main_window)
# PACKING WIDGETS
welcome_text.pack(padx=6,pady=6)
username_label.pack()
username.pack(padx=2,pady=2)
password_label.pack()
password.pack(padx=4,pady=4)
button.pack(padx=2,pady=2)
signupbutton.pack(padx=2,pady=10)
exitButton.pack(side=BOTTOM)
sv_ttk.set_theme("light")
root.resizable(width=False, height=False)
root.mainloop()