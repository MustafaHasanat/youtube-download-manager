from tkinter import Frame, Label, Button, Image, Frame
from PIL import Image, ImageTk
import webbrowser

class AboutAuthorPage:
    
    def __init__(self, master, tools):
        self.tools = tools
        self.page = Frame(master, bg=tools.palette["green"])
        self.page.pack(side="top", fill="both", expand=True)
        
        self._Author()
        self._URLs()
    
            
    def _Author(self):
        tools = self.tools
        self.author = Frame(self.page, bg=tools.palette["green"])
        self.author.pack(side="left")
        
        self.image = Image.open(r"youtube_download_manager\assets\author.png")
        self.image = self.image.resize((int(tools.screen_width*0.2), int(tools.screen_width*0.2)))
        self.image = tools.mask_circle_transparent(self.image, 1.5)
        self.image = ImageTk.PhotoImage(self.image)
        self.author_image = Label(self.author, image=self.image, bg=tools.palette["green"])
        self.author_image.image = self.image
        self.author_image.pack(padx=50, pady=15)

        self.author_name = Label(self.author, text="Mustafa Alhasanat", justify="center", font=("Berlin Sans FB", 30),
                                 bg=tools.palette["green"], fg=tools.palette["dark-green"])
        self.author_name.pack(padx=50, pady=10)
        
        self.author_role = Label(self.author, text="Software Developer", justify="center", font=("Berlin Sans FB", 20),
                                 bg=tools.palette["green"], fg=tools.palette["dark-green"])
        self.author_role.pack(padx=50)
        
        
        
    def _URLs(self):
        tools = self.tools
        self.urls = Frame(self.page, bg=tools.palette["green"])
        self.urls.pack(side="right")
        
        self.linkedin_url = "https://www.linkedin.com/in/mustafa-alhasanat"
        self.linkedin = Button(self.urls, text="My LinkedIn Account", font=("Berlin Sans FB", 25), cursor="hand2",
                               bg=tools.palette["dark-green"], fg=tools.palette["light-green"],
                               command=lambda: webbrowser.open_new(self.linkedin_url)) 
        self.linkedin.pack(padx=50, pady=20)
        
        self.github_url = "https://github.com/Mustfa1999"
        self.github = Button(self.urls, text="My Github Account", font=("Berlin Sans FB", 25), cursor="hand2",
                               bg=tools.palette["dark-green"], fg=tools.palette["light-green"], 
                             command=lambda: webbrowser.open_new(self.github_url))
        self.github.pack(padx=50, pady=20)
        
        self.blog_url = "https://mustafahasanat.blogspot.com/"
        self.blog = Button(self.urls, text="My Blog", font=("Berlin Sans FB", 25), cursor="hand2",
                               bg=tools.palette["dark-green"], fg=tools.palette["light-green"],
                               command=lambda: webbrowser.open_new(self.blog_url)) 
        self.blog.pack(padx=50, pady=20)
        
        self.website_url = "https://mustafahasanat.weebly.com/"
        self.website = Button(self.urls, text="My Portfolio", font=("Berlin Sans FB", 25), cursor="hand2",
                               bg=tools.palette["dark-green"], fg=tools.palette["light-green"], 
                             command=lambda: webbrowser.open_new(self.website_url))
        self.website.pack(padx=50, pady=20)
        
        
        
        
        
        
        
        
        
        
        
        