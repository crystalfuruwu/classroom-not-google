from tkinter import *
from tkinter import ttk
import sv_ttk
import json
def add_user(username, password):
    with open("/home/crystalfur/Projects/classroom/classroom_data.json", "w") as f:
        data = json.load()
    data_to_be_written = {"username":username,
    "password": password
    }
    file_data["accounts"].append(data_to_be_written)
    file.seek(0)
    json.dump(file_data, file, indent = 4)
    root.destroy()
def signup():
    print("Crystal Fur Classroom Extension: Signing up?")
    root = Tk()
    root.title('Classroom: Sign Up')
    root.geometry("480x360")
    def add_data_and_close():
        add_username = input_username.get("1.0",'end-1c')
        add_password = input_password.get("1.0",'end-1c')
        add_user(add_username, add_password)
    label_new_username = Label(root, text="New username")
    label_new_password = Label(root, text="New password")
    input_username = Text(root, height = 1, width = 25)
    input_password = Text(root, height = 1, width = 25)
    submit_and_close_button = ttk.Button(root, text="Create new account!", command=add_data_and_close)
    # PACKING !!!!
    label_new_username.pack()
    input_username.pack()
    label_new_password.pack()
    input_password.pack()
    submit_and_close_button.pack()
    sv_ttk.set_theme("light")
    root.resizable(width=False, height=False)
    root.mainloop
print("Crystal Fur Classroom Extension: This file was loaded as a module?")