import calendar
from Tkinter import *
root = Tk()
root.title("West Point Calendar")
root.geometry('600x510')
def click(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

#Welcome Screen
#/Welcome Screen

#Calendar
year = 2017
month = 1
str1 = calendar.month(year, month)
cally=[['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0'],['0','0','0','0','0','0','0']]
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
