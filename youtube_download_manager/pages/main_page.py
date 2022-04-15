from tkinter import Tk, Frame, Label, Button, Image
from tkinter.ttk import Notebook, Style
from PIL import Image, ImageTk

from pages.home_page import HomePage
from pages.download_page import DownloadPage
from pages.about_author_page import AboutAuthorPage
from pages.app_info_page import AppInfoPage
from pages.settings_page import SettingsPage


class MainWindow:
    """
    luanch the main window which has the access to navigate between the pages 

    Args:
        master (Tk window): the main Tk window
        tools (Tools instance): it will be used to access its attributes and methods and pass them to all pages
    """
        
    def __init__(self, master, tools):
        # initialize the window attributes
        self.wind = master
        self.tools = tools
        self.screen_width = tools.screen_width
        self.screen_height = tools.screen_height
        self.font = ("Berlin Sans FB", 20)
        self.palette = tools.palette
        
        # set the width of the window to be 85% of the full-screen width, same for height
        new_height = int(tools.screen_height*0.85)
        new_width = int(tools.screen_width*0.85)
        # set the x-offset of the window to be 75% of the full-screen width, same for y-offset
        new_height_offset = int(tools.screen_height*0.05)
        new_width_offset = int(tools.screen_width*0.075)

        # qpply the new width, height, and offset to the window
        self.wind.geometry(f"{new_width}x{new_height}+{new_width_offset}+{new_height_offset}")
        
        # call the private methods to create the page's frames 
        self._LeftFrame()
        self._RightFrame()
        
        
    def _LeftFrame(self):
        """
        this method creates the left frame which contains the app name, buttons to navigate between 
        pages, and the author's image
        """
        
        # create the left frame
        self.left_frame = Frame(self.wind, width=int(self.screen_width*0.2), height=self.screen_height, bg=self.palette["purple"])
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.left_frame.grid_columnconfigure(0, weight=2)
        
        # create the app name label
        self.app_name = Label(self.left_frame, text="YouTube Download\nManager", font=("Berlin Sans FB", 20, "bold"), bg=self.palette["purple"], fg=self.palette["light-green"])
        self.app_name.place(relx=0.5, rely=0.1, anchor="center")
        
        # create navigation buttons and assign them to their respective methods
        self.home_button = Button(self.left_frame, text="Home", bd=0, command=None, cursor="hand2",
                                  width=int(self.screen_width*0.01), font=self.font, 
                                  bg=self.palette["light-green"], fg=self.palette["dark-green"])
        self.download_button = Button(self.left_frame, text="Download", bd=0, command=None, cursor="hand2",
                                  width=int(self.screen_width*0.01), font=self.font, 
                                  bg=self.palette["purple"], fg=self.palette["light-green"])
        self.app_info = Button(self.left_frame, text="App Info", bd=0, command=None, cursor="hand2",
                                  width=int(self.screen_width*0.01), font=self.font, 
                                  bg=self.palette["purple"], fg=self.palette["light-green"])
        self.about_author = Button(self.left_frame, text="About Author", bd=0, command=None, cursor="hand2",
                                  width=int(self.screen_width*0.01), font=self.font, 
                                  bg=self.palette["purple"], fg=self.palette["light-green"])
        self.settings = Button(self.left_frame, text="Settings", bd=0, command=None, cursor="hand2",
                                  width=int(self.screen_width*0.01), font=self.font, 
                                  bg=self.palette["purple"], fg=self.palette["light-green"])
        
        # place the buttons on the left frame
        self.home_button.place(relx=0.5, rely=0.25, anchor="center")
        self.download_button.place(relx=0.5, rely=0.33, anchor="center")
        self.app_info.place(relx=0.5, rely=0.41, anchor="center")
        self.about_author.place(relx=0.5, rely=0.49, anchor="center")
        self.settings.place(relx=0.5, rely=0.56, anchor="center")
        
        # create the author's image and cut it to the appropriate size and shape
        self.image = Image.open(r"youtube_download_manager\assets\author.png")
        self.image = self.image.resize((int(self.screen_width*0.07), int(self.screen_width*0.07)))
        self.image = self.tools.mask_circle_transparent(self.image, 1.5)
        self.author_photo = ImageTk.PhotoImage(self.image)
        author_image = Label(self.left_frame, image=self.author_photo, bg=self.palette["purple"])
        author_image.place(relx=0.5, rely=0.7, anchor="center")
              

    def _RightFrame(self):
        """
        this method creates the right frame which contains the notebook that navigates through pages
        """
        
        # create the right frame
        self.right_frame = Frame(self.wind, width=int(self.screen_width*0.8), height=self.screen_height, bg=self.palette["light-green"])
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        self.right_frame.grid_columnconfigure(1, weight=8)
        
        # create the current page label
        self.current_page_name = Label(self.right_frame, text="Home Page", font=("Berlin Sans FB", 40, "bold"), 
                                  bg=self.palette["light-green"], fg=self.palette["dark-green"])
        self.current_page_name.place(relx=0.4, rely=0.08, anchor="center")
        
        # create the notebook
        self.current_page = Notebook(self.right_frame, width=int(self.screen_width*0.6), height=int(self.screen_height*0.65))
        self.current_page.place(relx=0.4, y=int(self.screen_height*0.15), anchor="n")
        
        # create the frames for the pages
        self.home_frame = Frame(self.current_page)
        self.download_frame = Frame(self.current_page)
        self.app_info_frame = Frame(self.current_page)
        self.about_author_frame = Frame(self.current_page)
        self.settings_frame = Frame(self.current_page)
        
        # add the frames to the notebook with the appropriate labels
        self.current_page.add(self.home_frame, text="Home")
        self.current_page.add(self.download_frame, text="Download")
        self.current_page.add(self.app_info_frame, text="App Info")
        self.current_page.add(self.about_author_frame, text="About Author")
        self.current_page.add(self.settings_frame, text="Settings")
        
        # link the notebook's frames to the respective methods
        self.home_button.config(command=lambda: self._HomeButton())
        self.download_button.config(command=lambda: self._DownloadButton())
        self.app_info.config(command=lambda: self._AppInfoButton())
        self.about_author.config(command=lambda: self._AboutAuthorButton())
        self.settings.config(command=lambda: self._SettingsButton())
        
        # hide the navigation bar from the notebook
        self.style = Style()
        self.style.layout('TNotebook.Tab', [])
        # self.style.theme_create( "yummy", parent="alt", 
        #     settings={
        #         "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        #         "TNotebook.Tab": { 
        #             "configure": {"padding": [5, 1], "background": self.palette["light-green"], "foreground": self.palette["dark-green"]},
        #             "map":  {"background": [("selected", self.palette["purple"])],  "expand": [("selected", [1, 1, 1, 0])] } } } )
        
        # self.style.theme_use("yummy")
        
        
        # call the methods that create the pages
        HomePage(self.home_frame, self.tools)
        DownloadPage(self.download_frame, self.tools)
        AboutAuthorPage(self.about_author_frame, self.tools)
        AppInfoPage(self.app_info_frame, self.tools)
        SettingsPage(self.settings_frame, self.tools)
        
        
    def _HomeButton(self):
        """
        this method links the home page to the home button and changes the current page label 
        it also changes the color of the home button to indicate that it is the current page and 
        changes the color of the other buttons to indicate that they are not the current page
        """
        
        self.current_page.select(0)
        self.current_page_name.config(text="Home Page")
        self.home_button.config(bg=self.palette["light-green"], fg=self.palette["dark-green"])
        self.download_button.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.app_info.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.about_author.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.settings.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        
    
    def _DownloadButton(self):
        """
        this method links the download page to the download button and changes the current page label
        it also changes the color of the download button to indicate that it is the current page and
        changes the color of the other buttons to indicate that they are not the current page
        """
        
        self.current_page.select(1)
        self.current_page_name.config(text="Downloading Page")
        self.home_button.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.download_button.config(bg=self.palette["light-green"], fg=self.palette["dark-green"])
        self.app_info.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.about_author.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.settings.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        
        
    def _AppInfoButton(self):
        """
        this method links the app info page to the app info button and changes the current page label
        it also changes the color of the app info button to indicate that it is the current page and
        changes the color of the other buttons to indicate that they are not the current page
        """
        
        self.current_page.select(2)
        self.current_page_name.config(text="App Info")
        self.home_button.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.download_button.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.app_info.config(bg=self.palette["light-green"], fg=self.palette["dark-green"])
        self.about_author.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.settings.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        
    
    def _AboutAuthorButton(self):
        """
        this method links the about author page to the about author button and changes the current page label
        it also changes the color of the about author button to indicate that it is the current page and
        changes the color of the other buttons to indicate that they are not the current page
        """
        
        self.current_page.select(3)
        self.current_page_name.config(text="About Author")
        self.home_button.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.download_button.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.app_info.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.about_author.config(bg=self.palette["light-green"], fg=self.palette["dark-green"])
        self.settings.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        
        
    def _SettingsButton(self):
        """
        this method links the settings page to the settings button and changes the current page label
        it also changes the color of the settings button to indicate that it is the current page and
        changes the color of the other buttons to indicate that they are not the current page
        """
        
        self.current_page.select(4)
        self.current_page_name.config(text="Settings")
        self.home_button.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.download_button.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.app_info.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.about_author.config(bg=self.palette["purple"], fg=self.palette["light-green"])
        self.settings.config(bg=self.palette["light-green"], fg=self.palette["dark-green"])

