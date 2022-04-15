from tkinter import Frame, Label, Button, Radiobutton, filedialog, IntVar


class SettingsPage:
    """
    this page is for changing the default downloading path and the prefered downloading type (video or audio)
    
    Args:
        master (tkinter frame): the placement frame that will contain the page inside the main window's notebook
        tools (Tools instance): the tools instance that will be used to access the tools methods and attributes
    """
    
    def __init__(self, master, tools):
        # create the page frame and pack it
        self.page = Frame(master, bg=tools.palette["green"])
        self.page.pack(side="top", fill="both", expand=True)
        
        # call the private methods to create the page's frames 
        self._DownloadPath(tools)
        self._DownloadType(tools)
        
    
    def _DownloadPath(self, tools):
        """
        creates a frame, which is the first row in the page that contains the default downloading path
        """
        
        # create the frame and pack it
        self.download_path = Frame(self.page, bg=tools.palette["green"])
        self.download_path.pack(side="top", pady=30, fill="x", expand=True)
        
        # create the label that has the sentence and pack it
        self.path_word = Label(self.download_path, text="Change Default\nDownloading Path", font=("Berlin Sans FB", 30),
                                bg=tools.palette["green"], fg=tools.palette["light-green"])
        self.path_word.pack(side="left", padx=30)
        
        # create the frame that will contain the path label and the browse button
        self.right_side = Frame(self.download_path, bg=tools.palette["green"])
        self.right_side.pack(side="left")
        
        # create the browse button and pack it, it should be linked to the private method that will open a file dialog
        self.browse_button = Button(self.right_side, text="Browse", bg=tools.palette["dark-green"], cursor="hand2",
                                    fg=tools.palette["light-green"], font=("Berlin Sans FB", 20),
                                    command=lambda: self._HandleBrowse(tools))
        self.browse_button.pack(side="top", pady=10)
        
        # create the label that will contain the path and pack it
        self.path_label = Label(self.right_side, text=tools.download_prefered_path, font=("Berlin Sans FB", 15),
                                bg=tools.palette["green"], fg=tools.palette["light-green"], 
                                width=int(tools.screen_width*0.1), wraplength=int(tools.screen_width*0.30))
        self.path_label.pack(side="top", pady=10)
        
        
    def _DownloadType(self, tools):
        """
        creates a frame, which is the first row in the page that contains the default downloading type
        """
        
        # create the frame that will contain the label and the radio buttons and pack it
        self.download_type = Frame(self.page, bg=tools.palette["green"])
        self.download_type.pack(side="top", pady=30, fill="x", expand=True)
        
        # create the label that has the sentence and pack it
        self.type_word = Label(self.download_type, text="Change Prefered\nDownloading Type", font=("Berlin Sans FB", 30),
                                bg=tools.palette["green"], fg=tools.palette["light-green"])
        self.type_word.pack(side="left", padx=30)
        
        # create the frame that will contain the radio buttons and pack it
        self.right_side2 = Frame(self.download_type, bg=tools.palette["green"])
        self.right_side2.pack(side="left", padx=100)
        
        
        # create the local function that will be called when the user clicks on one of the radio buttons
        def _SwitchType(file_type, vid_type, aud_type):
            """
            this function is called when the user clicks on one of the radio buttons,
            it will change the label that shows the prefered type and its background color,
            it will also change the prefered downloading type on the tools instance and on the cashe file so
            we save the new prefered type in the cashe file and reach it again when the program starts

            Args:
                file_type (string): the new prefered type (video or audio)
                vid_type (Radiobutton): the video radio button
                aud_type (Radiobutton): the audio radio button
            """
            
            # if the user clicked on the video radio button, change the label and the background color
            # and vice versa for the audio radio button
            if file_type == "Video":
                self.download_type.set(1)
                vid_type.config(bg=tools.palette["dark-green"])
                aud_type.config(bg=tools.palette["green"])                
            else:
                self.download_type.set(2)
                vid_type.config(bg=tools.palette["green"])
                aud_type.config(bg=tools.palette["dark-green"])
                
            # change the prefered type on the tools instance and on the cashe file by opening the cashe file
            # on the read-mode to get the previous data and then write the new data on the cashe file
            tools.download_prefered_type = file_type
            data = []
            
            with open(r"youtube_download_manager\cashe\cashe.txt", "r") as f:
                data = f.readlines()
                f.close()
                
            with open(r"youtube_download_manager\cashe\cashe.txt", "w") as f:
                data[1] = data[1][:data[1].index(">")+1] + file_type + "\n"
                f.writelines(data)
                f.close()
        
                        
        # create the integer variable that will hold the state of the buttons 
        # then create the radio buttons and pack them                        
        self.download_type = IntVar()
        
        vid_type = Radiobutton(self.right_side2, text="Video", variable=self.download_type, value=1, 
                               font=("Berlin Sans FB", 20), bg=tools.palette["dark-green"], fg=tools.palette["light-green"],
                               command=lambda: _SwitchType("Video", vid_type, aud_type), cursor="hand2",)
        aud_type = Radiobutton(self.right_side2, text="Audio", variable=self.download_type, value=2,
                               font=("Berlin Sans FB", 20), bg=tools.palette["green"], fg=tools.palette["light-green"],
                               command=lambda: _SwitchType("Audio", vid_type, aud_type), cursor="hand2",) 
        
        vid_type.pack(side="top", pady=10)
        aud_type.pack(side="top", pady=10)
        
        # if the initial prefered type is video, call the local function with the video radio button as argument
        # and vice versa for the audio radio button
        if tools.download_prefered_type == "Video":
            _SwitchType("Video", vid_type, aud_type)
        elif tools.download_prefered_type == "Audio":
            _SwitchType("Audio", vid_type, aud_type)
        else:
            _SwitchType("Video", vid_type, aud_type)
        
        
    def _HandleBrowse(self, tools):
        """
        this function is called when the user clicks on the browse button

        Args:
            tools (Tools instance): the tools instance that has all the tools that the program needs
        """
        
        # open the file dialog and get the path that the user chose
        folder_name = filedialog.askdirectory()
        
        # if the user didn't chose a path, change the path label to error message 
        if folder_name == "":
            self.path_label.config(text="You have to select a valid path name !")
            return

        # if the user chose a valid path, 
        # change the path label and the prefered path on the tools instance        
        tools.download_prefered_path = folder_name
        self.path_label.config(text=tools.download_prefered_path)
        
        # open the cashe file on the read-mode to get the previous data and then write the new data on the cashe file
        data = []
            
        with open(r"youtube_download_manager\cashe\cashe.txt", "r") as f:
            data = f.readlines()
            f.close()
            
        with open(r"youtube_download_manager\cashe\cashe.txt", "w") as f:
            data[0] = data[0][:data[0].index(">")+1] + folder_name  + "\n"
            f.writelines(data)
            f.close()
        
        
        
        
        
        
        
        