# Imports
import os

interrupt_directory = "Interrupts"

def load_interrupts():
    interrupts = []
    for root, directory, files in os.walk(interrupt_directory):
        for file in files:
            if ".png" or ".jpg" in file:
                interrupts.append(os.path.join(root, file))
    return interrupts