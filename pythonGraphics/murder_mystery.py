import tkinter as tk
from tkinter import *
from tkinter import ttk

#Turn it into a murder mystery

class begin
    

root = tk.Tk()
root.configure(bg='blue')


message_text = """Uh oh there has been a file murdered on your desktop (In your case deleted).
There are a few culprits that could have done it. Don't believe me? Check your desktop."""

file_x = "file1"
file_y = "file2"
file_z = "file3"

message_text = message_text + " " + file_x + " " + file_y + " " + file_z
killed_file = "killed file"

message_text = message_text + """\n Your job is to deduce which file is the murderer. 
Each file has thier own statements. You must be able to discern from thier statements 
which file killed """ + killed_file + """. All other files have been encrypted. 
You must find the killer to get back your files. Click the button below to begin."""

message = tk.Label(root, text=message_text, bg="blue", fg="white", font=("Courier"))
message.bind('<Configure>', lambda e: message.config(wraplength=message.winfo_width()))
message.pack()

root.title("A Desktop Mystery")
root.geometry("600x400+50+50")
root.resizable(False, False)

exit_button = Button(root, text="Begin", command=next_page, bg="blue", fg="white")
exit_button.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()