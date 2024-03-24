import tkinter as tk
from tkinter import *
from tkinter import ttk

#Turn it into a murder mystery

def callback():
    print("Button clicked")

root = tk.Tk()
root.configure(bg='blue')


message_text = """Uh oh there has been a file murdered on your desktop (In your case deleted).
There are a few culprits that could have done it. Don't beleive me check your desktop."""

file_x = "file1"
file_y = "file2"
file_z = "file3"

message_text = message_text + " " + file_x + " " + file_y + " " + file_z

message_text = message_text + """\n Your job is to deduce which file is the murderer. 
Each file has thier own statements. You must be able to discern """

message = tk.Label(root, text=message_text, bg="blue", fg="white", font=("Courier"))
message.bind('<Configure>', lambda e: message.config(wraplength=message.winfo_width()))
message.pack()

root.title("A Desktop Mystery")
root.geometry("600x400+50+50")
root.resizable(False, False)

exit_button = Button(root, text="Demo button", command=lambda: root.quit(), bg="blue", fg="white")
exit_button.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()