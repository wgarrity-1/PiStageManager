import os
import shutil

# PiStageManager backend
def debug():
    print("Cue_min: " + str(ShowController.cue_min))
    print("Cue_max: " + str(ShowController.cue_max))
    print("Current_cue: " + str(ShowController.current_cue))
    print("Show_slides: ")
    print(len(ShowLoader.show_slides))

class ShowController:
    cue_min = 0
    cue_max = 0
    current_cue = 0
    
    def set(self):
        shutil.copy(ShowLoader.show_slides[ShowController.current_cue], "Current Slide/current.png")
        print("Current slide: " + ShowLoader.show_slides[ShowController.current_cue])
    
    def forward(self):
        if ShowController.current_cue < ShowController.cue_max:
            ShowController.current_cue += 1
            self.set()
        else:
            print("You have reached the end of the show.")
        
    def back(self):
        if ShowController.current_cue > ShowController.cue_min:
            ShowController.current_cue -= 1
            self.set()
        else:
            print("You have reached the beginning of the show.")
        
    def interrupt(self, interrupt_slide):
        shutil.copy(interrupt_slide, "Current Slide/current.png")
        print("Interrupt!: " + interrupt_slide)
        

class ShowLoader:
    interrupt_directory = "Interrupts"
    show_slides = [] #empty list, used later to add the images in the selected show folder
    
    def interrupt_loader(self):
        interrupts = []
        for root, directory, files in os.walk(self.interrupt_directory):
            for file in files:
                if ".png" or ".jpg" in file:
                    interrupts.append(os.path.join(root, file))
        return interrupts
        
    def set_init(self):
        ShowController.set(self)
        
    def show_loader(self, show):
        # Goes through each file in the os.walk list and appends the location of the image files into the show_slides list with its directory root
        for root, directory, files in os.walk(show):
            for file in files:
                if ".png" or ".jpg" in file:
                    self.show_slides.append(os.path.join(root, file))
                    
        
        # Sorts the list so that all images are in order
        self.show_slides.sort()
        print(self.show_slides)
        
        ShowController.cue_max = len(self.show_slides) - 1
        print(ShowController.cue_max)
        
        self.set_init()
        

