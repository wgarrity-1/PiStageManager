from guizero import App, Text, MenuBar, info, PushButton, ListBox, Box
from tkinter import filedialog as fd
import sys
import webbrowser
import show_load #from show_load.py
import show_control #from show_control.py
import interrupt_load #from interrupt_load.py


# Variables
show_directory = "Please Select a Show Directory!"
interrupt_list = interrupt_load.load_interrupts() # List of interrupts in the interrupts folder


# Definitions
# Exit Command
def exit_menu_option():
    sys.exit()

# Open Show Command
def open_show():
    global show_directory
    show_directory = fd.askdirectory(initialdir = "/home", title="Please select the show folder") #Presents a diolog box to select a folder and save the directory to a variable
    show_folder_name.clear() #Clears the text at the top of the window
    show_folder_name.append("Show Folder: " + show_directory) #Changes the text with the show directory folder
    show_load.load(show_directory) #Calls the load function in show_load.py to initialize the show

# Command for the back button
def back_command():
    show_control.cue_backward() #Call the cue_backward function in show_control.py
    cue_number.clear() #Clears the cue text
    cue_number.append("Cue: " + str(show_control.current_cue)) #Changes the cue text to current cue number

# Command for the forward button, same as the back button but calls the forward command instread
def forward_command():
    show_control.cue_forward()
    cue_number.clear()
    cue_number.append("Cue: " + str(show_control.current_cue))

# Send Interrupt Command
def send_interrupt():
    selected_interrupt = interrupt_listbox.value #adds the current interrupt selected in the box to the variable selected_interrupt
    show_control.interrupt_show(selected_interrupt) #calls the interrupt_show function in show_control.py with the selected_interrupt as the parameter

# About command
def about():
    info("About PiStageManager", "PiStageManager 0.1 beta - Developed by will9183")

# View licence command
#def licence():
    #webbrowser.open("../LICENSE", new=2)

# Open Github Page Command
#def github():
    #webbrowser.open("https://github.com/will9183/PiStageManager", new=2)


# App
app = App(title="PiStageManager - Display Controller")
# Menubar with options
menubar = MenuBar(app,
                  toplevel=["File", "Help"],
                  options=[
                      [ ["Open Show", open_show], ["Exit", exit_menu_option] ],
                      [ ["About PiStageManager", about] ]
                      ])

# Text widget + box to display the show directory that is currently loaded
show_folder_box = Box(app, width="fill", align="top", border=True)
show_folder_name = Text(show_folder_box, text=show_directory, color="red")

# Control box where the slides can be controlled
control_box = Box(app, width="fill", border=True)
control_text = Text(control_box, text="Show display controls:")
cue_number = Text(control_box, text="Cue: 0")
back = PushButton(control_box, text="<", command=back_command, align="left")
forward = PushButton(control_box, text=">", command=forward_command, align="right")

# Interrupt box where interrupts can be selected and be sent
interrupt_box = Box(app, width="fill", align="bottom", border=True)
interrupt_text = Text(interrupt_box, text="Interrupts:")
interrupt_listbox = ListBox(interrupt_box, items=interrupt_list, width="fill")
interrupt_send = PushButton(interrupt_box, text="Send Selected Interrupt", command=send_interrupt, align="right")
interrupt_stop = PushButton(interrupt_box, text="Stop Interrupt", command=show_control.stop_interrupt, align="left")


app.display()