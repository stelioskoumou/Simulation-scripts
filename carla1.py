# This is a test script. It emulates an execution of a CARLA script
# under a certain configuration. The user of the Orchestrator tool
# should replace it with actual CARLA Python API scripts.

from tkinter import *
window = Tk()
lbl = Label(
    window,
    text="You chose to simulate with CARLA, under Configuration 1!",
    fg="blue",
    bg='#299617',
    font="Consolas 15 bold"
    )
lbl.pack()
window.mainloop()
