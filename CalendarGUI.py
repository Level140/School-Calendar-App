
import calendar
from Tkinter import *
root = Tk()
root.title("West Point Calendar")
root.geometry('600x800')
cally=[['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0']]
dayOnes=[]
dayTwos=[]
day=1
cal=StringVar()
month=IntVar()
year=IntVar()
year.set(2017)
month.set(1)

dateNumText = StringVar()


def createMonth(mn,yr):
    str1 = calendar.month(yr, mn)

    work=str1.split('\n')
    nextWeek=0
    #Get a grid of the calendar
    for y in range(0,6):
        for x in range(0,len(work[y+2])):
            if(work[y+2][x]==' '):
                pass
            else:
                if(work[y+2][x]=='0'):
                    nextWeek+=1

                if(nextWeek>0):
                    cally[y][x/3]=str(nextWeek)+work[y+2][x]
                else:
                    cally[y][x/3]=work[y+2][x]
    str1=str1.replace("\n","\n ")
    for x in dayOnes:
        a=x.split('/')
        if(str(yr)==a[2] and str(mn)==a[0]):
            str1=str1.replace(" "+a[1]+" ","*"+a[1]+" ",1)
            str1=str1.replace(" "+a[1]+"\n","*"+a[1]+"\n",1)
            str1=str1.replace(" "+a[1]+"*","*"+a[1]+"*",1)
            str1=str1.replace(" "+a[1]+"/","*"+a[1]+"/",1)
    for x in dayTwos:
        a=x.split('/')
        if(str(yr)==a[2] and str(mn)==a[0]):
            str1=str1.replace(" "+a[1]+" ","/"+a[1]+" ",1)
            str1=str1.replace(" "+a[1]+"\n","/"+a[1]+"\n",1)
            str1=str1.replace(" "+a[1]+"*","/"+a[1]+"*",1)
            str1=str1.replace(" "+a[1]+"/","/"+a[1]+"/",1)
    cal.set(str1)

def nextMonth():
    if(month.get()==12):
        month.set(1)
        year.set(year.get()+1)
    month.set(month.get()+1)
    createMonth(month.get(),year.get())
def lastMonth():
    if(month.get()==1):
        month.set(12)
        year.set(year.get()-1)
    month.set(month.get()-1)
    createMonth(month.get(),year.get())
#Welcome Screen
#/Welcome Screen

#Calendar
createMonth(month.get(),year.get())
#/Get a grid of the calendar
but_frame = Frame(root)
label1 = Label(root, textvariable=cal, justify=LEFT, font=('courier', 30, 'bold'), bg='Blue')
label1.pack(anchor=W,pady=0)
B = Button(but_frame, text ="<-", font=('courier', 25, 'bold'),command = lastMonth)
B.pack(side=LEFT)
F = Button(but_frame, text ="->", font=('courier', 25, 'bold'),command = nextMonth)
F.pack(side=LEFT)
but_frame.pack(anchor=W)
userInputFrame = Frame(but_frame)
userInputFrame.pack(side = LEFT)

daySelectFrame = Frame(userInputFrame)
daySelectFrame.pack()

lessonSelectFrame = Frame(userInputFrame)
lessonSelectFrame.pack()


#/Calendar

#Right Side Widgets

bigFrame=Frame(root)
classFrame = Frame(bigFrame)
classFrame.pack(side=LEFT,padx=10)
classFrame2 = Frame(bigFrame)
classFrame2.pack(side=RIGHT,padx=10)
bigFrame.pack(side=LEFT)

topLessonLabel = Label(classFrame, text = "Enter your class periods below", justify = LEFT)
topLessonLabel.pack()

aClass = StringVar()
aLessonLabel = Label(classFrame, text = "A Period", justify = LEFT)
aEntryBox = Entry(classFrame, width = 30, textvariable = aClass)
aLessonLabel.pack()
aEntryBox.pack()

bClass = StringVar()
bLessonLabel = Label(classFrame, text = "B Period", justify = LEFT)
bEntryBox = Entry(classFrame, width = 30, textvariable = bClass)
bLessonLabel.pack()
bEntryBox.pack()

cClass = StringVar()
cLessonLabel = Label(classFrame, text = "C Period", justify = LEFT)
cEntryBox = Entry(classFrame, width = 30, textvariable = cClass)
cLessonLabel.pack()
cEntryBox.pack()

dClass = StringVar()
dLessonLabel = Label(classFrame, text = "D Period", justify = LEFT)
dEntryBox = Entry(classFrame, width = 30, textvariable = dClass)
dLessonLabel.pack()
dEntryBox.pack()

eClass = StringVar()
eLessonLabel = Label(classFrame, text = "E Period", justify = LEFT)
eEntryBox = Entry(classFrame, width = 30, textvariable = eClass)
eLessonLabel.pack()
eEntryBox.pack()

fClass = StringVar()
fLessonLabel = Label(classFrame, text = "F Period", justify = LEFT)
fEntryBox = Entry(classFrame, width = 30, textvariable = fClass)
fLessonLabel.pack()
fEntryBox.pack()

gClass = StringVar()
gLessonLabel = Label(classFrame2, text = "G Period", justify = LEFT)
gEntryBox = Entry(classFrame2, width = 30, textvariable = gClass)
gLessonLabel.pack()
gEntryBox.pack()

hClass = StringVar()
hLessonLabel = Label(classFrame2, text = "H Period", justify = LEFT)
hEntryBox = Entry(classFrame2, width = 30, textvariable = hClass)
hLessonLabel.pack()
hEntryBox.pack()

iClass = StringVar()
iLessonLabel = Label(classFrame2, text = "I Period", justify = LEFT)
iEntryBox = Entry(classFrame2, width = 30, textvariable = iClass)
iLessonLabel.pack()
iEntryBox.pack()

jClass = StringVar()
jLessonLabel = Label(classFrame2, text = "J Period", justify = LEFT)
jEntryBox = Entry(classFrame2, width = 30, textvariable = jClass)
jLessonLabel.pack()
jEntryBox.pack()

kClass = StringVar()
kLessonLabel = Label(classFrame2, text = "K Period", justify = LEFT)
kEntryBox = Entry(classFrame2, width = 30, textvariable = kClass)
kLessonLabel.pack()
kEntryBox.pack()

lClass = StringVar()
lLessonLabel = Label(classFrame2, text = "L Period", justify = LEFT)
lEntryBox = Entry(classFrame2, width = 30, textvariable = lClass)
lLessonLabel.pack()
lEntryBox.pack()
#############
# To get selected day, variable is selectedDay
# To get selected date, variable is dateNumText
# To get selected lesson number, variable is lessonNumText


############





lessonNumText = StringVar()
inputLessonLabel = Label(userInputFrame, text = "Input the lesson number", justify = LEFT)
entryBox = Entry(userInputFrame, width = 30, textvariable = lessonNumText)
entryBox.insert(END, "0")
inputLessonLabel.pack()
entryBox.pack()

##########################
#Day 1/2 radio buttons
##########################
Label(daySelectFrame, text = "Select Day:", justify = LEFT, bg = "White").pack()

selectedDay = IntVar()

Radiobutton(daySelectFrame,
	text="Day 1",
	padx = 20,
	variable=selectedDay,
	value=1,justify = LEFT).pack(anchor=W)

Radiobutton(daySelectFrame,
	text="Day 2",
	padx = 20,
	variable=selectedDay,
	value=2,justify = LEFT).pack(anchor=W)


inputDateLabel = Label(userInputFrame, text = "Click a date on the calendar above", justify = LEFT)
dateNumText.set("No Date Selected")
dateEntry = Label(userInputFrame, width = 30, textvariable = dateNumText)

inputDateLabel.pack()
dateEntry.pack()


#############Classes



#############CSV



def genCSV():
    #csvFile = open("CSV.txt","r")
    #currCSV = csvFile.read()
    #csvFile.close()
    currCSV=""

    currCSV+="Subject,Start Date,Start Time,End Date,End Time"
    for x in dayOnes:
        a=x.split("/")
        currCSV += "\nDay 1 Lesson "+str(a[3])+","+a[0]+"/"+a[1]+"/"+a[2]+",7:00 AM,"+a[0]+"/"+a[1]+"/"+a[2]+",7:00 AM"
        if(aClass.get() is not ""):
            currCSV += "\n"+aClass.get()+","+a[0]+"/"+a[1]+"/"+a[2]+",7:30 AM,"+a[0]+"/"+a[1]+"/"+a[2]+",8:25 AM"
        if(bClass.get() is not ""):
            currCSV += "\n"+bClass.get()+","+a[0]+"/"+a[1]+"/"+a[2]+",8:40 AM,"+a[0]+"/"+a[1]+"/"+a[2]+",9:35 AM"
        if(cClass.get() is not ""):
            currCSV += "\n"+cClass.get()+","+a[0]+"/"+a[1]+"/"+a[2]+",9:50 AM,"+a[0]+"/"+a[1]+"/"+a[2]+",10:45 AM"
        if(dClass.get() is not ""):
            currCSV += "\n"+dClass.get()+","+a[0]+"/"+a[1]+"/"+a[2]+",11:00 AM,"+a[0]+"/"+a[1]+"/"+a[2]+",11:55 AM"
        if(eClass.get() is not ""):
            currCSV += "\n"+eClass.get()+","+a[0]+"/"+a[1]+"/"+a[2]+",1:55 PM,"+a[0]+"/"+a[1]+"/"+a[2]+",2:50 PM"
        if(fClass.get() is not ""):
            currCSV += "\n"+fClass.get()+","+a[0]+"/"+a[1]+"/"+a[2]+",3:05 PM,"+a[0]+"/"+a[1]+"/"+a[2]+",4:00 PM"
    for x in dayTwos:
        a=x.split("/")
        currCSV += "\nDay 2 Lesson "+str(a[3])+","+a[0]+"/"+a[1]+"/"+a[2]+",7:00 AM,"+a[0]+"/"+a[1]+"/"+a[2]+",7:00 AM"
        if(gClass.get() is not ""):
            currCSV += "\n"+gClass.get()+","+a[0]+"/"+a[1]+"/"+a[2]+",7:30 AM,"+a[0]+"/"+a[1]+"/"+a[2]+",8:25 AM"
        if(hClass.get() is not ""):
            currCSV += "\n"+hClass.get()+","+a[0]+"/"+a[1]+"/"+a[2]+",8:40 AM,"+a[0]+"/"+a[1]+"/"+a[2]+",9:35 AM"
        if(iClass.get() is not ""):
            currCSV += "\n"+iClass.get()+","+a[0]+"/"+a[1]+"/"+a[2]+",9:50 AM,"+a[0]+"/"+a[1]+"/"+a[2]+",10:45 AM"
        if(jClass.get() is not ""):
            currCSV += "\n"+jClass.get()+","+a[0]+"/"+a[1]+"/"+a[2]+",11:00 AM,"+a[0]+"/"+a[1]+"/"+a[2]+",11:55 AM"
        if(kClass.get() is not ""):
            currCSV += "\n"+kClass.get()+","+a[0]+"/"+a[1]+"/"+a[2]+",1:55 PM,"+a[0]+"/"+a[1]+"/"+a[2]+",2:50 PM"
        if(lClass.get() is not ""):
            currCSV += "\n"+lClass.get()+","+a[0]+"/"+a[1]+"/"+a[2]+",3:05 PM,"+a[0]+"/"+a[1]+"/"+a[2]+",4:00 PM"

    csvFile = open("CSV.txt","w")
    csvFile.write(currCSV)
    csvFile.close()

    #http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
    #http://effbot.org/tkinterbook/variable.htm
    #https://www.techwalla.com/articles/how-to-convert-int-to-string-in-python




csvButton = Button(root, text="Create CSV", font=('courier', 20, 'bold'), command=(lambda:genCSV()))
csvButton.pack(anchor=E)







##############









#/Right Side Widgets

dayNumIncrease= False


def click(event):
    global dayNumIncrease
    #http://stackoverflow.com/questions/11904981/local-variable-referenced-before-assignment
    co=0
    ro=0
    x, y = event.x, event.y
    if(x>0 and x<70):
        co=0
    if(x>70 and x<140):
        co=1
    if(x>140 and x<210):
        co=2
    if(x>210 and x<280):
        co=3
    if(x>280 and x<350):
        co=4
    if(x>350 and x<420):
        co=5
    if(x>420 and x<490):
        co=6
    if(y>80 and y<130):
        ro=0
    if(y>130 and y<180):
        ro=1
    if(y>180 and y<230):
        ro=2
    if(y>230 and y<280):
        ro=3
    if(y>280 and y<330):
        ro=4
    if(y>330 and y<380):
        ro=5
    dateEntry.configure(text=str(month.get())+"/"+str(cally[ro][co])+"/"+str(year.get()))


    if(selectedDay.get()==1):
        dayOnes.append(str(month.get())+"/"+str(cally[ro][co])+"/"+str(year.get())+"/"+str(lessonNumText.get()))
        selectedDay.set(2)

    elif(selectedDay.get()==2):
        dayTwos.append(str(month.get())+"/"+str(cally[ro][co])+"/"+str(year.get())+"/"+str(lessonNumText.get()))
        selectedDay.set(1)

    if (dayNumIncrease):
        lessonNumText.set(int(lessonNumText.get())+1)
    dayNumIncrease = not dayNumIncrease
    createMonth(month.get(),year.get())

    dateNumText.set((str(month.get())+"/"+str(cally[ro][co])+"/"+str(year.get())))




label1.bind("<Button-1>", click)

root.mainloop()
