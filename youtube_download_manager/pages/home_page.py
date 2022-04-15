from textwrap import wrap
from tkinter import Tk, Frame, Label, Button, Image, Text
from tkinter.ttk import Notebook
from PIL import Image, ImageTk, ImageDraw, ImageFilter
from matplotlib.pyplot import text


class HomePage:
    """
    a page that shows the home page of the app which has an intro to the app and
    a gudie for the user to use the app

    Args:
        master (tkinter frame): the placement frame that will contain the page inside the main window's notebook
        tools (Tools instance): the tools instance that will be used to access the tools methods and attributes
    """
        
    def __init__(self, master, tools):
        # create the page frame and pack it into the master frame
        self.page = Frame(master, bg=tools.palette["green"])
        self.page.pack(side="top", fill="both", expand=True)
        
        # self.app_name = Label(self.page, text="YouTube Download Manager", 
        #                       font=("Berlin Sans FB", 30, "bold"),
        #                       bg=palette["green"], fg=palette["light-green"])
        # self.app_name.pack(side="top", pady=50)
        
        # prepare texts for the intro and guide
        app_info_text = "<<<<<<< Intro >>>>>>> \nWelcome to Youtube Download Manager, a simple application that allows you to download videos from YouTube.\nYou can download videos and save them to your computer, you only need to enter the video's URL and click the download button,\nYes .. it's that simple !!"
        guide_text = "<<<<<<< Guide >>>>>>> \nGo to the downloading page then enter the URL of the video you want to download. Select the format of the file (video or audio) then click the download button.\n\nThe file will be saved in the Downloads folder."
 
        # create the app info label and pack it into the page frame 
        self.app_info = Label(self.page, text=app_info_text, wraplength=int(tools.screen_width/2), justify="center", 
                              font=("Berlin Sans FB", 20), bg=tools.palette["green"], fg=tools.palette["light-green"])
        self.app_info.pack(side="top", pady=10, padx=10)
        
        # create the guide label and pack it into the page frame
        self.guide = Label(self.page, text=guide_text, wraplength=int(tools.screen_width/2), justify="center",
                              font=("Berlin Sans FB", 20), bg=tools.palette["green"], fg=tools.palette["light-green"])
        self.guide.pack(side="top", pady=10, padx=10)