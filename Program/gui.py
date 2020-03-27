# Imports

# Import guizero for the gui
from guizero import App, Text, MenuBar, info, PushButton, ListBox, Box
# Import for the file dialog box
from tkinter import filedialog as fd
# Import sys so quit option in menu can work properly
import sys
# Imports show loading features
import show_load
# Imports show controling features
import show_control
# Imports interrupt loader
import interrupt_load

# Variables

# Show folder's directory
show_directory = "Please Select a Show Directory!"

interrupt_list = interrupt_load.load_interrupts()

# Definitions

# Exit Command
def exit_menu_option():
    sys.exit()

# Load Show Command, presents a diolog box to select a folder, then saves it to a variable, then it updates the text at the top of the app
def open_show():
    global show_directory
    show_directory = fd.askdirectory(initialdir = "/home", title="Please select the show folder")
    show_folder_name.clear()
    show_folder_name.append("Show Folder: " + show_directory)
    show_load.load(show_directory)

# Command for the back button
def back_command():
    show_control.cue_backward()
    cue_number.clear()
    cue_number.append("Cue: " + str(show_control.current_cue))

# Command for the forward button
def forward_command():
    show_control.cue_forward()
    cue_number.clear()
    cue_number.append("Cue: " + str(show_control.current_cue))

# Send Interrupt Command
def send_interrupt():
    selected_interrupt = interrupt_listbox.value
    show_control.interrupt_show(selected_interrupt)

# Dummy Help Command
def help_command():
    info("Help", "This program is unfinished so no help for you!")



# App
app = App(title="PiStageManager - Display Controller")

# Menubar
menubar = MenuBar(app,
                  toplevel=["File", "Help"],
                  options=[
                      [ ["Open Show", open_show], ["Exit", exit_menu_option] ],
                      [ ["Help", help_command], ["Debug", show_control.debug] ]
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