class Image:
    def __init__(self, resolution: str, title: str, extension:str):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, newResolution):
        self.resolution = newResolution
    
    def getTitle(self):
        return self.title;

    
img = Image("600x600", 'My image', 'jpg')
print(img.getTitle())