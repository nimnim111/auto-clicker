#modules
import threading
import tkinter as tk
from pynput.mouse import Button, Controller
import time

# variables
flag = True
Height = 700
Width = 800
mouse = Controller()
sleep =10
clickcount = 10
#functions
def  endclick_function():
    print("done")
    global flag
    flag = False
    button['state'] = tk.NORMAL
    button2['state'] = tk.DISABLED
def  click_function(entry):
    global flag
    flag = True
    clickcount = int(entry.get())
    print("clickcount is", clickcount)
    i = 1
    button['state'] = tk.DISABLED
    button2['state'] = tk.NORMAL
    while flag == True:
        if ( i <= clickcount):
            print(i)
            time.sleep(1)
            mouse.click(Button.left, 1)
            i = i + 1
        else:
            print("Setting the flag to false...")
            flag = False
            button['state'] = tk.NORMAL
def threadingclick_function(entry):
    t1 = threading.Thread(target=lambda:click_function(entry))
    t1.start()
def threadingend_function():
    print("threading end")
    t2 = threading.Thread(target=endclick_function)
    t2.start()

#gui code
root = tk.Tk()
canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

frame = tk.Frame(root,bg='black')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)

label = tk.Label(frame, text='How many times to click:', bg='white', font=50)
label.place(relx=0, rely =0.5, relwidth=0.5, relheight=0.25)

label2 = tk.Label(frame, text='TIme to sleep per click:', bg='white', font=50)
label2.place(relx=0, rely =0.75, relwidth=0.5, relheight=0.25)

#clickcount
entry = tk.Entry(frame, bg='white')
entry.place(relx=0.5, rely =0.5, relwidth=0.5, relheight=0.25)

#sleep time
entry2 = tk.Entry(frame, bg='white')
entry2.place(relx=0.5, rely=0.75, relwidth=0.5, relheight=0.25)



button = tk.Button(frame, text="Start" , bg='white', fg='black', font=50, command=lambda:threadingclick_function(entry))
button.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)

button2 = tk.Button(frame, text="Stop" , bg='white', fg='black', font=50, command=threadingend_function)
button2.place(relx=.5, rely=0, relwidth=0.5, relheight=0.5)



root.mainloop()
