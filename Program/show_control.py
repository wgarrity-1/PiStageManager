import show_load
import shutil # for file copy stuff


# Variables for determining the length of the slideshow and current cue
cue_min = 0
cue_max = 0
current_cue = 0


# Sets image onto html file (not yet though)
def set_image():
    shutil.copy(show_load.show_slides[current_cue], "Current Slide/current.png")
    print("Current slide: " + show_load.show_slides[current_cue])

# Determines the length of the list, subtracts 1, and then adds it to cue_max for the max cue that the slideshow contains
def find_cue_max():
    global cue_max
    cue_max = len(show_load.show_slides) - 1
    print(cue_max)

# Cue forward command
def cue_forward():
    global current_cue
    if current_cue < cue_max:
        current_cue += 1
        set_image()
    else:
        print("You have reached the end of the show.")

# Cue backward command
def cue_backward():
    global current_cue
    if current_cue > cue_min:
        current_cue -= 1
        set_image()
    else:
        print("You are already at the beginning of the show.")

# Interrupt Selection Command
def interrupt_show(interrupt_slide):
    shutil.copy(interrupt_slide, "Current Slide/current.png")
    print("Interrupt!: " + interrupt_slide)

# Stops the interrupt, kind of a useless function as it just calls another function
def stop_interrupt():
    print("Interrupt Stopped!")
    set_image()

# Debug command
def debug():
    print("Cue_min: " + str(cue_min))
    print("Cue_max: " + str(cue_max))
    print("Current_cue: " + str(current_cue))
    print("Show_slides: ")
    print(len(show_load.show_slides))