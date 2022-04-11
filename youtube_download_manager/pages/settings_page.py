from tkinter import Frame, Label, Button, Radiobutton, filedialog, IntVar


class SettingsPage:
    
    def __init__(self, master, tools):
        self.page = Frame(master, bg=tools.palette["green"])
        self.page.pack(side="top", fill="both", expand=True)
        
        self._DownloadPath(tools)
        self._DownloadType(tools)
        
    
    def _DownloadPath(self, tools):
        self.download_path = Frame(self.page, bg=tools.palette["green"])
        self.download_path.pack(side="top", pady=30, fill="x", expand=True)
        
        self.path_word = Label(self.download_path, text="Change Default\nDownloading Path", font=("Berlin Sans FB", 30),
                                bg=tools.palette["green"], fg=tools.palette["light-green"])
        self.path_word.pack(side="left", padx=30)
        
        self.right_side = Frame(self.download_path, bg=tools.palette["green"])
        self.right_side.pack(side="right", padx=30)
        
        self.browse_button = Button(self.right_side, text="Browse", bg=tools.palette["dark-green"], cursor="hand2",
                                    fg=tools.palette["light-green"], font=("Berlin Sans FB", 20),
                                    command=lambda: self._HandleBrowse(tools))
        self.browse_button.pack(side="top", pady=10)
        
        self.path_label = Label(self.right_side, text=tools.download_prefered_path, font=("Berlin Sans FB", 15),
                                wraplength=int(tools.screen_width*0.3), bg=tools.palette["green"], 
                                    fg=tools.palette["light-green"])
        self.path_label.pack(side="top", pady=10)
        
        
    def _DownloadType(self, tools):
        self.download_type = Frame(self.page, bg=tools.palette["green"])
        self.download_type.pack(side="top", pady=30, fill="x", expand=True)
        
        self.type_word = Label(self.download_type, text="Change Prefered\nDownloading Type", font=("Berlin Sans FB", 30),
                                bg=tools.palette["green"], fg=tools.palette["light-green"])
        self.type_word.pack(side="left", padx=30)
        
        self.right_side2 = Frame(self.download_type, bg=tools.palette["green"])
        self.right_side2.pack(side="right", padx=30)
        
        
        def _SwitchType(file_type, vid_type, aud_type):
            nonlocal download_type

            if file_type == "Video":
                tools.download_prefered_type = "Video"
                vid_type.config(bg=tools.palette["dark-green"])
                aud_type.config(bg=tools.palette["green"])
            else:
                tools.download_prefered_type = "Audio"
                vid_type.config(bg=tools.palette["green"])
                aud_type.config(bg=tools.palette["dark-green"])
                        
        
        download_type = IntVar()
        
        vid_type = Radiobutton(self.right_side2, text="Video", variable=download_type, value=1, 
                               font=("Berlin Sans FB", 20), bg=tools.palette["dark-green"], fg=tools.palette["light-green"],
                               command=lambda: _SwitchType("Video", vid_type, aud_type), cursor="hand2",)
        aud_type = Radiobutton(self.right_side2, text="Audio", variable=download_type, value=2,
                               font=("Berlin Sans FB", 20), bg=tools.palette["green"], fg=tools.palette["light-green"],
                               command=lambda: _SwitchType("Audio", vid_type, aud_type), cursor="hand2",) 
        
        vid_type.pack(side="top", pady=10, padx=70)
        aud_type.pack(side="top", pady=10, padx=70)
        
        
    def _HandleBrowse(self, tools):
        self.folder_name = filedialog.askdirectory()
        tools.download_prefered_path = self.folder_name
        self.path_label.config(text=tools.download_prefered_path)
        
        
        
        
        
        
        
        