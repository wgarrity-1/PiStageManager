import os

interrupt_directory = "Interrupts"

# Goes into the interrupt directory and returns the images in the folder
def load_interrupts():
    interrupts = []
    for root, directory, files in os.walk(interrupt_directory):
        for file in files:
            if ".png" or ".jpg" in file:
                interrupts.append(os.path.join(root, file))
    return interrupts