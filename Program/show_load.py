import os
import show_control

show_slides = [] #empty list, used later to add the images in the selected show folder

# Main loading function: takes show directory and outputs all image files into a list then sorts that list
def load(show):
    
    # Goes through each file in the os.walk list and appends the location of the image files into the show_slides list with its directory root
    for root, directory, files in os.walk(show):
        for file in files:
            if ".png" or ".jpg" in file:
                show_slides.append(os.path.join(root, file))
                
    print(show + " is loaded!")
    
    # Sorts the list so that all images are in order
    show_slides.sort()
    print(show_slides)
    
    show_control.find_cue_max() #Calls the find_cue_max function in show_control.py to determine the final cue that can be called
    show_control.set_image() #Calls the set_image function in show_control.py to set the display to the first image