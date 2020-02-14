from tkinter import Label, Entry, Tk, Button, END
from PIL import ImageTk,Image

root = Tk()
root.title("GPA Calculator")
root.resizable(0, 0)
root.geometry("800x400")
root.iconbitmap(r'D:\Programs\Python\GUI\GPA_CALC\gcuf.ico')

def new_window():
    about = Tk()
    about.title("GPA Calculator")
    about.resizable(0, 0)
    about.geometry("130x180")
    about.iconbitmap(r'D:\Programs\Python\GUI\GPA_CALC\gcuf.ico')
    developedby = Label(about, text = "     Developed by!", font = ('Calibri', 11, 'bold'))
    developedby.grid(column = 0, row = 0)
    aboutus = Label(about, text = "\n      M. Zuraiz Zafar\n    and\n     Abdullah", font = ('Calibri', 11))
    aboutus.grid(column = 0, row = 1)
    inst = Label(about, text = "\n   ADP CS\n   UCC, GCUF.", font = ('Calibri',14,'bold'))
    inst.grid(column = 0, row = 2)

warning = Label(root, text="Disabled Text Boxes are reserved \nfor Calculation", bg ='Red')
warning.place(x=600,y=10)

mainlabel = Label(root, text = "GPA Calculator", font = ('Helvetica', 32, 'bold'))
mainlabel.place(x=255,y=0)

subjec = Label(root, text = "Subject Name", font = ('Helvetica', 11, 'bold', 'underline'))
subjec.place(x=27,y=55)

optionalLabel = Label(root, text = "(Optional)")
optionalLabel.place(x=130,y=58)

chour = Label(root, text = "Credit Hour", font = ('Helvetica', 11, 'bold', 'underline'))
chour.place(x=225,y=55)

esteric = Label(root, text = "*")
#esteric.place(x=312,y=55)

esteric1 = Label(root, text = " ** ")
#esteric1.place(x=400,y=55)

tnumber = Label(root, text = "Total Number", font = ('Helvetica', 11, 'bold', 'underline'))
tnumber.place(x=330,y=55)

onumber = Label(root, text = "Obtained Number", font = ('Helvetica', 11, 'bold', 'underline'))
onumber.place(x=445,y=55)

perc = Label(root, text = "Percentage", font = ('Helvetica', 11, 'bold', 'underline'))
perc.place(x=590,y=55)

qpoint = Label(root, text = "Quality Points", font = ('Helvetica', 11, 'bold', 'underline'))
qpoint.place(x=690,y=55)

about = Button(root, text = "About Us!", command=new_window)
about.place(x=1,y=1)

entry1 = Entry(root, width = 30)
entry1.place(x=30,y=90)

entrya1 = Entry(root, width = 15)
entrya1.place(x=225,y=90)


entryb1 = Entry(root, width = 17, bg = 'Pink')
entryb1.place(x=330,y=90)

entryc1 = Entry(root, width = 22)
entryc1.place(x=445,y=90)

entryd1 = Entry(root, width = 15, bg = 'Pink')
entryd1.place(x=590,y=90)

entryf1 = Entry(root, width = 16, bg = 'Pink')
entryf1.place(x=692,y=90)

entry2 = Entry(root, width = 30)
entry2.place(x=30,y=120)

entrya2 = Entry(root, width = 15)
entrya2.place(x=225,y=120)

entryb2 = Entry(root, width = 17, bg = 'Pink')
entryb2.place(x=330,y=120)

entryc2 = Entry(root, width = 22)
entryc2.place(x=445,y=120)

entryd2 = Entry(root, width = 15, bg = 'Pink')
entryd2.place(x=590,y=120)

entryf2 = Entry(root, width = 16, bg = 'Pink')
entryf2.place(x=692,y=120)

entry3 = Entry(root, width = 30)
entry3.place(x=30,y=150)

entrya3 = Entry(root, width = 15)
entrya3.place(x=225,y=150)

entryb3 = Entry(root, width = 17, bg = 'Pink')
entryb3.place(x=330,y=150)

entryc3 = Entry(root, width = 22)
entryc3.place(x=445,y=150)

entryd3 = Entry(root, width = 15, bg = 'Pink')
entryd3.place(x=590,y=150)

entryf3 = Entry(root, width = 16, bg = 'Pink')
entryf3.place(x=692,y=150)

entry4 = Entry(root, width = 30)
entry4.place(x=30,y=180)

entrya4 = Entry(root, width = 15)
entrya4.place(x=225,y=180)

entryb4 = Entry(root, width = 17, bg = 'Pink')
entryb4.place(x=330,y=180)

entryc4 = Entry(root, width = 22)
entryc4.place(x=445,y=180)

entryd4 = Entry(root, width = 15, bg = 'Pink')
entryd4.place(x=590,y=180)

entryf4 = Entry(root, width = 16, bg = 'Pink')
entryf4.place(x=692,y=180)

entry5 = Entry(root, width = 30)
entry5.place(x=30,y=210)

entrya5 = Entry(root, width = 15)
entrya5.place(x=225,y=210)

entryb5 = Entry(root, width = 17, bg = 'Pink')
entryb5.place(x=330,y=210)

entryc5 = Entry(root, width = 22)
entryc5.place(x=445,y=210)

entryd5 = Entry(root, width = 15, bg = 'Pink')
entryd5.place(x=590,y=210)

entryf5 = Entry(root, width = 16, bg = 'Pink')
entryf5.place(x=694,y=210)

entry6 = Entry(root, width = 30)
entry6.place(x=30,y=240)

entrya6 = Entry(root, width = 15)
entrya6.place(x=225,y=240)

entryb6 = Entry(root, width = 17, bg = 'Pink')
entryb6.place(x=330,y=240)

entryc6 = Entry(root, width = 22)
entryc6.place(x=445,y=240)

entryd6 = Entry(root, width = 15, bg = 'Pink')
entryd6.place(x=590,y=240)

entryf6 = Entry(root, width = 16, bg = 'Pink')
entryf6.place(x=694,y=240)


ser1 = Label(text="1. ")
ser1.place(x=8, y=90)

ser2 = Label(text="2. ")
ser2.place(x=8, y=120)

ser3 = Label(text="3. ")
ser3.place(x=8, y=150)

ser4 = Label(text="4. ")
ser4.place(x=8, y=180)

ser5 = Label(text="5. ")
ser5.place(x=8, y=210)

ser6 = Label(text="6. ")
ser6.place(x=8, y=240)

def disableentry():
    entryb1.configure(state = 'disable')
    entryb2.configure(state = 'disable')
    entryb3.configure(state = 'disable')
    entryb4.configure(state = 'disable')
    entryb5.configure(state = 'disable')
    entryb6.configure(state = 'disable')

    entryd1.configure(state = 'disable')
    entryd2.configure(state = 'disable')
    entryd3.configure(state = 'disable')
    entryd4.configure(state = 'disable')
    entryd5.configure(state = 'disable')
    entryd6.configure(state = 'disable')

    entryf1.configure(state = 'disable')
    entryf2.configure(state = 'disable')
    entryf3.configure(state = 'disable')
    entryf4.configure(state = 'disable')
    entryf5.configure(state = 'disable')
    entryf6.configure(state = 'disable')

disableentry()

def enablentry():
    entryb1.configure(state = 'normal')
    entryb2.configure(state = 'normal')
    entryb3.configure(state = 'normal')
    entryb4.configure(state = 'normal')
    entryb5.configure(state = 'normal')
    entryb6.configure(state = 'normal')

    entryd1.configure(state = 'normal')
    entryd2.configure(state = 'normal')
    entryd3.configure(state = 'normal')
    entryd4.configure(state = 'normal')
    entryd5.configure(state = 'normal')
    entryd6.configure(state = 'normal')

    entryf1.configure(state = 'normal')
    entryf2.configure(state = 'normal')
    entryf3.configure(state = 'normal')
    entryf4.configure(state = 'normal')
    entryf5.configure(state = 'normal')
    entryf6.configure(state = 'normal')

def CH4(marks):

    if marks >= 64:
        return 16
    elif marks == 63:
        return 15.67
    elif marks == 62:
        return 15.33
    elif marks == 61:
        return 15
    elif marks == 60:
        return 14.67
    elif marks == 59:
        return 14.33
    elif marks == 58:
        return 14
    elif marks == 57:
        return 13.67
    elif marks == 56 :
        return 13.33
    elif marks == 55 :
        return 13
    elif marks == 54:
        return 12.67
    elif marks == 53:
        return 12.33
    elif marks == 52:
        return 12
    elif marks == 51:
        return 11.67
    elif marks == 50:
        return 11.33
    elif marks == 49:
        return 11
    elif marks==48:
        return 10.67
    elif  marks==47:
        return 10.33
    elif (marks==46):
        return 10
    elif (marks ==45):
        return 9.67
    elif (marks==44):
        return 9.33
    elif (marks ==43):
        return 9
    elif (marks==42):
        return 8.67
    elif (marks ==41):
        return 8.33
    elif (marks==40):
        return 8
    elif (marks ==39):
        return 7.5
    elif (marks==38):
        return 7
    elif (marks ==37):
        return 6.5
    elif (marks==36):
        return 6
    elif (marks ==35):
        return 5.5
    elif (marks==34):
        return 5
    elif (marks ==33):
        return 4.5
    elif (marks==32):
        return 4



def CH3(marks):

    if marks>=48:
        return 12
    elif  marks==47:
        return 11.67
    elif (marks==46):
        return 11.33
    elif (marks ==45):
        return 11
    elif (marks==44):
        return 10.67
    elif (marks ==43):
        return 10.33
    elif (marks==42):
        return 10
    elif (marks ==41):
        return 9.67
    elif (marks==40):
        return 9.33
    elif (marks ==39):
        return 9
    elif (marks==38):
        return 8.67
    elif (marks ==37):
        return 8.33
    elif (marks==36):
        return 8
    elif (marks ==35):
        return 7.67
    elif (marks==34):
        return 7.33
    elif (marks ==33):
        return 7
    elif (marks==32):
        return 6.67
    elif (marks ==31):
        return 6.33
    elif (marks==30):
        return 6
    elif (marks ==29):
        return 5.5
    elif (marks==28):
        return 5
    elif (marks ==27):
        return 4.5
    elif (marks==26):
        return 4
    elif (marks ==25):
        return 3.5
    elif (marks==24):
        return 3



def CH2(marks):

    if marks >= 32:
        return 8
    elif (marks == 31):
        return 7.67
    elif (marks==30):
        return 7.33
    elif (marks ==29):
        return 7
    elif (marks==28):
        return 6.67
    elif (marks ==27):
        return 6.33
    elif (marks==26):
        return 6
    elif (marks ==25):
        return 5.67
    elif (marks==24):
        return 5.33
    elif marks == 23:
        return 5
    elif marks == 22:
        return 4.67
    elif marks ==  21:
        return 4.33
    elif marks == 20:
        return 4
    elif marks == 19:
        return  3.5
    elif marks == 18:
        return 3
    elif marks == 17:
        return 2.5
    elif marks == 16:
        return 2

def QPP(marks):
    QP=0
    if marks >= 64:
        QP=QP+16
        return QP
    elif marks >= 63:
        QP=QP+15.67
        return QP
    elif marks >= 62:
        QP=QP+15.33
        return QP
    elif marks >= 61:
        QP=QP+15
        return QP
    elif marks >= 60:
        QP=QP+14.67
        return QP
    elif marks >= 59:
        QP=QP+14.33
        return QP
    elif marks >= 58:
        QP=QP+14
        return QP
    elif marks >= 57:
        QP=QP+13.67
        return QP
    elif marks>=48:
        QP=QP+12
        return QP
    elif  marks>=47:
        QP=QP+11.67
        return QP
    elif (marks>=46):
        QP=QP+11.33
        return QP
    elif (marks >=45):
        QP =QP+11
        return QP
    elif (marks>=44):
        QP=QP+10.67
        return QP
    elif (marks >=43):
        QP =QP+10.33
        return QP
    elif (marks>=42):
        QP=QP+10
        return QP
    elif (marks >=41):
        QP =QP+9.67
        return QP
    elif (marks>=40):
        QP=QP+9.33
        return QP
    elif (marks >=39):
        QP =QP+9
        return QP
    elif (marks>=38):
        QP=QP+8.67
        return QP
    elif (marks >=37):
        QP =QP+8.33
        return QP
    elif (marks>=36):
        QP=QP+8
        return QP
    elif (marks >=35):
        QP =QP+7.67
        return QP
    elif (marks>=34):
        QP=QP+7.33
        return QP
    elif (marks >=33):
        QP =QP+7
        return QP
    elif (marks>=32):
        QP=QP+6.67
        return QP
    elif (marks >=31):
        QP =QP+6.33
        return QP
    elif (marks>=30):
        QP=QP+6
        return QP
    elif (marks >=29):
        QP =QP+5.67
        return QP
    elif (marks>=28):
        QP=QP+5.33
        return QP
    elif (marks >=27):
        QP =QP+5
        return QP
    elif (marks>=26):
        QP=QP+4.67
        return QP
    elif (marks >=25):
        QP =QP+4.33
        return QP
    elif (marks>=24):
        QP=QP+4
        return QP

def qualitypoint(credithrs, obtnumbers):
    pass

def mastr():
    enablentry()
    credit1 = int(entrya1.get())
    credit2 = int(entrya2.get())
    credit3 = int(entrya3.get())
    credit4 = int(entrya4.get())
    credit5 = int(entrya5.get())
    credit6 = int(entrya6.get())

    entryb1.delete(0, END)
    entryb2.delete(0, END)
    entryb3.delete(0, END)
    entryb4.delete(0, END)
    entryb5.delete(0, END)
    entryb6.delete(0, END)

    entryd1.delete(0, END)
    entryd2.delete(0, END)
    entryd3.delete(0, END)
    entryd4.delete(0, END)
    entryd5.delete(0, END)
    entryd6.delete(0, END)

    entryf1.delete(0, END)
    entryf2.delete(0, END)
    entryf3.delete(0, END)
    entryf4.delete(0, END)
    entryf5.delete(0, END)
    entryf6.delete(0, END)

    tcred = credit1 + credit2 + credit3 + credit4 + credit5 + credit6

    totalcredit = Label(root, text = "Total Credits: " + str(tcred) )
    totalcredit.place(x=225,y=262)

    entryb1.insert(0,int(credit1)*20)
    entryb2.insert(0,int(credit2)*20)
    entryb3.insert(0,int(credit3)*20)
    entryb4.insert(0,int(credit4)*20)
    entryb5.insert(0,int(credit5)*20)
    entryb6.insert(0,int(credit6)*20)

    obtained1 = int(entryc1.get())
    obtained2 = int(entryc2.get())
    obtained3 = int(entryc3.get())
    obtained4 = int(entryc4.get())
    obtained5 = int(entryc5.get())
    obtained6 = int(entryc6.get())
    
    totnum = int(entryb1.get()) + int(entryb2.get()) + int(entryb3.get()) + int(entryb4.get()) + int(entryb5.get()) + int(entryb6.get())
    totnumber = Label(root, text = "Total Numbers: " + str(totnum))
    totnumber.place(x=327,y=262)

    tobtained = obtained1 + obtained2 + obtained3 + obtained4 + obtained5 + obtained6
    totalobtained = Label(root, text = "Total Obtained: " + str(tobtained))
    totalobtained.place(x=443,y=262)

    entryd1.insert(0,"{:.2f}".format((100*(obtained1/(int(credit1)*20)))) + '%')
    entryd2.insert(0,"{:.2f}".format((100*(obtained2/(int(credit2)*20)))) + '%')
    entryd3.insert(0,"{:.2f}".format((100*(obtained3/(int(credit3)*20)))) + '%')
    entryd4.insert(0,"{:.2f}".format((100*(obtained4/(int(credit4)*20)))) + '%')
    entryd5.insert(0,"{:.2f}".format((100*(obtained5/(int(credit5)*20)))) + '%')
    entryd6.insert(0,"{:.2f}".format((100*(obtained6/(int(credit6)*20)))) + '%')

    if (credit1 == 2):
        QP1 = CH2(obtained1)
    elif (credit1 == 3):
        QP1 = CH3(obtained1)
    elif (credit1 == 4):
        QP1 = CH4(obtained1)

    if (credit2 == 2):
        QP2 = CH2(obtained2)
    elif (credit2 == 3):
        QP2 = CH3(obtained2)
    elif (credit2 == 4):
        QP2 = CH4(obtained2)

    if (credit3 == 2):
        QP3 = CH2(obtained3)
    elif (credit3 == 3):
        QP3 = CH3(obtained3)
    elif (credit3 == 4):
        QP3 = CH4(obtained3)

    if (credit4 == 2):
        QP4 = CH2(obtained4)
    elif (credit4 == 3):
        QP4 = CH3(obtained4)
    elif (credit4 == 4):
        QP4 = CH4(obtained4)

    if (credit5 == 2):
        QP5 = CH2(obtained5)
    elif (credit5 == 3):
        QP5 = CH3(obtained5)
    elif (credit5 == 4):
        QP5 = CH4(obtained5)

    if (credit6 == 2):
        QP6 = CH2(obtained6)
    elif (credit6 == 3):
        QP6 = CH3(obtained6)
    elif (credit6 == 4):
        QP6 = CH4(obtained6)

    entryf1.insert(0,str(QP1))
    entryf2.insert(0,str(QP2))
    entryf3.insert(0,str(QP3))
    entryf4.insert(0,str(QP4))
    entryf5.insert(0,str(QP5))
    entryf6.insert(0,str(QP6))

    gradepoints = QP1 + QP2 + QP3 + QP4 + QP5 + QP6

    if ((gradepoints/tcred) > 4):
        tgpa = str(4)
    else:
        tgpa = "{:.2f}".format((gradepoints/tcred))
    gpa = Label(root, text = "GPA: " + tgpa, font = ('Helvetica', 12, 'bold'))
    gpa.place (x=400, y=300)

cal = Button(text = "Calculate", padx=15, pady=5, command = mastr)
cal.place(x=700, y=355)

root.mainloop()