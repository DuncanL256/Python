from tkinter import *
import datetime
import math

import time

#variable initialization
hoursOfSleep = 0
minutesOfSleep = 0
#avgSleeptime = 0
userAge = 0


window = Tk()
window.title("Nap App") #app name
window.geometry('360x640')
window.configure(bg="#5182BA") #sets background color

applbl = Label(window, text="Nap App", font=("Arial Bold", 50), bg="#5182BA", fg="#2E3033") #header
applbl.place(x=40, y=30)

#functions for inputs 
def recordHour():
    hoursOfSleep = wake.get()
    print(hoursOfSleep)

def recordMinute():
    minutesOfSleep = wake2.get()
    print(minutesOfSleep)

def recordSleepTime():
    #avgSleeptime = sleepTime.get()
    print(avgSleeptime)

def recordAge(ageNumber):
    userAge = ageNumber
    #print(ageNumber)
    #print(userAge)

wake = Spinbox(window, from_=0, to=12, font=("Arial Bold", 16), bg="#2E3033", fg="#B5B6BA", command=recordHour) #hours
wake.place(x=100, y=120, width=45, height=40)
wake2 = Spinbox(window, from_=0, to=59, font=("Arial Bold", 16) , bg="#2E3033", fg="#B5B6BA", command= recordMinute) #minutes
wake2.place(x=150, y=120, width=45, height=40)
wake3 = Checkbutton(window, text='AM', bg="#5182BA") #Am
wake3.place(x=200, y=120)
wake4 = Checkbutton(window, text='PM', bg="#5182BA") #Pm
wake4.place(x=200, y=140)

#sleepTimelbl = Label(window, text="How long do you sleep?", font=("Arial Bold", 12), bg="#5182BA", fg="#2E3033") #sleep time header
#sleepTimelbl.place(x=85, y=175)
#sleepTime = Scale(window, from_=0, to=10, orient='horizontal', bg="#2E3033", fg="white", command= recordSleepTime) #time the user typically sleeps
#sleepTime.place(x=80, y=200, width=200)
#sleepTimelbl2 = Label(window, text="Hours", font=("Arial Bold", 10), bg="#5182BA", fg="#2E3033") 
#sleepTimelbl2.place(x=280, y=220)

agelbl = Label(window, text="How old are you?", font=("Arial Bold", 12), bg="#5182BA", fg="#2E3033") #age header
agelbl.place(x=110, y=175)
age = Scale(window, from_=12, to=100, orient='horizontal', bg="#2E3033", fg="white", command= recordAge) #age of the uiser
age.place(x=80, y=200, width=200)

sleepHeader = Label(window, text="Optimal Sleep:", font=("Arial Bold", 14), bg="#5182BA", fg="#2E3033") #age header

def convertTime(time24h): #converts to 12 hour time
    time_obj = datetime.datetime.strptime(time24h, "%H:%M")
    return time_obj.strftime("%I:%M %p")

def calculateSleep():
    print("calculating")

    userAgeInt = int(age.get())
    hoursOfSleep = int(wake.get())
    minutesOfSleep = int(wake2.get())

    recomendedSleep = 0 #recomended sleep numbers for 3 age groups 
    if userAgeInt < 18:
        recomendedSleep = 37800 #10.5 hours to seconds (7 sleep cycles)
    elif 17 < userAgeInt < 65:
        recomendedSleep = 32400 #9 hours to seconds (6 sleep cycles)
    elif 64 < userAgeInt:
        recomendedSleep = 27000 #7.5 hours to seconds (5 sleep cycles)
    

    userWakeUp = (hoursOfSleep*3600) + (minutesOfSleep*60) #converts user wake up time to seconds
    optimalSleep = userWakeUp - recomendedSleep #calculate best sleep time in seconds
    reConHours = math.trunc(float(optimalSleep) / 3600)
    hoursRemainder = optimalSleep % 3600
    reConMinutes = -abs(hoursRemainder // 60)

    if reConHours < 0: #allows for time to roll over into  the previous day
        reConHours = 24 + reConHours

    print(reConHours)
    print(reConMinutes)

    if reConMinutes == 0:
        displayTime = str(reConHours) + ":00"
    elif reConMinutes == -30:
        reConHours = reConHours -1
        if reConHours < 0: #allows for time to roll over into  the previous day
            reConHours = 24 + reConHours
        displayTime = str(reConHours) + ":30"
    else:
        reConHours = reConHours -1
        if reConHours < 0: #allows for time to roll over into  the previous day
            reConHours = 24 + reConHours
        reConMinutes = abs(reConMinutes)
        reConMinutes = str(reConMinutes)
        displayTime = str(reConHours) + ":" + reConMinutes
    
    print("display time: " + displayTime)
    time12h = convertTime(displayTime)
    print(time12h)


    sleepHeader.place(x=110, y=320) #places the formerly invisible sleep header
    wakeTime = Label(window, text=time12h, font=("Arial Bold", 22), bg="#5182BA", fg="#2E3033") #shows the optimal time to go to sleep
    wakeTime.place(x=115, y=355) 




calculate = Button(window, text="Calculate", font=("Arial Bold", 12), bg="#2E3033", fg="white", command=calculateSleep)
calculate.place(x=130, y=260, width=100, height=45)

window.mainloop()