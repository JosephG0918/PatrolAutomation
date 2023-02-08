from tkinter import *
import os

class SampleGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Alpine Ascents Patrol Sum Automation")
        self.window.geometry("400x200")
        self.window.resizable(False, False)

        self.btn = Button(self.window, text="Click Me", bg="white", fg="black", height= 5, width=20, command=self.run).pack()

    def run(self):
        os.system("python " + "AlpinePatrolAutomation.py")

window = Tk()
SampleGUI(window)
window.mainloop()