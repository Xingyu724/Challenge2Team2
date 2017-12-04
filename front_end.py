from tkinter import *
from tkinter import ttk
from decimal import *

root = Tk()

def update_temppoint():
    if temp_verification(var_values[0].get()) == True:
        temp_set = Decimal(var_values[0].get())
        displayed_temp = ttk.Label(root, text = "Current temperature setpoint: " + str(temp_set) + "\u2103").grid(row = 3, column = 0)
    # else:
       # displayed_temp = ttk.Label(root, text = "Please enter a value between 25 and 35 (inclusive).").grid(row = 3, column = 0) 
    var_values[0].delete(0, 100)
    

def update_phpoint():
    ph_set = Decimal(var_values[1].get())
    var_values[1].delete(0, 100)
    ttk.Label(root, text = "Current pH setpoint: " + str(ph_set)).grid(row = 4, column = 0)

def update_stirpoint():
    stir_set = Decimal(var_values[2].get())
    var_values[2].delete(0, 100)
    ttk.Label(root, text = "Current stirring setpoint: " + str(stir_set) + " RPM").grid(row = 5, column = 0)
    

controllables = ['Temperature', 'pH', 'Stirring']
var_values = ['new_temp', 'new_ph', 'new_stir']
command_names = [update_temppoint, update_phpoint, update_stirpoint]
units = ['(\u2103)', '', '(RPM)']

def temp_verification(entered):
    if entered.isdigit() == True:
        if int(entered) >= 25:
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



root.mainloop()