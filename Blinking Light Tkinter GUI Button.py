#import necessary libraries
from time import sleep
import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import ttk

#set numbering system and disable warnings
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#set pin direction
GPIO.setup(7, GPIO.OUT, initial = 0)

#variable to track when button is pressed or not pressed
button_on = False 

def blinking():
    global button_on
    if button_on == False:
        GPIO.output(7,0)
        print('off')
        sleep(0.5)
        GPIO.output(7,1)
        print('on')
        sleep(0.5)
        GPIO.output(7,0)
        print('off')
        sleep(0.5)
        GPIO.output(7,1)
        print('on')
        sleep(0.5)
    root.after(1000, blinking)

def stopblinking(event):
    global button_on
    button_on = True
    print(stopblinking)
    GPIO.output(7,1)
    return button_on

def button_released(event):
    global button_on
    button_on = False 
    print(button_released)
    return button_on
    blinking()

#Tkinter
root = tk.Tk()
root.geometry('400x400')
btn = ttk.Button(root, text='Light')
btn.bind('<ButtonPress-1>', stopblinking)
btn.bind('<ButtonRelease-1>', button_released)
btn.focus()
btn.pack(expand=True)
root.after(1000, blinking)
root.mainloop()