from tkinter import *
from tkinter import messagebox
import time
import random
from fpdf import FPDF
root = Tk()
root.geometry('1600x800+0+0')
root.title("Desktop Application")

''' Defining variables '''
newWindow = object
operator = ""
text_input = StringVar()
text_history = StringVar()
randomReference= StringVar()
discount = IntVar()
discount_set = {'MAX50':0.5,'MAX30' : 0.3}
coupan_code = StringVar()
chicken_burger = StringVar()
chicken_burger.set('0')
veg_burger = StringVar()
veg_burger.set('0')
fries = StringVar()
fries.set('0')
coldDrink = StringVar()
coldDrink.set('0')
water_tax = StringVar()
vatTax = StringVar()
service_tax = StringVar()
sumUp =StringVar()
'''Cost of Items '''
cost_chicken = 80
cost_veg = 60
cost_fries = 50
cost_drink = 30

'''tax Percentages'''
water_tax_per = 0.01
service_tax_per = 0.12
vat_tax_per = 0.09

array_entry = [['Ref No.:' , randomReference.get() ],['Chicken Burger:',chicken_burger.get() , cost_chicken]
    ,['Veg Burger: ',veg_burger.get() , cost_veg],['Fries: ',fries.get(),cost_fries],
               ['ColdDrink:',coldDrink.get(),cost_drink] ]

''' defining Functions '''

def generateBill():

    file = open('Bill.txt','w')
    file.write('Ref No : '  + str(randomReference.get()) + '\n')
    file.write('Chicken Burger: ' + chicken_burger.get() + ' ' + str(cost_chicken) + '\n')
    file.write('Veg Burger: ' + veg_burger.get() + ' ' + str(cost_veg) + '\n')
    file.write('Fries: ' + fries.get() + ' ' + str(cost_fries) + '\n')
    file.write('ColdDrink: ' + coldDrink.get() +' ' + str(cost_drink) + '\n' )
    file.write('Total: ' + sumUp.get() +'\n')
    file.write('Discount: ' + str(discount.get()))
    file.close()


def close():

    global newWindow
    newWindow.destroy()
    if  len(coupan_code.get()) == 0 :
        messagebox.showinfo('Error','Enter the Coupan')
    elif coupan_code.get() not in discount_set.keys():
       messagebox.showinfo('Error','Coupan Invalid')
       coupan_code.set('')
    else :
       id = random.randint(1347, 9843)
       randomReference.set(str(id))
       cost = int(chicken_burger.get())*cost_chicken + int(veg_burger.get())*cost_veg + int(fries.get())*cost_fries + int(coldDrink.get())*cost_drink
       res = cost * (water_tax_per + service_tax_per + vat_tax_per) + cost
       discount_price = res - discount_set[str(coupan_code.get())]*res
       sumUp.set('Rs' + str(discount_price))
       water_tax.set(str(water_tax_per))
       vatTax.set(str(vat_tax_per))
       service_tax.set(str(service_tax_per))
       discount.set(discount_set[str(coupan_code.get())]*res)
       coupan_code.set('')

def evaluateBill():
    if int(chicken_burger.get()) != 0 or int(veg_burger.get()) != 0 or int(fries.get()) != 0 or int(coldDrink.get()) != 0  :
       id = random.randint(1347,9843)
       randomReference.set(str(id))
       cost = int(chicken_burger.get())*cost_chicken + int(veg_burger.get())*cost_veg + int(fries.get())*cost_fries + int(coldDrink.get())*cost_drink
       res = cost*(water_tax_per + service_tax_per + vat_tax_per) + cost
       sumUp.set('Rs'+str(res))
       water_tax.set(str(water_tax_per))
       vatTax.set(str(vat_tax_per))
       service_tax.set(str(service_tax_per))
    elif int(chicken_burger.get()) == 0 and int(veg_burger.get()) == 0 and int(fries.get()) == 0 and int(coldDrink.get()) == 0 :
        messagebox.showinfo('Error', 'Make an order')

def applyDiscount():
    global newWindow
    newWindow = Toplevel(root)
    newWindow.title('Enter the Discount')
    newWindow.geometry('700x300')
    new_label = Label(newWindow, text=' Enter the Coupan Code ', bd=8, bg='grey', font=('arial', 20, 'bold'),
                      justify='right')
    new_label.grid(row=0, column=1, columnspan=3)
    new_entry = Entry(newWindow,textvariable = coupan_code,font=('arial', 20, 'bold'),bd = 6,bg = 'white',fg = 'black')
    new_entry.grid(row = 0,column = 5 ,columnspan  = 4)
    exit = Button(newWindow,text = 'Close' , font =('arial',15,'bold'),command = close)
    exit.grid(row = 6 ,column =  1)

def reset():
    randomReference.set('')
    fries.set('0')
    chicken_burger.set('0')
    veg_burger.set('0')
    coldDrink.set('0')
    water_tax.set('0')
    service_tax.set('0')
    vatTax.set('0')
    sumUp.set('0')

def onClick(number):
    global operator
    operator += number
    text_input.set(operator)
    text_history.set(operator)

def evaluateCalcy():
    if text_input.get():
       global operator
       operator = str(eval(text_input.get()))
       text_input.set(operator)
       text_history.set(operator)
    else :
        messagebox.showinfo('Error','No Input Found')

def clearText():
    if text_input.get():
       text_history.set(text_input.get())
       stack = [i for i in text_input.get()]
       stack.pop()
       text_input.set("".join(stack))
    else :
        messagebox.showinfo('Error','No input to be Clear')

def historyText():
    if text_input.get():
        messagebox.showinfo('History',text_history.get())


""" Making Frames """

top = Frame(root,bg = 'powder blue',relief =SUNKEN,width = 1600,height = 80)
top.pack(side = TOP)
left = Frame(root,bg = 'powder blue',relief =SUNKEN,width = 800,height = 700)
left.pack(side = LEFT)
right = Frame(root,bg = 'powder blue',relief =SUNKEN,width = 300,height = 700)
right.pack(side = RIGHT)

""" Inserting in frames """

''' Top Frame '''

top_info_label = Label(top,text ='Restaurant Management System',bg = 'powder blue',font = ('arial',30,'bold'),bd = 10,anchor = 'w')
top_info_label.grid(row = 0 ,column = 0)
top_time_label = Label(top,text =time.asctime(),bg = 'powder blue',font = ('arial',20,'bold'),bd = 10,anchor = 'w')
top_time_label.grid(row = 1 ,column = 0)

''' Right Frame'''

right_entry_text = Entry(right,textvariable = text_input,font = ('arial',20,'bold'),bg ='powder blue',bd = 30,insertwidth = 4,justify = 'right')
right_entry_text.grid(columnspan = 6)

'''Making Buttons in right frame '''

button7 = Button(right,text = '7',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = lambda : onClick('7'))
button7.grid(row = 2,column = 0)
button8 = Button(right,text = '8',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = lambda : onClick('8'))
button8.grid(row = 2,column = 1)
button9 = Button(right,text = '9',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = lambda : onClick('9'))
button9.grid(row = 2,column = 2)
buttonAdd = Button(right,text = '+',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = lambda : onClick('+'))
buttonAdd.grid(row = 2,column = 3)

button6 = Button(right,text = '6',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = lambda : onClick('6'))
button6.grid(row = 3,column = 0)
button5 = Button(right,text = '5',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = lambda : onClick('5'))
button5.grid(row = 3,column = 1)
button4 = Button(right,text = '4',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = lambda : onClick('4'))
button4.grid(row = 3,column = 2)
buttonSub = Button(right,text = '-',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = lambda : onClick('-'))
buttonSub.grid(row = 3,column = 3)

button1 = Button(right,text = '1',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = lambda : onClick('1'))
button1.grid(row = 4,column = 0)
button2 = Button(right,text = '2',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = lambda : onClick('2'))
button2.grid(row = 4,column = 1)
button3 = Button(right,text = '3',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = lambda : onClick('3'))
button3.grid(row = 4,column = 2)
buttonMul = Button(right,text = '*',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = lambda : onClick('*'))
buttonMul.grid(row = 4,column = 3)

buttonDec = Button(right,text = '.',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = lambda : onClick('.'))
buttonDec.grid(row = 5,column = 0)
buttonZero = Button(right,text = '0',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = lambda : onClick('0'))
buttonZero.grid(row = 5,column = 1)
buttonEquals = Button(right,text = '=',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = evaluateCalcy)
buttonEquals.grid(row = 5,column = 2)
buttonDiv = Button(right,text = '/',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = lambda : onClick('/'))
buttonDiv.grid(row = 5,column = 3)
buttonClear = Button(right,text = 'C',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = clearText)
buttonClear.grid(row = 6,column = 1)
buttonHistory = Button(right,text = 'H',padx = 16,pady = 16 ,font = ('arial',20,'bold'),bd = 8,fg = 'black',command = historyText)
buttonHistory.grid(row = 6,column = 2)

''' Left Frame '''
description = Label(left,text = 'List Of Items :-',bg = 'powder blue',bd = 8,font = ('arial',20,'bold'))
description.grid(row = 0 ,column = 0)
taxes = Label(left,text = 'List Of Taxes :- ',bg = 'powder blue',bd = 8,font = ('arial',20,'bold'))
taxes.grid(row = 0 ,column = 2)


reference_label = Label(left,text = 'Refer No.',bg = 'powder blue',bd = 8,font = ('arial',20,'bold'))
reference_label.grid(row = 1 ,column = 0)
reference_entry = Entry(left,textvariable = randomReference,bg = 'powder blue',font = ('arial',15,'bold'),bd = 8,state = 'disabled')
reference_entry.configure(background="black",disabledbackground="white",disabledforeground = 'black')
reference_entry.grid(row = 1 ,column = 1)

chicken_burger_label = Label(left,text = 'Chicken Burger',bg = 'powder blue',bd = 8 ,font = ('arial',20,'bold'))
chicken_burger_label.grid(row = 2 ,column = 0 )
chicken_burger_entry = Entry(left,textvariable = chicken_burger,bg = 'powder blue',font = ('arial',15,'bold'),bd = 8)
chicken_burger_entry.grid(row = 2,column = 1)

veg_burger_label =Label(left,text = 'Veg Burger',bg = 'powder blue',bd = 8 ,font = ('arial',20,'bold'))
veg_burger_label.grid(row = 3 ,column = 0)
veg_burger_entry = Entry(left,textvariable = veg_burger,bg = 'powder blue',font = ('arial',15,'bold'),bd = 8 )
veg_burger_entry.grid(row = 3 ,column = 1)

fries_label = Label(left,text = 'Fries',bg = 'powder blue',bd = 8 ,font = ('arial',20,'bold'))
fries_label.grid(row = 4 ,column = 0)
fries_entry = Entry(left,textvariable = fries,bg = 'powder blue',font = ('arial',15,'bold'),bd = 8)
fries_entry.grid(row = 4 ,column = 1)

coldrink_label = Label(left,text = 'Cold Drink',bg = 'powder blue',bd = 8 ,font = ('arial',20,'bold'))
coldrink_label.grid(row = 5 ,column = 0)
coldDrink_entry = Entry(left,textvariable = coldDrink,bg = 'powder blue',bd = 8 ,font = ('arial',15,'bold'))
coldDrink_entry.grid(row = 5 ,column  = 1 )

water_label = Label(left,text = 'Water Tax',bg = 'powder blue',bd = 8 ,font = ('arial',20,'bold'))
water_label.grid(row = 1 ,column = 2)
water_entry = Entry(left,textvariable = water_tax,bg = 'powder blue',bd = 8 ,font = ('arial',15,'bold'),state = 'disabled')
water_entry.config(background="black",disabledbackground="white",disabledforeground = 'black')
water_entry.grid(row = 1 , column = 3)

service_label = Label(left,text = 'Service Tax',bg = 'powder blue',bd = 8 ,font = ('arial',20,'bold'))
service_label.grid(row = 2 ,column = 2)
service_entry = Entry(left,textvariable = service_tax,bg = 'powder blue',bd = 8 ,font = ('arial',15,'bold'),state = 'disabled')
service_entry.config(background="black",disabledbackground="white",disabledforeground = 'black')
service_entry.grid(row = 2 , column = 3)

vat_label = Label(left,text = 'VAT',bg = 'powder blue',bd = 8 ,font = ('arial',20,'bold'))
vat_label.grid(row = 3 ,column = 2)
vat_entry = Entry(left,textvariable = vatTax,bg = 'powder blue',bd = 8 ,font = ('arial',15,'bold'),state = 'disabled')
vat_entry.config(background="black",disabledbackground="white",disabledforeground = 'black')
vat_entry.grid(row = 3 ,column = 3)

total_label = Label(left,text = 'Total',bg = 'powder blue',bd = 8 ,font = ('arial',20,'bold'))
total_label.grid(row = 4,column = 2)
total_entry = Entry(left,textvariable = sumUp,bg = 'powder blue',bd = 8 ,font = ('arial',15,'bold'),state = 'disabled')
total_entry.config(background="black",disabledbackground="white",disabledforeground = 'black')
total_entry.grid(row = 4 ,column = 3)

discount_label = Label(left,text = 'Discount',bg = 'powder blue',bd = 8 ,font = ('arial',20,'bold'))
discount_label.grid(row = 5,column = 2)
discount_entry = Entry(left,textvariable = discount,bg = 'powder blue',bd = 8 ,font = ('arial',15,'bold'),state = 'disabled')
discount_entry.grid(row = 5,column = 3)

#Button on left Frame

reset = Button(left,text = 'Reset',padx = 16,pady = 16 ,font = ('arial',15,'bold'),bd = 8,fg = 'black',command = reset)
reset.grid(row  =10 ,column = 2)

print_bill = Button(left,text = 'Print Bill',padx = 16,pady = 16 ,font = ('arial',15,'bold'),bd = 8,fg = 'black',command = generateBill)
print_bill.grid(row  =10 ,column = 1)

apply_discount =  Button(left,text = 'Apply Discount',padx = 16,pady = 16 ,font = ('arial',15,'bold'),bd = 8,fg = 'black',command = applyDiscount)
apply_discount.grid(row = 10,column = 3)

total =  Button(left,text = 'Total',padx = 16,pady = 16 ,font = ('arial',15,'bold'),bd = 8,fg = 'black',command = evaluateBill)
total.grid(row = 10,column = 0)

root.mainloop()
