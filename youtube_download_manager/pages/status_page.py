# from tkinter import Tk, Frame, Label, Button, Image
# from tkinter.ttk import Notebook
# from PIL import Image, ImageTk, ImageDraw, ImageFilter


# class StatusPage:
    
#     def __init__(self, master, palette):
#         self.page = Frame(master, bg=palette["green"])
#         self.page.pack(side="top", fill="both", expand=True)
        
from tkinter import Tk, messagebox        


walt = Tk()  

download_approval = messagebox.askokcancel("Download Wizard", "hello")
print(download_approval)

walt.mainloop()
  