from tkinter import *
from tkinter import ttk
from decimal import *
from serial import *

root = Tk()
displayed_temp = StringVar()
displayed_ph = StringVar()
displayed_stir = StringVar()
ser = Serial('COM6')

def monitoring():
    found = ser.readline()
    print(found)

def update_temppoint():
    if temp_verification(var_values[0].get()) == True:
        temp_set = var_values[0].get()
        displayed_temp.set("Current temperature setpoint: " + temp_set + "\u2103")
        ser.write(temp_set.encode('utf-8'))
    else:
        displayed_temp.set("Please enter a value between 25 and 35 (inclusive).")
    ttk.Label(root, textvariable = displayed_temp).grid(row = 3, column = 0) 
    var_values[0].delete(0, 100)
    

def update_phpoint():
    if ph_verification(var_values[1].get()) == True:
        ph_set = var_values[1].get()
        displayed_ph.set("Current pH setpoint: " + ph_set)
        ser.write(ph_set.encode('utf-8'))
    else:
        displayed_ph.set("Please enter a value between 3 and 7 (inclusive).")
    ttk.Label(root, textvariable = displayed_ph).grid(row = 4, column = 0) 
    var_values[1].delete(0, 100)


def update_stirpoint():
    if stir_verification(var_values[2].get()) == True:
        stir_set = var_values[2].get()
        displayed_stir.set("Current stirring setpoint: " + stir_set + " RPM")
        ser.write(stir_set.encode('utf-8'))
    else:
        displayed_stir.set("Please enter a value between 500 and 1500 (inclusive).")
    ttk.Label(root, textvariable = displayed_stir).grid(row = 5, column = 0) 
    var_values[2].delete(0, 100)
    

controllables = ['Temperature', 'pH', 'Stirring']
var_values = ['new_temp', 'new_ph', 'new_stir']
command_names = [update_temppoint, update_phpoint, update_stirpoint]
units = ['(\u2103)', '', '(RPM)']

def temp_verification(entered):
    if entered.isdigit():
        if Decimal(entered) >= 25 and Decimal(entered) <= 35:
            return True
        else:
            return False
    else:
        return False

def ph_verification(entered):
    if entered.isdigit():
        if Decimal(entered) >= 3 and Decimal(entered) <= 7:
            return True
        else:
            return False
    else:
        return False

def stir_verification(entered):
    if entered.isdigit():
        if Decimal(entered) >= 500 and Decimal(entered) <= 1500:
            return True
        else:
            return False
    else:
        return False


for i in range (0, 3):
    var_values[i] = ttk.Entry(root, width = 20)
    var_values[i].grid(row=i, column=1)
    enter = ttk.Button(root, command= command_names[i] , text="Enter")
    enter.grid(row=i, column=2)
    ttk.Label(root, text="Update " + controllables[i] + " Setpoint " + units[i]).grid(row=i, column=0)


monitoring()
root.mainloop()