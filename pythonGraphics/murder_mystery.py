import tkinter as tk
from tkinter import *
import time
import datetime

class MurderMystery(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("A Desktop Mystery")
        self.geometry("600x600+50+50")
        self.resizable(False, False)
        self.configure(bg='blue')

        # Container to hold the pages
        self.container = tk.Frame(self, bg='blue')
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Create and store instances of the two pages
        for F in (PageOne, PageTwo, Page3):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageOne")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='blue')
        self.controller = controller

        message_text = """Uh oh there has been a file murdered on your desktop (In your case deleted).
        There are a few culprits that could have done it. Don't believe me? Check your desktop."""

        file_x = "file1"
        file_y = "file2"
        file_z = "file3"

        message_text = message_text + " " + file_x + " " + file_y + " " + file_z
        killed_file = "<killed file>"

        message_text = message_text + """\n Your job is to deduce which file is the murderer. 
        Each file has thier own statements. You must be able to discern from thier statements 
        which file killed """ + killed_file + """. All other files have been encrypted. 
        You must find the killer to get back your files. Click the button below to begin."""

        message = tk.Label(self, text=message_text, bg="blue", fg="white", font=("Courier", 12))
        message.bind('<Configure>', lambda e: message.config(wraplength=message.winfo_width()))
        message.pack(pady=10, padx=10)

        button = Button(self, text="Next", command=lambda: controller.show_frame("PageTwo"), bg="blue", fg="white")
        button.pack(ipadx=5, ipady=5, expand=True)


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='blue')
        self.controller = controller

        self.message_text = "LOL Fuck you I actually deleted everything"
        self.message = tk.Label(self, text=self.message_text, bg="blue", fg="white", font=("Courier", 12))
        self.message.pack(pady=10, padx=10) 

        self.after(5000, self.update_message)


    def update_message(self):
        # Update the message text after a certain time
        self.message.config(text="Just kidding. Click on the button below to continue")

        button = Button(self, text="Actually begin", command=lambda: self.controller.show_frame("Page3"), bg="blue", fg="white")
        button.pack(ipadx=5, ipady=5, expand=True)

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='blue')
        self.controller = controller

        message_text = """Read each testimonial and determine who did it. 
        Guess wrong a new file will be "murdered" if you catch my drift.
        Don't think you can just do process of elimination either. Make enough 
        choices and all your files will be deleted. Good luck"""

        

        message = tk.Label(self, text=message_text, bg="blue", fg="white", font=("Courier", 12))
        message.bind('<Configure>', lambda e: message.config(wraplength=message.winfo_width()))
        message.pack(pady=10, padx=10)

        self.testimonial_text = """I saw <File 1> running to the downloads when the virus started to run."""
        self.testimonial = tk.Label(self, text=message_text, bg="blue", fg="white", font=("Courier", 12))
        self.testimonial.bind('<Configure>', lambda e: self.testimonial.config(wraplength=self.testimonial.winfo_width()))
        self.testimonial.pack_forget()

        def onclick(self):
            self.testimonial.config(text=self.testimonial_text)
            self.testimonial.pack()

        button = Button(self, text="<File name 1> Testimonial", command=onclick, bg="blue", fg="white")
        button.grid(row=1, column=0, pady=10)
        button.pack(ipadx=5, ipady=5, expand=True)

        

        

if __name__ == "__main__":
    app = MurderMystery()
    app.mainloop()