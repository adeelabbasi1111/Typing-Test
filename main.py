from tkinter import *
from threading import *
import time

window = Tk()
window.geometry('500x500')
window.title('Typing test')
window.config(bg='#3C3A3B')


def start_test():
    for widget in window.winfo_children():
       widget.destroy()
    global time_counter , inp
    time_counter = Label(window, text="", bg='#3C3A3B',fg='sky blue',font='Arial 20 bold')
    inp = Text(window,wrap=WORD,bg='#3C3A3B',fg='white',font='Arial 15 bold',width=40,height=10)
    init_b = Button(window,text='Start Timer',font="Arial 20 bold",command=start_timer)
    inp.insert("1.0",'Start typing about yourself , name age education')
    time_counter.grid(row=0, column=0, columnspan=2)
    inp.grid(row=1, column=0, columnspan=2,padx=30,pady=30)
    init_b.grid(row=2, column=0, columnspan=2)


def start_timer():
    inp.delete('1.0',END)
    inp.focus()
    t1 = Thread(target=clock)
    t1.start()

def clock():
    global seconds
    count = 60
    seconds = count
    while count > 0:
        time.sleep(1)
        count -= 1
        time_counter.config(text=count)
    calculator()

def calculator():
    string = inp.get('1.0', END)
    wpm = int(len(string.split(' '))/seconds*60)
    characters = 0
    for char in string:
        if char !="\n":
            characters += 1
    cpm = int(characters/seconds*60)

    for widget in window.winfo_children():
       widget.destroy()

    result = Label(window, text=f"You've typed {wpm} words and\n {cpm} characters per minute", font='Arial 15 bold')
    result.grid(row=0, column=0, columnspan=2,padx=100,pady=200)


start_b = Button(window, text='Start', bg='yellow',fg='black', font=('Arial', 30, 'bold'),command=start_test)

start_b.grid(row=0, column=0,padx=200, pady=200)








window.mainloop()