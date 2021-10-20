# This is a test script. It emulates an execution of a CARLA script
# under a certain configuration. The user of the Orchestrator tool
# should replace it with actual CARLA Python API scripts.

from tkinter import *
root = Tk()
lbl = Label(
    root,
    text="You chose to simulate with SUMO, under Configuration 5!",
    fg="#FFFFFF",
    bg='#299617',
    font="Cambria 15 bold"
    )
lbl.pack()
root.mainloop()