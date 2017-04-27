import calendar
from Tkinter import *
root = Tk()
root.title("West Point Calendar")
root.geometry('600x510')
cally=[['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0']]

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
    print cally[ro][co]
    #print('{}, {}'.format(x, y))

#Welcome Screen
#/Welcome Screen

#Calendar
year = 2017
month = 1
str1 = calendar.month(year, month)
work=str1.split('\n')
print work
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
#/Get a grid of the calendar

for x in cally:
    print x
label1 = Label(root, text=str1, justify=LEFT, font=('courier', 30, 'bold'), bg='Blue')
label1.pack(anchor=W,pady=50)
#/Calendar

label1.bind("<Button-1>", click)

root.mainloop()
