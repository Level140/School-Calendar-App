import calendar
from Tkinter import *
root = Tk()
root.title("West Point Calendar")
root.geometry('550x800')
cally=[['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0']]
dayOnes=[]
dayTwos=[]
day=1
cal=StringVar()
month=IntVar()
year=IntVar()
year.set(2017)
month.set(1)


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
B = Button(root, text ="<-", font=('courier', 15, 'bold'),command = lastMonth)
B.pack(anchor=E)
F = Button(root, text ="->", font=('courier', 15, 'bold'),command = nextMonth)
F.pack(anchor=E)
label1 = Label(root, textvariable=cal, justify=LEFT, font=('courier', 30, 'bold'), bg='Blue')
label1.pack(anchor=W,pady=5)

#/Calendar

#Right Side Widgets


#############
# To get selected day, variable is selectedDay
# To get selected date, variable is dateNumText
# To get selected lesson number, variable is lessonNumText


############

userInputFrame = Frame(root)
userInputFrame.pack(side = LEFT)

daySelectFrame = Frame(userInputFrame)
daySelectFrame.pack()

lessonSelectFrame = Frame(userInputFrame)
lessonSelectFrame.pack()



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

dateNumText = StringVar()


inputDateLabel = Label(userInputFrame, text = "Click a date on the calendar above", justify = LEFT)
dateEntry = Label(userInputFrame, width = 30, text = dateNumText)

inputDateLabel.pack()
dateEntry.pack()



#############CSV



def genCSV():
    csvFile = open("CSV.txt","r")
    currCSV = csvFile.read()
    csvFile.close()

    csvFile = open("CSV.txt","w")
    currCSV += ("," + str(selectedDay.get()) + "," + str(dateNumText.get()) + "," + str(lessonNumText.get()))
    csvFile.write(currCSV)
    csvFile.close()

    #http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
    #http://effbot.org/tkinterbook/variable.htm
    #https://www.techwalla.com/articles/how-to-convert-int-to-string-in-python




csvButton = Button(userInputFrame, text="Add to CSV", command=(lambda:genCSV()))
csvButton.pack()







##############









#/Right Side Widgets

def click(event):
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
        dayOnes.append(str(month.get())+"/"+str(cally[ro][co])+"/"+str(year.get()))
    if(selectedDay.get()==2):
        dayTwos.append(str(month.get())+"/"+str(cally[ro][co])+"/"+str(year.get()))
    createMonth(month.get(),year.get())

    dateNumText.set((str(month.get())+"/"+str(cally[ro][co])+"/"+str(year.get())))




label1.bind("<Button-1>", click)

root.mainloop()
