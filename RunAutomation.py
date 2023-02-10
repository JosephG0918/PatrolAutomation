# Not actually hard coding CM names, just placeholders.

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
        self.extractedCMs = []

        # -------------List of CMs-------------
        self.subject1_PatrolTimeInMin = []
        self.subject1Time = []
        self.subject1_total = 0
        self.subject2_PatrolTimeInMin = []
        self.subject2Time = []
        self.subject2_total = 0
        self.subject3_PatrolTimeInMin = []
        self.subject3Time = []
        self.subject3_total = 0
        self.subject4_PatrolTimeInMin = []
        self.subject4Time = []
        self.subject4_total = 0
        self.subject5_PatrolTimeInMin = []
        self.subject5Time = []
        self.subject5_total = 0
        self.subject6_PatrolTimeInMin = []
        self.subject6Time = []
        self.subject6_total = 0
        self.subject7_PatrolTimeInMin = []
        self.subject7Time = []
        self.subject7_total = 0
        self.subject8_PatrolTimeInMin = []
        self.subject8Time = []
        self.subject8_total = 0
        self.subject9_PatrolTimeInMin = []
        self.subject9Time = []
        self.subject9_total = 0
        self.subject10_PatrolTimeInMin = []
        self.subject10Time = []
        self.subject10_total = 0
        self.subject11_PatrolTimeInMin = []
        self.subject11Time = []
        self.subject11_total = 0
        self.subject12_PatrolTimeInMin = []
        self.subject12Time = []
        self.subject12_total = 0
        self.subject13_PatrolTimeInMin = []
        self.subject13Time = []
        self.subject13_total = 0
        self.subject14_PatrolTimeInMin = []
        self.subject14Time = []
        self.subject14_total = 0
        self.subject15_PatrolTimeInMin = []
        self.subject15Time = []
        self.subject15_total = 0
        self.subject16_PatrolTimeInMin = []
        self.subject16Time = []
        self.subject16_total = 0
        self.subject17_PatrolTimeInMin = []
        self.subject17Time = []
        self.subject17_total = 0
        self.subject18_PatrolTimeInMin = []
        self.subject18Time = []
        self.subject18_total = 0
        self.subject19_PatrolTimeInMin = []
        self.subject19Time = []
        self.subject19_total = 0
        self.subject20_PatrolTimeInMin = []
        self.subject20Time = []
        self.subject20_total = 0
        # -------------------------------------

    def getTime(self):
        with open('data.txt', 'r') as file:
            data = file.read().replace('\n', '')
        with open('CommunityManagers.txt', 'r') as cmFile:
            self.extractedCMs = cmFile.read().replace('\n','')
            self.extractedCMs = self.extractedCMs.split(";")

        listOfCMs = self.extractedCMs # List of CM names.
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
                        if cm == self.extractedCMs[0]:
                            for k in patrolTime:
                                self.subject1Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[1]:
                            for k in patrolTime:
                                self.subject2Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[2]:
                            for k in patrolTime:
                                self.subject3Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[3]:
                            for k in patrolTime:
                                self.subject4Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[4]:
                            for k in patrolTime:
                                self.subject5Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[5]:
                            for k in patrolTime:
                                self.subject6Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[6]:
                            for k in patrolTime:
                                self.subject7Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[7]:
                            for k in patrolTime:
                                self.subject8Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[8]:
                            for k in patrolTime:
                                self.subject9Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[9]:
                            for k in patrolTime:
                                self.subject10Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[10]:
                            for k in patrolTime:
                                self.subject11Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[11]:
                            for k in patrolTime:
                                self.subject12Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[12]:
                            for k in patrolTime:
                                self.subject13Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[13]:
                            for k in patrolTime:
                                self.subject14Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[14]:
                            for k in patrolTime:
                                self.subject15Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[15]:
                            for k in patrolTime:
                                self.subject16Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[16]:
                            for k in patrolTime:
                                self.subject17Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[17]:
                            for k in patrolTime:
                                self.subject18Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[18]:
                            for k in patrolTime:
                                self.subject19Time.append(k)
                            patrolTime = []
                        elif cm == self.extractedCMs[19]:
                            for k in patrolTime:
                                self.subject20Time.append(k)
                            patrolTime = []
                        # -------------------------------------
                    else:
                        continue

    def caculateTime(self):
        # -------------List of CMs-------------
        for i in self.subject1Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject1_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject1_PatrolTimeInMin.append(minutes)
        for integer in self.subject1_PatrolTimeInMin:
            self.subject1_total += integer

        for i in self.subject2Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject2_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject2_PatrolTimeInMin.append(minutes)
        for integer in self.subject2_PatrolTimeInMin:
            self.subject2_total += integer

        for i in self.subject3Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject3_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject3_PatrolTimeInMin.append(minutes)
        for integer in self.subject3_PatrolTimeInMin:
            self.subject3_total += integer

        for i in self.subject4Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject4_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject4_PatrolTimeInMin.append(minutes)
        for integer in self.subject4_PatrolTimeInMin:
            self.subject4_total += integer

        for i in self.subject5Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject5_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject5_PatrolTimeInMin.append(minutes)
        for integer in self.subject5_PatrolTimeInMin:
            self.subject5_total += integer

        for i in self.subject6Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject6_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject6_PatrolTimeInMin.append(minutes)
        for integer in self.subject6_PatrolTimeInMin:
            self.subject6_total += integer

        for i in self.subject7Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject7_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject7_PatrolTimeInMin.append(minutes)
        for integer in self.subject7_PatrolTimeInMin:
            self.subject7_total += integer

        for i in self.subject8Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject8_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject8_PatrolTimeInMin.append(minutes)
        for integer in self.subject8_PatrolTimeInMin:
            self.subject8_total += integer

        for i in self.subject9Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject9_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject9_PatrolTimeInMin.append(minutes)
        for integer in self.subject9_PatrolTimeInMin:
            self.subject9_total += integer

        for i in self.subject10Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject10_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject10_PatrolTimeInMin.append(minutes)
        for integer in self.subject10_PatrolTimeInMin:
            self.subject10_total += integer

        for i in self.subject11Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject11_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject11_PatrolTimeInMin.append(minutes)
        for integer in self.subject11_PatrolTimeInMin:
            self.subject11_total += integer

        for i in self.subject12Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject12_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject12_PatrolTimeInMin.append(minutes)
        for integer in self.subject12_PatrolTimeInMin:
            self.subject12_total += integer

        for i in self.subject13Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject13_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject13_PatrolTimeInMin.append(minutes)
        for integer in self.subject13_PatrolTimeInMin:
            self.subject13_total += integer

        for i in self.subject14Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject14_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject14_PatrolTimeInMin.append(minutes)
        for integer in self.subject14_PatrolTimeInMin:
            self.subject14_total += integer

        for i in self.subject15Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject15_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject15_PatrolTimeInMin.append(minutes)
        for integer in self.subject15_PatrolTimeInMin:
            self.subject15_total += integer

        for i in self.subject16Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject16_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject16_PatrolTimeInMin.append(minutes)
        for integer in self.subject16_PatrolTimeInMin:
            self.subject16_total += integer

        for i in self.subject17Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject17_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject17_PatrolTimeInMin.append(minutes)
        for integer in self.subject17_PatrolTimeInMin:
            self.subject17_total += integer

        for i in self.subject18Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject18_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject18_PatrolTimeInMin.append(minutes)
        for integer in self.subject18_PatrolTimeInMin:
            self.subject18_total += integer

        for i in self.subject19Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject19_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject19_PatrolTimeInMin.append(minutes)
        for integer in self.subject19_PatrolTimeInMin:
            self.subject19_total += integer

        for i in self.subject20Time:
            if re.findall("[0-9]+(h)", i) == ["h"]:
                convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
                convertHoursToMin = convertHoursToMin * 60
                self.subject20_PatrolTimeInMin.append(convertHoursToMin)
            else:
                minutes = int(re.findall("([0-9]+)m", i)[0])
                self.subject20_PatrolTimeInMin.append(minutes)
        for integer in self.subject20_PatrolTimeInMin:
            self.subject20_total += integer
        # -------------------------------------

    def postResults(self):
        with open('results.txt', 'w+') as file:
            # -------------List of CMs-------------
            file.write(f"{self.extractedCMs[0]}: {self.subject1_total} minutes.\n")
            file.write(f"{self.extractedCMs[1]}: {self.subject2_total} minutes.\n")
            file.write(f"{self.extractedCMs[2]}: {self.subject3_total} minutes.\n")
            file.write(f"{self.extractedCMs[3]}: {self.subject4_total} minutes.\n")
            file.write(f"{self.extractedCMs[4]}: {self.subject5_total} minutes.\n")
            file.write(f"{self.extractedCMs[5]}: {self.subject6_total} minutes.\n")
            file.write(f"{self.extractedCMs[6]}: {self.subject7_total} minutes.\n")
            file.write(f"{self.extractedCMs[7]}: {self.subject8_total} minutes.\n")
            file.write(f"{self.extractedCMs[8]}: {self.subject9_total} minutes.\n")
            file.write(f"{self.extractedCMs[9]}: {self.subject10_total} minutes.\n")
            file.write(f"{self.extractedCMs[10]}: {self.subject11_total} minutes.\n")
            file.write(f"{self.extractedCMs[11]}: {self.subject12_total} minutes.\n")
            file.write(f"{self.extractedCMs[12]}: {self.subject13_total} minutes.\n")
            file.write(f"{self.extractedCMs[13]}: {self.subject14_total} minutes.\n")
            file.write(f"{self.extractedCMs[14]}: {self.subject15_total} minutes.\n")
            file.write(f"{self.extractedCMs[15]}: {self.subject16_total} minutes.\n")
            file.write(f"{self.extractedCMs[16]}: {self.subject17_total} minutes.\n")
            file.write(f"{self.extractedCMs[17]}: {self.subject18_total} minutes.\n")
            file.write(f"{self.extractedCMs[18]}: {self.subject19_total} minutes.\n")
            file.write(f"{self.extractedCMs[19]}: {self.subject20_total} minutes.\n")
            # -------------------------------------

    def switchButtonState(self):
        if (self.btn['state'] == NORMAL):
            self.btn.config(state=DISABLED)
        else:
            self.btn.config(state=DISABLED)

    def run(self):
        if __name__ == "__main__":
            try:
                self.output.delete('1.0', END)
                self.getTime()
                self.caculateTime()
                self.postResults()
                self.output.insert(INSERT, "Finished! See results.txt")
                self.switchButtonState()
            except:
                self.output.delete('1.0', END)
                self.output.insert(INSERT, "Error.")

window = Tk()
SampleGUI(window)
window.mainloop()