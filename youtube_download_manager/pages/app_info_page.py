from tkinter import Frame, Label, Button, messagebox
import webbrowser
import threading


class AppInfoPage:
    """
    a page that shows the app info and has a button to open the github page of this project

    Args:
        master (tkinter frame): the placement frame that will contain the page inside the main window's notebook
        tools (Tools instance): the tools instance that will be used to access the tools methods and attributes
    """
    
    def __init__(self, master, tools):
        # indicator that there is a web page is openning now or not
        self.requesting = False
        
        # create the page frame and pack it into the master frame
        self.page = Frame(master, bg=tools.palette["green"])
        self.page.pack(side="top", fill="both", expand=True)
        
        # create the app version label and pack it into the page frame
        self.version = Label(self.page, text="--- Version ---\n1.0", justify="center", font=("Berlin Sans FB", 25), 
                              bg=tools.palette["green"], fg=tools.palette["light-green"])
        self.version.pack(side="top", pady=10)
        
        # create the programming language label and pack it into the page frame
        self.language = Label(self.page, text="--- Language ---\nPython 3", justify="center", font=("Berlin Sans FB", 25), 
                              bg=tools.palette["green"], fg=tools.palette["light-green"])
        self.language.pack(side="top", pady=10)
        
        # create the programming modules label and pack it into the page frame
        self.modules = Label(self.page, text="--- Modules ---\ntkinter - pafy - PIL - webbrowser - urllib - io", 
                             justify="center", font=("Berlin Sans FB", 25), bg=tools.palette["green"], 
                             fg=tools.palette["light-green"])
        self.modules.pack(side="top", pady=10)
        
        # create the github label and pack it into the page frame
        self.github_word = Label(self.page, text="--- Project on Github ---", justify="center", font=("Berlin Sans FB", 25), 
                              bg=tools.palette["green"], fg=tools.palette["light-green"])
        self.github_word.pack(side="top", pady=10)
        
        
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
            
            
        # create the github button and pack it into the page frame
        github_project = "https://mustfa1999.github.io/youtube-download-manager"
        self.github = Button(self.page, text="Go to Github", font=("Berlin Sans FB", 25), bg=tools.palette["purple"], 
                             fg=tools.palette["light-green"], command=lambda: url_button_handler(github_project),
                             cursor="hand2")
        self.github.pack(side="top", pady=10)