from tkinter import Frame, Label, Button, Image, Entry, StringVar
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from pafy import new

class DownloadPage:
    
    def __init__(self, master, tools):
        self.page = Frame(master, bg=tools.palette["green"])
        self.page.pack(side="top", fill="both", expand=True)
        self.tools = tools
        
        self.url = StringVar()
        # self.url.set("https://www.youtube.com/watch?v=hS5CfP8n_js")
                
        self._UpperFrame()
        self._LowerFrame()
        
    
    def _UpperFrame(self):
        palette, width, height = self.tools.palette, self.tools.screen_width, self.tools.screen_height

        self.upper_frame = Frame(self.page, bg=palette["green"])
        self.upper_frame.grid(row=0, column=0)
        self.upper_frame.grid_rowconfigure(0, weight=1)
        
        self.url_label = Label(self.upper_frame, text="URL: ", bg=palette["green"], fg=palette["light-green"],
                               font=("Berlin Sans FB", 20))
        self.url_label.grid(row=0, column=0, sticky="w", padx=15, pady=20)
        self.url_label.grid_columnconfigure(0, weight=1)
        
        self.url_entry = Entry(self.upper_frame, bg=palette["dark-green"], fg=palette["light-green"], 
                               font=("Berlin Sans FB", 20), width=int(width*0.025), textvariable=self.url)
        self.url_entry.grid(row=0, column=1, sticky="e", padx=15,  pady=20)
        self.url_entry.grid_columnconfigure(1, weight=1)
        
        self.request_button = Button(self.upper_frame, text="Request", bg=palette["dark-green"], command=lambda: self._HandleRequest(),
                                     fg=palette["light-green"], font=("Berlin Sans FB", 20), width=int(width*0.005))
        self.request_button.grid(row=0, column=2, sticky="e", padx=15,  pady=20)
        self.request_button.grid_columnconfigure(2, weight=1)
        
        
    def _LowerFrame(self):
        palette, width, height = self.tools.palette, self.tools.screen_width, self.tools.screen_height
        
        self.lower_frame = Frame(self.page, bg=palette["green"], width=int(width))
        self.lower_frame.grid(row=1, column=0)
        self.lower_frame.grid_rowconfigure(1, weight=1)
        
        
        
        self.splash_img = Image.open(r"youtube_download_manager\assets\icon.png")
        self.splash_img = self.splash_img.resize((int(width*0.23), int(width*0.23)))
        self.splash_img = ImageTk.PhotoImage(self.splash_img)
        self.thumbnail = Label(self.lower_frame, image=self.splash_img, bg=palette["purple"])
        self.thumbnail.image = self.splash_img
        self.thumbnail.grid(row=0, column=0, columnspan=3, rowspan=3)
        
        
        self.vid_title = Label(self.lower_frame, text="---Title---", wraplength=int(width*0.15),bg=palette["green"], 
                               width=int(width*0.015), font=("Berlin Sans FB", 15, "bold"), justify="left")
        self.vid_title.grid(row=0, column=3, columnspan=3, rowspan=1, sticky="w")
        
        self.vid_author = Label(self.lower_frame, text="---Author---", wraplength=int(width*0.15),bg=palette["green"], 
                               width=int(width*0.015), font=("Berlin Sans FB", 15, "bold"), justify="left")
        self.vid_author.grid(row=1, column=3, columnspan=3, rowspan=1, sticky="w")
        
        self.vid_duration = Label(self.lower_frame, text="---Duration---", wraplength=int(width*0.15),bg=palette["green"], 
                               width=int(width*0.015), font=("Berlin Sans FB", 15, "bold"), justify="left")
        self.vid_duration.grid(row=2, column=3, columnspan=3, rowspan=1, sticky="w")
        
        
        
        self.vid_views_word = Label(self.lower_frame, text="Views", bg=palette["green"], font=("Berlin Sans FB", 15, "bold"))
        self.vid_views_word.grid(row=3, column=0, columnspan=1, rowspan=1)
        
        self.vid_likes_word = Label(self.lower_frame, text="Likes", bg=palette["green"], font=("Berlin Sans FB", 15, "bold"))
        self.vid_likes_word.grid(row=3, column=1, columnspan=1, rowspan=1)
        
        self.vid_dislikes_word = Label(self.lower_frame, text="Dislikes", bg=palette["green"], font=("Berlin Sans FB", 15, "bold"))
        self.vid_dislikes_word.grid(row=3, column=2, columnspan=1, rowspan=1)
        
        self.vid_views = Label(self.lower_frame, text="---", bg=palette["green"], font=("Berlin Sans FB", 15))
        self.vid_views.grid(row=4, column=0, columnspan=1, rowspan=1)
        
        self.vid_likes = Label(self.lower_frame, text="---", bg=palette["green"], font=("Berlin Sans FB", 15))
        self.vid_likes.grid(row=4, column=1, columnspan=1, rowspan=1)
        
        self.vid_dislikes = Label(self.lower_frame, text="---", bg=palette["green"], font=("Berlin Sans FB", 15))
        self.vid_dislikes.grid(row=4, column=2, columnspan=1, rowspan=1)
        
    
        self.type_selection = Combobox(self.lower_frame, values=["Video", "Audio"],
                                       font=("Berlin Sans FB", 15), state= "readonly", 
                                       width=int(width*0.006), foreground="black")        
        
        if self.tools.download_prefered_type == "Video":
            self.type_selection.current(0)
        else:
            self.type_selection.current(1)
            
        self.type_selection.grid(row=1, column=6, columnspan=1, rowspan=1, padx=10)
        
        self.download_img = Image.open(r"youtube_download_manager\assets\downloads.ico")
        self.download_img = self.download_img.resize((int(width*0.05), int(width*0.05)))
        self.tools.mask_circle_transparent(self.download_img, 1.5)
        self.download_img = ImageTk.PhotoImage(self.download_img)
        self.download_button = Button(self.lower_frame, image=self.download_img, bg=palette["green"], cursor="hand2",
                                      font=("Berlin Sans FB", 15), bd=0, activebackground=palette["green"])
        self.download_button.image = self.download_img
        self.download_button.grid(row=2, column=6, columnspan=1, rowspan=1, padx=10)
        
        
    def _HandleRequest(self):
        url = self.url.get()
        
        pafy_pbj = new(url)
        
        self.thumb = pafy_pbj.thumb
        self.title = pafy_pbj.title
        self.author = pafy_pbj.author
        self.duration = pafy_pbj.duration
        self.likes = pafy_pbj.likes
        self.dislikes = pafy_pbj.dislikes
        self.viewcount = pafy_pbj.viewcount
        
        self.vid_title.config(text=f"Title:\n{self.title}")
        self.vid_author.config(text=f"Author:\n{self.author}")
        self.vid_duration.config(text=f"Duration:\n{self.duration}")
        self.vid_likes.config(text=f"{self.likes}")
        self.vid_dislikes.config(text=f"{self.dislikes}")
        self.vid_views.config(text=f"{self.viewcount}")
        
        
    def _HandleDownload(self):
        vid_type = self.type_selection.get()
        
        # pafy_pbj = new(url)
        
        # if vid_type == "Video":
        #     pafy_pbj.getbest().download()
        # elif vid_type == "Audio":
        #     pafy_pbj.getbestaudio().download()
        # else:
        #     pass
        
        pass
        