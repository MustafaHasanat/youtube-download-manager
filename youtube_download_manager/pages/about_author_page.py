from tkinter import Frame, Label, Button, Image, Frame, messagebox
from PIL import Image, ImageTk
import webbrowser
import threading

class AboutAuthorPage:
    """
    the page is splitted into two parts, the left one for the author info and the right one for the urls

    Args:
        master (tkinter frame): the placement frame that will contain the page inside the main window's notebook
        tools (Tools instance): the tools instance that will be used to access the tools methods and attributes
    """
    
    def __init__(self, master, tools):
        self.tools = tools      # define the tools for this page
        # create the page frame and pack it into the master frame 
        self.page = Frame(master, bg=tools.palette["green"])        
        self.page.pack(side="top", fill="both", expand=True)
        
        # call the private methods to create the page's frames 
        self._Author()
        self._URLs()
        
        # indicator that there is a web page is openning now or not
        self.requesting = False
    
            
    def _Author(self):
        """
        creates a frame, which is the left part of the page that contains the author's info
        """
        
        tools = self.tools
        # create the left side frame and pack it into the page frame 
        self.author = Frame(self.page, bg=tools.palette["green"])
        self.author.pack(side="left")
        
        # create the author's image and pack it into the left side frame
        self.image = Image.open(r"youtube_download_manager\assets\author.png")
        self.image = self.image.resize((int(tools.screen_width*0.2), int(tools.screen_width*0.2)))
        self.image = tools.mask_circle_transparent(self.image, 1.5)
        self.image = ImageTk.PhotoImage(self.image)
        self.author_image = Label(self.author, image=self.image, bg=tools.palette["green"])
        self.author_image.image = self.image
        self.author_image.pack(padx=50, pady=15)

        # create the author's name and pack it into the left side frame
        self.author_name = Label(self.author, text="Mustafa Alhasanat", justify="center", font=("Berlin Sans FB", 30),
                                 bg=tools.palette["green"], fg=tools.palette["dark-green"])
        self.author_name.pack(padx=50, pady=10)
        
        self.author_role = Label(self.author, text="Software Developer", justify="center", font=("Berlin Sans FB", 20),
                                 bg=tools.palette["green"], fg=tools.palette["dark-green"])
        self.author_role.pack(padx=50)
        
        
        
    def _URLs(self):
        """
        creates a frame, which is the right part of the page that contains the author's urls
        it will contain buttons for social each url for the author
        """
        
        tools = self.tools
        # create the right side frame and pack it into the page frame
        self.urls = Frame(self.page, bg=tools.palette["green"])
        self.urls.pack(side="right")
        
        
        def url_button_handler(url):
            """
            opens the url in the default browser

            Args:
                url (string): url to be opened
            """
            
            def thread(url):
                """
                a function that opens the url in the default browser

                Args:
                    url (string): url to be opened
                """
                
                self.requesting = True
                webbrowser.open_new(url)
                self.requesting = False
            
            
            # if there is a web page is openning now, raise an error message box
            if self.requesting:
                messagebox.showerror("Page is openning !!!", "There is a page opening currently, please wait until it is finished.")

            # open the web page in a new thread only if there is no web page is openning now
            threading.Thread(target=thread, args=(url,)).start()
            
                
                                 
        
        # create the linkedin url button and pack it into the right side frame
        self.linkedin_url = "https://www.linkedin.com/in/mustafa-alhasanat"
        self.linkedin = Button(self.urls, text="My LinkedIn Account", font=("Berlin Sans FB", 25), cursor="hand2",
                               bg=tools.palette["dark-green"], fg=tools.palette["light-green"],
                               command=lambda: url_button_handler(self.linkedin_url))
        self.linkedin.pack(padx=50, pady=20)
        
        # create the github url button and pack it into the right side frame
        self.github_url = "https://github.com/Mustfa1999"
        self.github = Button(self.urls, text="My Github Account", font=("Berlin Sans FB", 25), cursor="hand2",
                               bg=tools.palette["dark-green"], fg=tools.palette["light-green"], 
                             command=lambda: url_button_handler(self.github_url))
        self.github.pack(padx=50, pady=20)
        
        # create the blog url button and pack it into the right side frame
        self.blog_url = "https://mustafahasanat.blogspot.com/"
        self.blog = Button(self.urls, text="My Blog", font=("Berlin Sans FB", 25), cursor="hand2",
                               bg=tools.palette["dark-green"], fg=tools.palette["light-green"],
                               command=lambda: url_button_handler(self.blog_url)) 
        self.blog.pack(padx=50, pady=20)
        
        # create the website url button and pack it into the right side frame
        self.website_url = "https://mustafahasanat.weebly.com/"
        self.website = Button(self.urls, text="My Portfolio", font=("Berlin Sans FB", 25), cursor="hand2",
                               bg=tools.palette["dark-green"], fg=tools.palette["light-green"], 
                             command=lambda: url_button_handler(self.website_url))
        self.website.pack(padx=50, pady=20)
        
        
        
        
        
        
        
        
        
        
        
        