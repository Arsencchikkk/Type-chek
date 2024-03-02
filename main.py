import ttkthemes
from tkinter import *
import tkinter.font as fonts
from tkinter import Button
import tkinter as tk
from time import sleep
import pygame
from pygame import mixer
import threading
from tkinter import ttk
import random

###########Functionality Part
totaltime = 60
time = 0
wrongwords = 0
elapsedtimeinminutes = 0
pygame.init()

# Sounds4
onClick_sound = pygame.mixer.Sound("C:\\Users\\User\\Downloads\\mouse-click-153941.mp3")

def count():
    global wrongwords, elapsedtimeinminutes, time
    while time < totaltime:
        entered_paragraph = textarea.get(1.0, END).split()
        totalwords = len(entered_paragraph)
        totalwords_count_label.config(text=totalwords)
        para_word_list = label_paragraph['text'].split()

        wrongwords = 0  # Обнуляем wrongwords перед каждой итерацией

        for pair in list(zip(para_word_list, entered_paragraph)):
            if pair[0] != pair[1]:
                wrongwords += 1

        wrongwords_count_label.config(text=wrongwords)

        elapsedtimeinminutes = time / 60
        if elapsedtimeinminutes > 0:  # Проверка деления на ноль
            wpm = (totalwords - wrongwords) / elapsedtimeinminutes
            wpm_count_label.config(text=int(wpm))
            gross_wpm = totalwords / elapsedtimeinminutes

            if gross_wpm > 0:  # Проверка на деление на ноль
                accuracy = wpm / gross_wpm * 100
                accuracy = round(accuracy)
                accuracy_percent_label.config(text=str(accuracy) + '%')
            else:
                accuracy_percent_label.config(text='0%')

        # Обновляем значение времени
        time += 1
        sleep(1)  # Задержка на 1 секунду для корректной работы таймера

def start():
    t1 = threading.Thread(target=start_timer)
    t1.start()

    t2 = threading.Thread(target=count)
    t2.start()

    onClick_sound.play()

def reset():
    global time, elapsedtimeinminutes
    time = 0
    elapsedtimeinminutes = 0
    startButton.config(state=NORMAL)
    resetButton.config(state=DISABLED)
    textarea.config(state=NORMAL)
    textarea.delete(1.0, END)
    textarea.config(state=DISABLED)

    elapsed_timer_label.config(text='0')
    remaining_timer_label.config(text='0')
    wpm_count_label.config(text='0')
    accuracy_percent_label.config(text='0')
    totalwords_count_label.config(text='0')
    wrongwords_count_label.config(text='0')

def start_timer():
    startButton.config(state=DISABLED)
    textarea.config(state=NORMAL)
    textarea.focus()

    global time_list
    time_list = [0]

    global timer_is_running
    timer_is_running = True

    def update_time():
        elapsed_time = time_list[0]
        elapsed_timer_label.config(text=elapsed_time)
        remaining_time = totaltime - elapsed_time
        remaining_timer_label.config(text=remaining_time)

        if elapsed_time >= totaltime:
            textarea.config(state=DISABLED)
            resetButton.config(state=NORMAL)
            timer_is_running = False
            return

        time_list[0] += 1
        root.after(1000, update_time)  #для того чтоб фукция вызывалась каждую 1 сек
        entered_text = textarea.get(1.0, END).strip()
        para_text = label_paragraph['text']

        for i, (entered_char, para_char) in enumerate(zip(entered_text, para_text)):
            if entered_char == para_char:
                start_index = f"1.0+{i}c"  #для того чтоб
                end_index = f"1.0+{i+1}c"
                textarea.tag_add("green", start_index, end_index)
                textarea.tag_config("green", foreground="green")
            else:
                start_index = f"1.0+{i}c"
                end_index = f"1.0+{i+1}c"
                textarea.tag_add("red", start_index, end_index)
                textarea.tag_config("red", foreground="red")

    update_time()

    startButton.config(state=DISABLED)

difficulty_levels = ["Easy", "Medium", "Hard"]


root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('940x735+300+25')
root.resizable(height=0, width=0)
root.overrideredirect(True)
from tkinter import ttk, Toplevel

mainframe=Frame(root,bd=4)
mainframe.grid()

titleframe=Frame(mainframe)
titleframe.grid()

Label_text=Label(titleframe,text='Type Check',font=('Time News Roman',28,'bold'),bg="navy",fg='white',width=38,bd=10)
Label_text.grid(pady=5)

paragraph_frame=Frame(mainframe)
paragraph_frame.grid(row=1,column=0)

paragraph_list=[
"Software engineering is a field that focuses on the systematic development and maintenance of software systems In software Software engineering encompasses a range of disciplines, including software architecture, requirements engineering, quality assurance, and project management As technology continues to advance, software engineering plays a critical role in shaping the digital landscape and driving ",
"I wake up early every morning to start my day with a fresh cup of coffee. After breakfast, I usually go for a jog in the park to get some exercise.No matter how busy life gets, I always make sure to take moments to appreciate the little things and find joy in the everyday n the evening, I unwind by reading a book or watching a movie before going to bed",
"Python is a versatile programming language commonly used for web development, data analysis, and artificial intelligence learning Python can open up numerous opportunities for aspiring programmers due to its simplicity and readability With Python, you can automate repetitive tasks Overall, Python's versatility, simplicity, and powerful features make it " ,
"After finishing my work at the office, I decided to treat myself to a nice dinner at a new restaurant in town. The ambiance was cozy, and the aroma of freshly cooked meals filled the air as I perused the menu. After much deliberation, I settled on a succulent steak accompanied by roasted vegetables As I enjoyed my meal, I couldn't help but appreciate the simple pleasures in life",

]
random.shuffle(paragraph_list)

label_paragraph=Label(paragraph_frame,text=paragraph_list[0],wraplength=920,justify=LEFT,font=('arial',14,'bold'))
label_paragraph.grid()

textarea_frame=Frame(mainframe)
textarea_frame.grid()

textarea=Text(textarea_frame,font=('arial',12,'bold'),width=100,height=7,bd=4,relief=GROOVE,wrap='word',state=DISABLED)
textarea.grid()


frame_output=Frame(mainframe)
frame_output.grid(row=3,column=0)

elapsed_time_label=Label(frame_output,text='Elapsed Time',font=('Tahoma',12,'bold'),fg='red')
elapsed_time_label.grid(row=0,column=0,padx=5)

elapsed_timer_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
elapsed_timer_label.grid(row=0,column=1,padx=5)

remaining_time_label=Label(frame_output,text='Remaining Time',font=('Tahoma',12,'bold'),fg='red')
remaining_time_label.grid(row=0,column=2,padx=5)

remaining_timer_label=Label(frame_output,text='60',font=('Tahoma',12,'bold'))
remaining_timer_label.grid(row=0,column=3,padx=5)

wpm_label=Label(frame_output,text='WPM',font=('Tahoma',12,'bold'),fg='red')
wpm_label.grid(row=0,column=4,padx=5)

wpm_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
wpm_count_label.grid(row=0,column=5,padx=5)

totalwords_label=Label(frame_output,text='Total Words',font=('Tahoma',12,'bold'),fg='red')
totalwords_label.grid(row=0,column=6,padx=5)

totalwords_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
totalwords_count_label.grid(row=0,column=7,padx=5)

wrongwords_label=Label(frame_output,text='Wrong Words',font=('Tahoma',12,'bold'),fg='red')
wrongwords_label.grid(row=0,column=8,padx=5)

wrongwords_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
wrongwords_count_label.grid(row=0,column=9,padx=5)

accuracy_label=Label(frame_output,text='Accuracy',font=('Tahoma',12,'bold'),fg='red')
accuracy_label.grid(row=0,column=10,padx=5)

accuracy_percent_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
accuracy_percent_label.grid(row=0,column=11,padx=5)


difficulty_combo = ttk.Combobox(mainframe, values=difficulty_levels)
difficulty_combo.grid(row=6, column=0, pady=5)

buttons_Frame=Frame(mainframe)
buttons_Frame.grid(row=4,column=0)

startButton=ttk.Button(buttons_Frame,text='Start',command=start,)
startButton.grid(row=0, column=0, padx=10,pady=10)

resetButton=ttk.Button(buttons_Frame,text='Reset',state=DISABLED,command=reset)
resetButton.grid(row=0,column=1,padx=10,pady=10)

exitButton=ttk.Button(buttons_Frame,text='Exit',command=root.destroy)
exitButton.grid(row=0,column=2,padx=10,pady=10)

keyboard_frame=Frame(mainframe)
keyboard_frame.grid(row=5,column=0)

frame1to0=Frame(keyboard_frame)
frame1to0.grid(row=0,column=0,pady=3)

label1=Label(frame1to0,text='1',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label2=Label(frame1to0,text='2',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label3=Label(frame1to0,text='3',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label4=Label(frame1to0,text='4',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label5=Label(frame1to0,text='5',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label6=Label(frame1to0,text='6',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label7=Label(frame1to0,text='7',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label8=Label(frame1to0,text='8',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label9=Label(frame1to0,text='9',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label0=Label(frame1to0,text='0',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

label1.grid(row=0,column=0,padx=5)
label2.grid(row=0,column=1,padx=5)
label3.grid(row=0,column=2,padx=5)
label4.grid(row=0,column=3,padx=5) 
label5.grid(row=0,column=4,padx=5)
label6.grid(row=0,column=5,padx=5)
label7.grid(row=0,column=6,padx=5)
label8.grid(row=0,column=7,padx=5)
label9.grid(row=0,column=8,padx=5)
label0.grid(row=0,column=9,padx=5)

frameqtop=Frame(keyboard_frame)
frameqtop.grid(row=1,column=0,pady=3)
labelQ=Label(frameqtop,text='Q',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelW=Label(frameqtop,text='W',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelE=Label(frameqtop,text='E',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelR=Label(frameqtop,text='R',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelT=Label(frameqtop,text='T',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelY=Label(frameqtop,text='Y',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelU=Label(frameqtop,text='U',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelI=Label(frameqtop,text='I',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelO=Label(frameqtop,text='O',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelP=Label(frameqtop,text='P',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

labelQ.grid(row=0,column=0,padx=5)
labelW.grid(row=0,column=1,padx=5)
labelE.grid(row=0,column=2,padx=5)
labelR.grid(row=0,column=3,padx=5)
labelT.grid(row=0,column=4,padx=5)
labelY.grid(row=0,column=5,padx=5)
labelU.grid(row=0,column=6,padx=5)
labelI.grid(row=0,column=7,padx=5)
labelO.grid(row=0,column=8,padx=5)
labelP.grid(row=0,column=9,padx=5)

frameatol=Frame(keyboard_frame)
frameatol.grid(row=2,column=0,pady=3)
labelA=Label(frameatol,text='A',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelS=Label(frameatol,text='S',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelD=Label(frameatol,text='D',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelF=Label(frameatol,text='F',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelG=Label(frameatol,text='G',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelH=Label(frameatol,text='H',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelJ=Label(frameatol,text='J',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelK=Label(frameatol,text='K',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelL=Label(frameatol,text='L',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

labelA.grid(row=0,column=0,padx=5)
labelS.grid(row=0,column=1,padx=5)
labelD.grid(row=0,column=2,padx=5)
labelF.grid(row=0,column=3,padx=5)
labelG.grid(row=0,column=4,padx=5)
labelH.grid(row=0,column=5,padx=5)
labelJ.grid(row=0,column=6,padx=5)
labelK.grid(row=0,column=7,padx=5)
labelL.grid(row=0,column=8,padx=5)

frameztom=Frame(keyboard_frame)
frameztom.grid(row=3,column=0,pady=3)
labelZ=Label(frameztom,text='Z',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelX=Label(frameztom,text='X',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelC=Label(frameztom,text='C',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelV=Label(frameztom,text='V',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelB=Label(frameztom,text='B',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelN=Label(frameztom,text='N',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelM=Label(frameztom,text='M',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

labelZ.grid(row=0,column=0,padx=5)
labelX.grid(row=0,column=1,padx=5)
labelC.grid(row=0,column=2,padx=5)
labelV.grid(row=0,column=3,padx=5)
labelB.grid(row=0,column=4,padx=5)
labelN.grid(row=0,column=5,padx=5)
labelM.grid(row=0,column=6,padx=5)

spaceFrame=Frame(keyboard_frame)
spaceFrame.grid(row=4,column=0,pady=3)

labelSpace=Label(spaceFrame,bg='black',fg='white',font=('arial',10,'bold'),width=40,height=2,bd=10,relief=GROOVE)
labelSpace.grid(row=0,column=0)

def changeBG(widget):
    widget.config(bg='purple')
    widget.after(100,lambda :widget.config(bg='black'))


label_numbers=[label1,label2,label3,label4,label5,label6,label7,label8,label9,label0]

label_alphabets=[labelA,labelB,labelC,labelD,labelE,labelF,labelG,labelH,labelI,labelJ,labelK,labelL,labelM,labelN,
                 labelO,labelP,labelQ,labelR,labelS,labelT,labelU,labelV,labelW,labelX,labelY,labelZ]

space_label=[labelSpace]

binding_numbers=['1','2','3','4','5','6','7','8','9','0']

binding_capital_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
                           'U','V','W','X','Y','Z']

binding_small_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
                         'u','v','w','x','y','z']

for numbers in range(len(binding_numbers)):
    root.bind(binding_numbers[numbers],lambda event,label=label_numbers[numbers]:changeBG(label))

for capital_alphabets in range(len(binding_capital_alphabets)):
    root.bind(binding_capital_alphabets[capital_alphabets],lambda event,label=label_alphabets[capital_alphabets]:changeBG(label))

for small_alphabets in range(len(binding_small_alphabets)):
    root.bind(binding_small_alphabets[small_alphabets],lambda event,label=label_alphabets[small_alphabets]:changeBG(label))

root.bind('<space>',lambda event:changeBG(space_label[0]))

root.mainloop()


