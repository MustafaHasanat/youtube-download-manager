from tkinter import Frame, Label, Button
import webbrowser


class AppInfoPage:
    
    def __init__(self, master, tools):
        self.page = Frame(master, bg=tools.palette["green"])
        self.page.pack(side="top", fill="both", expand=True)
        
        self.version = Label(self.page, text="--- Version ---\n1.0", justify="center", font=("Berlin Sans FB", 25), 
                              bg=tools.palette["green"], fg=tools.palette["light-green"])
        self.version.pack(side="top", pady=10)
        
        self.language = Label(self.page, text="--- Language ---\nPython 3", justify="center", font=("Berlin Sans FB", 25), 
                              bg=tools.palette["green"], fg=tools.palette["light-green"])
        self.language.pack(side="top", pady=10)
        
        self.modules = Label(self.page, text="--- Modules ---\ntkinter - pafy - PIL - webbrowser", justify="center", font=("Berlin Sans FB", 25), 
                              bg=tools.palette["green"], fg=tools.palette["light-green"])
        self.modules.pack(side="top", pady=10)
        
        self.github_word = Label(self.page, text="--- Project on Github ---", justify="center", font=("Berlin Sans FB", 25), 
                              bg=tools.palette["green"], fg=tools.palette["light-green"])
        self.github_word.pack(side="top", pady=10)
        
        github_project = "https://mustfa1999.github.io/youtube-download-manager"
        self.github = Button(self.page, text="Go to Github", font=("Berlin Sans FB", 25), bg=tools.palette["purple"], 
                             fg=tools.palette["light-green"], command=lambda: webbrowser.open_new(github_project),
                             cursor="hand2")
        self.github.pack(side="top", pady=10)