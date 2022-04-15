from pages.main_page import MainWindow        
from tkinter import Tk 
from PIL import Image, ImageDraw, ImageFilter

class Tools:
    """
    a class that has the useful attributes and methods we want to share across the program
    """
    
    def __init__(self):
        # initialize values for screen width, screen height, preferred download folder, and the palette of colors
        self.screen_width = 0
        self.screen_height = 0
        self.download_prefered_path = ""
        self.palette =  {"purple": "#8A39E1", 
                        "green": "#62BAAC",
                        "light-green": "#C3FCF1",
                        "dark-green": "#4B8078"}
        
        # open the cashe file to get the prefered download folder and prefered download type
        # set thier values to the class attributes and close the file
        with open(r"youtube_download_manager\cashe\cashe.txt", "r") as f:
            data = f.readlines() 
            self.download_prefered_path = data[0][data[0].index(">")+1:].strip()
            self.download_prefered_type = data[1][data[1].index(">")+1:].strip()
            f.close()
    
    
    def mask_circle_transparent(self, pil_img, blur_radius, offset=0):
        """
        this method cut a PIL image as a circle and make the background transparent

        Args:
            pil_img (PIL image): the image that will be cut as a circle
            blur_radius (_type_): the radius of the blur that will be applied to the image
            offset (int, optional): the offset of the circle from the center of the image, defaults to 0

        Returns:
            PIL image: the image that has been cut as a circle and made transparent
        """
        
        offset = blur_radius * 2 + offset
        mask = Image.new("L", pil_img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
        result = pil_img.copy()
        result.putalpha(mask)
        
        return result
    

if __name__ == "__main__":
    # create the main window, give it a title, and prevent it from resizing
    wind = Tk()
    wind.title("YouTube Download Manager")       
    wind.resizable(0, 0)

    # create the tools instance 
    tools = Tools()
    
    # get the screen width and height and set them as width and height attributes of the tools instance
    tools.screen_width = wind.winfo_screenwidth()
    tools.screen_height = wind.winfo_screenheight()

    # launch the main window and give it the tools instance
    app = MainWindow(wind, tools)

    # close the loop so the window can be run successfully
    app.wind.mainloop()

