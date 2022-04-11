from pages.main_page import MainWindow        
from tkinter import Tk 
from PIL import Image, ImageTk, ImageDraw, ImageFilter

class Tools:
    def __init__(self):
        self.screen_width = 0
        self.screen_height = 0
        
        self.palette =  {"purple": "#8A39E1", 
                        "green": "#62BAAC",
                        "light-green": "#C3FCF1",
                        "dark-green": "#4B8078"}
        
        self.download_prefered_path = r".\youtube_download_manager\downloads"
        self.download_prefered_type = "Video"
    
    
    def mask_circle_transparent(self, pil_img, blur_radius, offset=0):
            offset = blur_radius * 2 + offset
            mask = Image.new("L", pil_img.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
            mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
            result = pil_img.copy()
            result.putalpha(mask)
            return result
        
        
        
wind = Tk()
wind.title("YouTube Download Manager")       
wind.resizable(0, 0)

tools = Tools()
tools.screen_width = wind.winfo_screenwidth()
tools.screen_height = wind.winfo_screenheight()

app = MainWindow(wind, tools)

app.wind.mainloop()

