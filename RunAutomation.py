# "List of CMs" is important, must be changed if one leaves or joins.

from tkinter import *
import re

class SampleGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Alpine Ascents Patrol Sum Automation")
        self.window.geometry("400x212")
        self.window.resizable(False, False)
        
        self.btn = Button(self.window, text="Run Automation", bg="white", fg="black", height= 5, width=20, command=self.run)
        self.btn.pack(pady=43)
        self.output = Text(self.window, font=('Arial', 20), height=1, width=20)
        self.output.pack()

        # -------------List of CMs-------------
        self.dude08_PatrolTimeInMin = []
        self.dude08Time = []
        self.dude08_total = 0
        self.adidazboy_PatrolTimeInMin = []
        self.adidazboyTime = []
        self.adidazboy_total = 0
        self.boring_PatrolTimeInMin = []
        self.boringTime = []
        self.boring_total = 0
        self.rosegirl_PatrolTimeInMin = []
        self.rosegirlTime = []
        self.rosegirl_total = 0
        # -------------------------------------

    def GetTime(self):
        with open('data.txt', 'r') as file:
            data = file.read().replace('\n', '')

        listOfCMs = ["Dude080721", "AdidazBoy123", "boringpjtx", "rosegirlye"] # List of CM names.
        listOfCMData = data.split("Paul") # Delimiter

        for i in listOfCMData:
            if i == '':
                continue
            else:
                cm = re.findall('@(.+)Total', i)[0]
                for j in listOfCMs:
                    if cm == j:
                        patrolTime = re.findall("[0-9]+[hm]", i)
                        # -------------List of CMs-------------
                        if cm == "Dude080721":
                            for k in patrolTime:
                                self.dude08Time.append(k)
                            patrolTime = []
                        elif cm == "AdidazBoy123":
                            for k in patrolTime:
                                self.adidazboyTime.append(k)
                            patrolTime = []
                        elif cm == "boringpjtx":
                            for k in patrolTime:
                                self.boringTime.append(k)
                            patrolTime = []
                        elif cm == "rosegirlye":
                            for k in patrolTime:
                                self.rosegirlTime.append(k)
                            patrolTime = []
                        # -------------------------------------
                    else:
                        continue

    def CaculateTime(self):

        # -------------List of CMs-------------
        for i in self.dude08Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.dude08_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.dude08_PatrolTimeInMin.append(minutes)
        for integer in self.dude08_PatrolTimeInMin:
            self.dude08_total += integer

        for i in self.adidazboyTime:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.adidazboy_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.adidazboy_PatrolTimeInMin.append(minutes)
        for integer in self.adidazboy_PatrolTimeInMin:
            self.adidazboy_total += integer

        for i in self.boringTime:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.boring_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.boring_PatrolTimeInMin.append(minutes)
        for integer in self.boring_PatrolTimeInMin:
            self.boring_total += integer

        for i in self.rosegirlTime:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.rosegirl_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.rosegirl_PatrolTimeInMin.append(minutes)
        for integer in self.rosegirl_PatrolTimeInMin:
            self.rosegirl_total += integer
        # -------------------------------------

    def PostResults(self):
        with open('results.txt', 'w+') as file:
            # -------------List of CMs-------------
            file.write(f"Dude080721: {self.dude08_total} minutes.\n")
            file.write(f"AdidazBoy123: {self.adidazboy_total} minutes.\n")
            file.write(f"boringpjtx: {self.boring_total} minutes.\n")
            file.write(f"rosegirlye: {self.rosegirl_total} minutes.\n")
            # -------------------------------------

    def switchButtonState(self):
        if (self.btn['state'] == NORMAL):
            self.btn.config(state=DISABLED)
        else:
            self.btn.config(state=DISABLED)

    def run(self):
        if __name__ == "__main__":
            self.output.delete('1.0', END)
            self.GetTime()
            self.CaculateTime()
            self.PostResults()
            self.output.insert(INSERT, "Finished! See results.txt")
            self.switchButtonState()

window = Tk()
SampleGUI(window)
window.mainloop()