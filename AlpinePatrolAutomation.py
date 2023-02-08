# "List of CMs" is important. Must be updated if one decides to leave or a new CM joins.

import re

# -------------List of CMs-------------
dude08_PatrolTimeInMin = []
dude08Time = []
dude08_total = 0
adidazboy_PatrolTimeInMin = []
adidazboyTime = []
adidazboy_total = 0
boring_PatrolTimeInMin = []
boringTime = []
boring_total = 0
rosegirl_PatrolTimeInMin = []
rosegirlTime = []
rosegirl_total = 0
# -------------------------------------

def GetTime():
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
                            dude08Time.append(k)
                        patrolTime = []
                    elif cm == "AdidazBoy123":
                        for k in patrolTime:
                            adidazboyTime.append(k)
                        patrolTime = []
                    elif cm == "boringpjtx":
                        for k in patrolTime:
                            boringTime.append(k)
                        patrolTime = []
                    elif cm == "rosegirlye":
                        for k in patrolTime:
                            rosegirlTime.append(k)
                        patrolTime = []
                    # -------------------------------------
                else:
                    continue

def CaculateTime():
    global dude08_total, adidazboy_total, boring_total, rosegirl_total # List of CMs
    # -------------List of CMs-------------
    for i in dude08Time:
        if re.findall("[0-9]+(h)", i) == ["h"]:
            convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
            convertHoursToMin = convertHoursToMin * 60
            dude08_PatrolTimeInMin.append(convertHoursToMin)
        else:
            minutes = int(re.findall("([0-9]+)m", i)[0])
            dude08_PatrolTimeInMin.append(minutes)
    for integer in dude08_PatrolTimeInMin:
        dude08_total += integer

    for i in adidazboyTime:
        if re.findall("[0-9]+(h)", i) == ["h"]:
            convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
            convertHoursToMin = convertHoursToMin * 60
            adidazboy_PatrolTimeInMin.append(convertHoursToMin)
        else:
            minutes = int(re.findall("([0-9]+)m", i)[0])
            adidazboy_PatrolTimeInMin.append(minutes)
    for integer in adidazboy_PatrolTimeInMin:
        adidazboy_total += integer

    for i in boringTime:
        if re.findall("[0-9]+(h)", i) == ["h"]:
            convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
            convertHoursToMin = convertHoursToMin * 60
            boring_PatrolTimeInMin.append(convertHoursToMin)
        else:
            minutes = int(re.findall("([0-9]+)m", i)[0])
            boring_PatrolTimeInMin.append(minutes)
    for integer in boring_PatrolTimeInMin:
        boring_total += integer

    for i in rosegirlTime:
        if re.findall("[0-9]+(h)", i) == ["h"]:
            convertHoursToMin = int(re.findall("([0-9]+)h", i)[0])
            convertHoursToMin = convertHoursToMin * 60
            rosegirl_PatrolTimeInMin.append(convertHoursToMin)
        else:
            minutes = int(re.findall("([0-9]+)m", i)[0])
            rosegirl_PatrolTimeInMin.append(minutes)
    for integer in rosegirl_PatrolTimeInMin:
        rosegirl_total += integer
    # -------------------------------------

def PostResults():
    with open('results.txt', 'w+') as file:
        # -------------List of CMs-------------
        file.write(f"Dude080721: {dude08_total} minutes.\n")
        file.write(f"AdidazBoy123: {adidazboy_total} minutes.\n")
        file.write(f"boringpjtx: {boring_total} minutes.\n")
        file.write(f"rosegirlye: {rosegirl_total} minutes.\n")
        # -------------------------------------

if __name__ == "__main__":
    GetTime()
    CaculateTime()
    PostResults()