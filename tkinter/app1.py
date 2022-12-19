from tkinter import *
import time
root= Tk()
HEIGHT=500
WIDTH=700

root.title('Welcome to this application')
# root.eval('tk::PlaceWindow . center')

x=root.winfo_screenwidth() // 2 - int(WIDTH/2)
y=int(root.winfo_screenheight()*0.14)

screen_resolution= str(WIDTH)+'x'+str(HEIGHT) + '+' + str(x) + '+' + str(y)
root.geometry(screen_resolution) # to set coordiantes of app while running 

# root.geometry('700x500')
root.configure(background='lightgrey')
root.pack_propagate(False)

def menubar():
    menu=Menu(root) #declaring menu-bar
    file=Menu(menu,tearoff=0) #declaring items in menu
    file.add_command(label='new') #creating items in menu
    file.add_separator() #inserts a seperator line
    file.add_command(label='save') 
    file.add_command(label='save as') 
    
    float_menu=Menu(menu, tearoff=0)
    float_menu.add_command(label='text')
    # float_menu.add_command(label='image')
    
    submenu=Menu(float_menu) #decalring submenu-bar
    media=Menu(submenu, tearoff=0) 
    media.add_command(label='Images')
    media.add_command(label='Video')
    float_menu.add_cascade(label='Media', menu=media)
    
    menu.add_cascade(label='File', menu=file) #displaying and labeling menu
    menu.add_cascade(label='Insert', menu=float_menu) 
    
    root.config(menu=menu)    
menubar()

lb = Label(root,text='button not clicked')
lb.grid(column=0,row=0) #.grid() to display the element
lb.configure(font="Montserrat",bg='lightgrey') # to change font

txt=Entry(root,width=15)
txt.grid(column=0,row=1)
txt.configure(font="Montserrat",bg='lightgrey',)

def clicked():
    if txt.get()=="":
        res="You wrote nothing"
    else:
        res="You wrote " + txt.get()   
    lb.configure(text=res)
round=PhotoImage(file='GUI_application/tkinter/button.png')
btn=Button(root,image=round,border=0,bd=0,command=clicked,background='lightgrey',activebackground='lightgrey')
# btn = Button(
#     root, 
#     text='click me',
#     command=clicked,
#     font=("Courier+New"),
#     bg="lightblue",
#     fg="white",
#     activebackground="darkblue",
#     activeforeground="black",
#     bd=0)
btn.grid(column=1,row=0)

def hor_scale():
    v1 = DoubleVar()

    def show1():  

        sel = "Horizontal Scale Value = " + str(v1.get())
        l1.config(text = sel, font =("Courier", 14))  
    
    
    s1 = Scale( root, variable = v1, 
               from_ = 0, to = 100, 
               orient = HORIZONTAL)
    
    l3 = Label(root, text = "Horizontal Scaler")
    
    b1 = Button(root, text ="Display Horizontal", 
                command = show1, 
                bg = "yellow")  
    
    l1 = Label(root)

    s1.grid(column=3,row=4) 
    l3.grid(column=3,row=3) 
    b1.grid(column=3,row=6) 
    l1.grid(column=3,row=7) 
hor_scale()

def ver_scale():
    v2 = DoubleVar()
  
    def show2():
        sel = "Vertical Scale Value = " + str(v2.get()) 
        l2.config(text = sel, font =("Courier", 14))
    
    s2 = Scale( root, variable = v2,
               from_ = 100, to = 0,
               orient = VERTICAL) 
    
    l4 = Label(root, text = "Vertical Scaler")
    
    b2 = Button(root, text ="Display Vertical",
                command = show2,
                bg = "purple", 
                fg = "white")
    
    l2 = Label(root)
    
    s2.grid(column=3,row=9)
    l4.grid(column=3,row=8)
    b2.grid(column=3,row=10)
    l2.grid(column=3,row=11)
ver_scale()

root.mainloop()