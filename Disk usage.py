import psutil
from tkinter import *

wn = Tk()
wn.geometry('600x400')
def check():
    space_left = psutil.disk_usage('/')
    print(space_left)
    button.pack_forget()
    label = Label(wn, text='total space: ' +str(round(space_left.total / 2**30, 1))+ ' GB\nused space: '+str(round(space_left.used / 2**30, 1))+ ' GB\nfree space: ' +str(round(space_left.free / 2**30, 1)) + ' GB\npercent: '+str(round(space_left.percent / 2**30, 1)) ,font=('comic sans',25))
    label.pack()

button = Button(wn,text='Check Space',font=('Arial',20),command=check)
button.pack()

wn.mainloop()
