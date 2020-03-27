# Imports
import os
import show_control

# List for all of the slides in the folder
show_slides = []

# Main loading function, takes show directory and outputs all image files into a list then sorts that list
def load(show):
    
    # Goes through each file in the os.walk list and appends the location of the image files into the show_slides list
    for root, directory, files in os.walk(show):
        for file in files:
            if ".png" or ".jpg" in file:
                show_slides.append(os.path.join(root, file))
                
    print(show + " is loaded!")
    
    # Sorts the list so that all images are in order
    show_slides.sort()
    print(show_slides)
    
    # Finds the last cue and then sets the show for the first cue
    show_control.find_cue_max()
    show_control.set_image()