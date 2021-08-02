#add tkinter basic template
from tkinter import *

root=Tk()
root.title("driving license")
root.geometry("400x500")




root.configure(bg="white")
canvas = Canvas(root, width=400, height=600)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 500, 55, fill="#255")
canvas.create_rectangle(0, 500, 500, 450, fill="#255")

label_ID_tag = canvas.create_text(30, 120, font=('Times', '16', 'bold'), text="ID :")
label_heading = canvas.create_text(150, 90, font=('Times', '24', 'bold italic'), text="Driving License")
label_name_tag = canvas.create_text(40, 205, font=('Times', '16', 'bold'), text="Name :")
label_Dob_tag = canvas.create_text(70, 250, font=('Times', '16', 'bold'), text="date of birth :")
label_pin_tag = canvas.create_text(50, 295, font=('Times', '16', 'bold'), text="Pin no :")
label_Address_tag = canvas.create_text(50, 350, font=('Times', '16', 'bold'), text="Address :")
label_vehicle_tag = canvas.create_text(50, 400, font=('Times', '16', 'bold'), text="Vehicle :")

label_ID = Label(root)
label_name = Label(root)
label_Dob = Label(root)
label_pin = Label(root)
label_Address = Label(root)
label_Vehicle = Label(root)

#add function
def myCardDetails():
    
    ID= "45889256494241"
    print(type(ID))
    name = "Howell"
    print(type(name))
    Dob = "07/02/2009"
    print(type(Dob))
    pin = "401201"
    print(type(pin))
    Address = "Mudwadi, Tamtalao road, Vasai (w)"
    print(type(Address))
    Vehicle = "Four"
    print(type(Vehicle))
    label_ID['text'] = ID
    label_name['text'] = name
    label_Dob['text'] = Dob
    label_pin['text'] = pin
    label_Address['text'] = Address
    label_Vehicle['text'] = Vehicle

#add button
button1 = Button(root, text = "Show my Driving lisence ", command=myCardDetails)

button1.configure(width=20, activebackground="#9EC6EE", relief=FLAT)
button1_window = canvas.create_window(150, 435, anchor=CENTER, window=button1)
label_ID_window = canvas.create_window(100, 120, anchor=CENTER, window=label_ID)
label_name_window = canvas.create_window(100, 205, anchor=CENTER, window=label_name)
label_Dateofbirth_window = canvas.create_window(170, 250, anchor=CENTER, window=label_Dob)
label_pin_window = canvas.create_window(120, 295, anchor=CENTER, window=label_pin)
label_Address_window = canvas.create_window(200, 350, anchor=CENTER, window=label_Address)
label_Vehicle_window = canvas.create_window(110, 400, anchor=CENTER, window=label_Vehicle)


canvas.pack()

#tkinter basic template end statement

root.mainloop()