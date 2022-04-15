from tkinter import Frame, Label, Button, Image, Entry, StringVar, Toplevel, messagebox
from tkinter.ttk import Combobox, Progressbar
from PIL import Image, ImageTk
from pafy import new
import urllib.request
import io
import threading

class DownloadPage:
    """
    the page is divided into two frames, the upper frame and the lower frame
    
    Args:
        master (tkinter frame): the placement frame that will contain the page inside the main window's notebook
        tools (Tools instance): the tools instance that will be used to access the tools methods and attributes
    """
    
    def __init__(self, master, tools):
        # create the page frame and set the tools instance
        self.master = master
        self.page = Frame(master, bg=tools.palette["green"])
        self.page.pack(side="top", fill="both", expand=True)
        self.tools = tools
        
        # create some attributes that will be used to check some real-time conditions
        self.title = None                   # used to check if we applied a request or not 
        self.requesting_data = False        # used to check if we are requesting data currently or not
        self.downloading_process = False    # used to check if we are downloading a file currently or not
        
        # create the entry variable that will be used to store the url
        self.url = StringVar()          # test: https://www.youtube.com/watch?v=H9154xIoYTA
                
        # call the methods that will create the upper and lower frames
        self._UpperFrame()
        self._LowerFrame()
        
    
    def _UpperFrame(self):
        """
        the upper frame contains the url entry and the request button
        """
        
        # initialize the pallate and the width 
        palette, width = self.tools.palette, self.tools.screen_width

        # create the upper frame and attach it in a grid layout (0, 0)
        self.upper_frame = Frame(self.page, bg=palette["green"])
        self.upper_frame.grid(row=0, column=0)
        self.upper_frame.grid_rowconfigure(0, weight=1)
        
        # create the url label and attach it in an inner grid layout (0, 0)
        self.url_label = Label(self.upper_frame, text="URL: ", bg=palette["green"], fg=palette["light-green"],
                               font=("Berlin Sans FB", 20))
        self.url_label.grid(row=0, column=0, sticky="w", padx=15, pady=20)
        self.url_label.grid_columnconfigure(0, weight=1)
        
        # create the url entry and attach it in an inner grid layout (0, 1)
        self.url_entry = Entry(self.upper_frame, bg=palette["dark-green"], fg=palette["light-green"], 
                               font=("Berlin Sans FB", 20), width=int(width*0.025), textvariable=self.url)
        self.url_entry.grid(row=0, column=1, sticky="e", padx=15,  pady=20)
        self.url_entry.grid_columnconfigure(1, weight=1)
        
        # create the request button and attach it in an inner grid layout (0, 2)
        self.request_button = Button(self.upper_frame, text="Request", bg=palette["dark-green"], 
                                     command=lambda: self._HandleRequest(), cursor="hand2",
                                     fg=palette["light-green"], font=("Berlin Sans FB", 20), width=int(width*0.005))
        self.request_button.grid(row=0, column=2, sticky="e", padx=15,  pady=20)
        self.request_button.grid_columnconfigure(2, weight=1)
        
        
    def _LowerFrame(self):
        """
        the lower frame contains a splash area, a progress bar, a selection entry, and a download button
        """
        
        # initialize the palette and the width
        palette, width = self.tools.palette, self.tools.screen_width
        
        # create the lower frame and attach it in a grid layout (1, 0)
        self.lower_frame = Frame(self.page, bg=palette["green"], width=int(width))
        self.lower_frame.grid(row=1, column=0)
        self.lower_frame.grid_rowconfigure(1, weight=1)
        
        # create the splash area and attach it in an inner grid layout (0, 0) and a span of (3, 3)
        # the splash area will contain the video's image, title, author, duration, likes, dislikes, and views
        self.splash_img = Image.open(r"youtube_download_manager\assets\icon.png")
        self.splash_img = self.splash_img.resize((int(width*0.23), int(width*0.23)))
        self.splash_img = ImageTk.PhotoImage(self.splash_img)
        self.thumbnail = Label(self.lower_frame, image=self.splash_img, bg=palette["purple"])
        self.thumbnail.image = self.splash_img
        self.thumbnail.grid(row=0, column=0, columnspan=3, rowspan=3)
        
        # create the middle frame  and attach it in an inner grid layout (1, 3) and a span of (3, 3)
        self.middle_frame = Frame(self.lower_frame, bg=palette["green"])
        self.middle_frame.grid(row=1, column=3, columnspan=3, rowspan=3, padx=10)
        
        # create the title, author, and duration labels and top-pack them in an inner grid of the middle frame
        self.vid_title = Label(self.middle_frame, text="---Title---", wraplength=int(width*0.15),bg=palette["green"], 
                               width=int(width*0.015), font=("Berlin Sans FB", 15, "bold"), justify="center")
        self.vid_title.pack(side="top")
        
        self.vid_author = Label(self.middle_frame, text="\n\n---Author---", wraplength=int(width*0.15),bg=palette["green"], 
                               width=int(width*0.015), font=("Berlin Sans FB", 15, "bold"), justify="center")
        self.vid_author.pack(side="top")
        
        self.vid_duration = Label(self.middle_frame, text="\n\n---Duration---", wraplength=int(width*0.15),bg=palette["green"], 
                               width=int(width*0.015), font=("Berlin Sans FB", 15, "bold"), justify="center")
        self.vid_duration.pack(side="top")
        
        # create the likes, dislikes, and views labels and attach them them in an inner grid 
        # of the lower frame at (3, 0), (3, 1), and (3, 2) where span is (1, 1)
        # these are static labels that will not be updated
        self.vid_views_word = Label(self.lower_frame, text="Views", bg=palette["green"], 
                                    font=("Berlin Sans FB", 15, "bold"), fg=palette["purple"])
        self.vid_views_word.grid(row=3, column=0, columnspan=1, rowspan=1)
        
        self.vid_likes_word = Label(self.lower_frame, text="Likes", bg=palette["green"], 
                                    font=("Berlin Sans FB", 15, "bold"), fg=palette["purple"])
        self.vid_likes_word.grid(row=3, column=1, columnspan=1, rowspan=1)
        
        self.vid_dislikes_word = Label(self.lower_frame, text="Dislikes", bg=palette["green"], 
                                       font=("Berlin Sans FB", 15, "bold"), fg=palette["purple"])
        self.vid_dislikes_word.grid(row=3, column=2, columnspan=1, rowspan=1)
        
        # create the views, likes, and dislikes labels and attach them in an inner grid 
        # of the lower frame at (4, 0), (4, 1), and (4, 2) where span is (1, 1)
        # these are dynamic labels that will be updated when the request button is pressed
        self.vid_views = Label(self.lower_frame, text="---", bg=palette["green"], font=("Berlin Sans FB", 15))
        self.vid_views.grid(row=4, column=0, columnspan=1, rowspan=1)
        
        self.vid_likes = Label(self.lower_frame, text="---", bg=palette["green"], font=("Berlin Sans FB", 15))
        self.vid_likes.grid(row=4, column=1, columnspan=1, rowspan=1)
        
        self.vid_dislikes = Label(self.lower_frame, text="---", bg=palette["green"], font=("Berlin Sans FB", 15))
        self.vid_dislikes.grid(row=4, column=2, columnspan=1, rowspan=1)
        
        # create the upper-right frame and attach it in an inner grid layout (1, 6) and a span of (1, 1)
        self.right_upper = Frame(self.lower_frame, bg=palette["green"])
        self.right_upper.grid(row=1, column=6, columnspan=1, rowspan=1, padx=10)
        
        # create the label and progress bar and top-pack them in the inner grid layout of the upper-right frame
        self.requesting_state = Label(self.right_upper, text="State: \nNothing to get", bg=palette["green"], 
                                      width=int(width*0.008), fg=palette["light-green"], font=("Berlin Sans FB", 15))
        self.requesting_state.pack(side="top", pady=4)
        
        self.requesting_bar = Progressbar(self.right_upper, orient="horizontal", length=int(width*0.08), 
                                          mode="determinate", value=0)
        self.requesting_bar.pack(side="top", pady=4)
        
        # create the selection label and spinbox and top-pack them in the inner grid layout of the upper-right frame
        self.select_word = Label(self.right_upper, text="\nSelect a type:", bg=palette["green"], 
                                 font=("Berlin Sans FB", 15), fg="black")
        self.select_word.pack(side="top")
        
        self.type_selection = Combobox(self.right_upper, values=["Video", "Audio"], width=int(width*0.006), 
                                       foreground="black", font=("Berlin Sans FB", 15), state= "readonly")        
        self.type_selection.pack(side="top", pady=4)
        
        # if the default preferred type is video, set the spinbo on the video option, and vice versa for audio
        if self.tools.download_prefered_type == "Video":
            self.type_selection.current(0)
        else:
            self.type_selection.current(1)
        
        # import the download image and cut it into a circle
        self.download_img = Image.open(r"youtube_download_manager\assets\downloads.ico")
        self.download_img = self.download_img.resize((int(width*0.05), int(width*0.05)))
        self.tools.mask_circle_transparent(self.download_img, 1.5)
        self.download_img = ImageTk.PhotoImage(self.download_img)

        # create the download button and attach it in an inner grid layout of the lower frame at (2, 6) and a span of (1, 1) 
        self.download_button = Button(self.lower_frame, image=self.download_img, bg=palette["green"], cursor="hand2",
                                      font=("Berlin Sans FB", 15), bd=0, activebackground=palette["green"],
                                      command=lambda: self._HandleDownload())
        self.download_button.image = self.download_img
        self.download_button.grid(row=2, column=6, columnspan=1, rowspan=1, padx=10)
        
        
    def _HandleRequest(self):
        """
        this function handles the request button press, it will check if the user has entered a valid url, 
        then it will fire up a thread to get the video's information and update the labels accordingly
        """
        
        def _req():
            """
            this function contains only an inner function that will be called internally as a thread,
            that will allow the program to get the video's information and still running the GUI with 
            no lags
            
            the thread is a flow that works as an individual program, so it will not interfere with the GUI
            
            while requesting, the progress bar and the requesting state label will be updated
            """
            
            # if there is a request in progress, raise an error message and stop the function
            if self.requesting_data:
                messagebox.showerror("Request is running !!!", "There is a request running currently, please wait until it is finished.")
                return
            
            # start the progress bar and set the requesting data to true
            self.requesting_data = True
            self.requesting_bar.start(10)
            self.requesting_state.config(text="State: \nRequesting ...")
            
            # fire up a GET request to get the video's information
            url = self.url.get()
            width = self.tools.screen_width
            pafy_pbj = new(url)
            
            # feched the video's information
            self.thumb = pafy_pbj.bigthumbhd
            self.title = pafy_pbj.title
            author = pafy_pbj.author
            self.duration = pafy_pbj.duration
            likes = pafy_pbj.likes
            dislikes = pafy_pbj.dislikes
            viewcount = pafy_pbj.viewcount
            
            # use the feched information to update the labels
            self.vid_title.config(text=f"---Title---\n{self.title}")
            self.vid_author.config(text=f"\n---Author---\n{author}")
            self.vid_duration.config(text=f"\n---Duration---\n{self.duration}")
            self.vid_likes.config(text=f"{likes:,}")
            self.vid_dislikes.config(text=f"{dislikes}")
            self.vid_views.config(text=f"{viewcount:,}")
            
            # import the image from the fechted url and update the splash image label 
            raw_data = urllib.request.urlopen(self.thumb).read()
            im = Image.open(io.BytesIO(raw_data))
            image = im.resize((int(width*0.23), int(width*0.23)))
            image = ImageTk.PhotoImage(image)
            self.thumbnail.image = image
            self.thumbnail.config(image=image)
            
            # after finishing the request, set the requesting data to false and stop the progress bar
            self.requesting_data = False
            self.requesting_bar.stop()
            self.requesting_state.config(text="State: \nNothing to get")
            
            
        # start a thread to handle the request
        threading.Thread(target=_req).start()
        
        
    def _HandleDownload(self):
        """
        
        """
        
        # create the palette
        palette = self.tools.palette

        
        def _req():
            """
            this function will be fired up as a thread to get the video's information before downloading
            """
            
            # if there is a request in progress, raise an error message and stop the function            
            if self.requesting_data:
                messagebox.showerror("Request is running !!!", "There is a request running currently, please wait until it is finished.")
                return
            
            # if the user has not entered a valid Youtube url, raise an error message and stop the function
            if not str(self.url.get()).count("youtube.com/watch?v=") == 1:
                messagebox.showerror("Invalid Youtube URL !!!", "The URL you entered is not a valid Youtube URL !!!")
                return
            
            # if the reuest button has not been pressed, raise an error message and stop the function
            if self.title is None:
                messagebox.showerror("No request yet !", "You have to request a video first !!!")
                return
            
            # get the type that the user has selected
            self.file_type = self.type_selection.get()
        
            # the message that will be displayed in the confirmation box
            msg = f"""
            You are about to download the following file:
            Title: {self.title}
            Duration: {self.duration} 
            Type: {self.file_type}       
            """
            
            # confirm the download by clicking the yes button
            download_approval = messagebox.askokcancel("Download Wizard", msg)  
            
            # if the user has not confirmed the download, stop the function
            if not download_approval:
                return
            
            # create a download wizard window to display that the download is in progress
            self.download_wizard = Toplevel(self.master, bg=palette["light-green"], width=600, height=300)
            
            # attach the title of the video and a progress bar to the window
            download_title = Label(self.download_wizard, text=f"{self.title}\nDownloading ...", bg=palette["light-green"], 
                                font=("Berlin Sans FB", 15, "bold"), fg="black")
            download_title.pack(padx=10, pady=20)
            
            self.download_progress = Progressbar(self.download_wizard, orient="horizontal", length=400, 
                                                 mode="determinate", value=0)
            self.download_progress.pack(padx=10, pady=20)
            
            # set the requesting data to true and start the progress bar, 
            # once the request is finished, set the requesting data to false  
            self.requesting_data = True
            self.pafy_obj = new(self.url.get())
            self.requesting_data = False
            
            # select a proper stream for the file according to the user's selection
            if self.file_type == "Video":
                my_stream = self.pafy_obj.getbestvideo(preftype="mp4")
            else:
                my_stream = self.pafy_obj.audiostreams[0]
            
            
            def _download_file(my_stream):
                """
                this function will be fired up as a thread to download the file 
                """
                
                # if there is a file downloading now, raise an error message and stop the function
                if self.downloading_process:
                    messagebox.showerror("File is downloading !!!", "There is a file downloading currently, please wait until it is finished.")
                    return
                
                # set the downloading process to true and start the progress bar
                self.downloading_process = True
                self.download_progress.start(5)
                
                # download the file
                my_stream.download(self.tools.download_prefered_path)
                
                # once the file is downloaded, set the downloading process to false and stop the progress bar
                self.downloading_process = False
                self.download_progress.stop()
                
                # a message will be displayed to the user that the file has been downloaded
                done = f"""
                Downloading the following file is done:
                {self.title}
                
                You can find it in the "downloads" folder.
                """
                
                # show the message to the user
                messagebox.showinfo("Done boss !!!", done)
                
                # clear the requested data and close the download wizard window
                self.Clear()
                self.download_wizard.destroy()

            
            # fire up the thread to download the file
            threading.Thread(target=_download_file, args=(my_stream,)).start()


        # fire up the thread to get the video's information
        threading.Thread(target=_req).start()
                        

    def Clear(self):
        """
        this function clears the labels, the entry, and set the splash image to default
        it shall be called when the download is done  
        """
        
        # get the width
        width = self.tools.screen_width
        
        # clear the url entry
        self.url.set("")
        
        # clear the labels
        self.vid_title.config(text="---Title---")
        self.vid_author.config(text="\n\n---Author---")
        self.vid_duration.config(text="\n\n---Duration---")
        self.vid_likes.config(text="---")
        self.vid_dislikes.config(text="---")
        self.vid_views.config(text="---")
        
        # set the splash image to default
        self.splash_img = Image.open(r"youtube_download_manager\assets\icon.png")
        self.splash_img = self.splash_img.resize((int(width*0.23), int(width*0.23)))
        self.splash_img = ImageTk.PhotoImage(self.splash_img)
        self.thumbnail.config(image=self.splash_img)        
        self.thumbnail.image = self.splash_img
        
        
        
        