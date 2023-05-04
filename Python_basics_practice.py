from os import system

system('cls')


# -----------------------------------------------------------
# from abc import ABC,abstractmethod

# class Mammals(ABC):
#     lays_egg = False
    
#     @abstractmethod
#     def birth(self):
#         print("Gives birth without an egg")

# class Egg_laying(ABC):
#     lays_egg = True
    
#     @abstractmethod
#     def birth(self):
#         print("Gives birth by laying egg")

# class Dog(Mammals):

#     def birth(self):
#         return super().birth()

#     def bark(self):
#         print("This dog is barking")

# class Plattipus(Mammals,Egg_laying):

#     def birth(self):
#         return super().birth()

#     def quak(self):
#         print("This plattipus is quacking")

# dog = Dog()
# plattipus = Plattipus()

# print(dog.lays_egg)
# dog.birth()
# dog.bark()
# --------------------------------------------------------



### Graphical User Interface Windows (GUI)








   

































### save a file (file dialog)

# from tkinter import *
# from tkinter import filedialog

# def saveFile():
#     file = filedialog.asksaveasfile(initialdir="E:\\【JERIN】\\Python (VS code)\\Projects",
#                                     defaultextension=".txt",
#                                     filetypes=[
#                                         ("Text file",".txt"),
#                                         ("HTML file",".html"),
#                                         ("All files",".*")
#                                     ])

#     if file is None:
#         return


#     fileText = str(text.get(0.0,END))
#     # fileText = input("Enter something fool: ")
#     file.write(fileText)
#     file.close()

    

# windows = Tk()

# saveButton = Button(windows,text="Save",command=saveFile)

# saveButton.pack()

# text = Text(windows,
#             bg="light yellow",
#             font=("Ink free",25),
#             height=8,
#             width=20,
#             padx=20,
#             pady=20)

# text.pack()

# windows.mainloop()




### menubar

# from tkinter import *


# def openFile():
#     print("You opened a file!!")

# def saveFile():
#     print("You saved a file!")

# def cut():
#     print("You Cut the text!")

# def copy():
#     print("You Copied the text!")

# def paste():
#     print("You pasted the text!")

# windows = Tk()

# openImage = PhotoImage(file="folder.png")
# saveImage = PhotoImage(file="floppy-disk.png")
# exitImage = PhotoImage(file="logout.png")

# menubar = Menu(windows)
# windows.config(menu=menubar)

# fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",10))
# menubar.add_cascade(label="File",menu=fileMenu)
# fileMenu.add_command(label="Open",command=openFile,image=openImage,compound=LEFT)
# fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound=LEFT)
# fileMenu.add_separator()
# fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound=LEFT)

# editMenu = Menu(menubar,tearoff=0,font=("MV Boli",10))
# menubar.add_cascade(label="Edit",menu=editMenu)
# editMenu.add_command(label="Cut",command=cut)
# editMenu.add_command(label="Copy",command=copy)
# editMenu.add_command(label="Paste",command=paste)


# windows.mainloop()





## frame = a rectangular container to group and hold widgets

# from tkinter import *



# windows = Tk()

# frame = Frame(windows,bg="red",relief=SUNKEN,bd=7)
# frame.place(x=20,y=20)

# Button(frame,text="W",font=("Consolas",25),relief=RAISED,bd=5,width=3).pack(side=TOP)
# Button(frame,text="A",font=("Consolas",25),relief=RAISED,bd=5,width=3).pack(side=LEFT)
# Button(frame,text="S",font=("Consolas",25),relief=RAISED,bd=5,width=3).pack(side=LEFT)
# Button(frame,text="D",font=("Consolas",25),relief=RAISED,bd=5,width=3).pack(side=LEFT)


# windows.mainloop()




### new windows

# from tkinter import *


# def create_window():

#     new_window = Tk()      ## new window "on top" of ohter windows. linked to a "bottom" window
#                                  ## Tk() = new independent window

#     old_windows.destroy()

# old_windows = Tk()

# Button(old_windows,text="Create new window",font=("Comic sans",15),relief=RAISED,bd=8,command=create_window).pack()


# old_windows.mainloop()





###  window tabs

# from tkinter import *
# from tkinter import ttk

# windows = Tk()

# notebook = ttk.Notebook(windows)      ## widget that manages a collection of windows/displays

# tab1 = Frame(notebook)      ## new frame for tab 1
# tab2 = Frame(notebook)      ## new frame for tab 2

# notebook.add(tab1,text="Tab 1")
# notebook.add(tab2,text="Tab 2")
# notebook.pack(expand=True,fill=BOTH)     ## expand = exapand to fill any space not otherwise used
#                                          ## fill = fill space on x and y axis
# Label(tab1,text="Hello welcome to tab 1",bg="#00ff00",width=50,height=25).pack()
# Label(tab2,text="Hello welcome to tab 2",bg="#fff44f",width=50,height=25).pack()

# windows.mainloop()






### grid = geomentry manager that organizes widgets in a table-like structure in a parent

# from tkinter import *


# windows = Tk()

# titleLabel = Label(windows,text="Enter your info",font=("Arial",25,"bold")).grid(row=0,column=0,columnspan=2)

# firstNameLabel = Label(windows,text="First name:",font=("MV Boli",15)).grid(row=1,column=0)
# firstNameEntry = Entry(windows,font=("MV Boli",15),width=20).grid(row=1,column=1)

# lastNameLabel = Label(windows,text="Last name:",font=("MV Boli",15)).grid(row=2,column=0)
# lastNameEntry = Entry(windows,font=("MV Boli",15),width=20).grid(row=2,column=1)

# emailLabel = Label(windows,text="Email:",font=("MV Boli",15)).grid(row=3,column=0)
# emailEntry = Entry(windows,font=("MV Boli",15),width=20).grid(row=3,column=1)

# submitButton = Button(windows,text="Submit",font=("MV Boli",9),relief=RAISED,bd=5).grid(row=4,column=0,columnspan=2)


# windows.mainloop()




### progress bar

# from tkinter import *
# from tkinter .ttk import *
# import time

# def download():
#     GB = 1000
#     download = 0
#     speed = 5
    
#     while (download < GB):
#         time.sleep(0.05)
#         bar["value"]+=(speed/GB)*100
#         download+=speed
#         percent.set(str(int((download/GB)*100))+"%")
#         tasks.set(str(download)+"/"+str(GB)+" GB completed")
#         windows.update_idletasks()

# windows = Tk()

# percent = StringVar()
# tasks = StringVar()


# bar = Progressbar(windows,orient=HORIZONTAL,length=300)
# bar.pack(pady=10)

# percentLabel = Label(windows,textvariable=percent).pack()
# taskLabel = Label(windows,textvariable=tasks).pack() 

# button = Button(windows,text="Download",command=download).pack()

# windows.mainloop()




### canvas = widget that is used to draw graphs, plots, images in a windows

# from tkinter import * 

# windows = Tk()

# canvas = Canvas(windows,width=500,height=500,bg="light yellow",)
# canvas.pack(pady=10,padx=10)

# # blueLine = canvas.create_line(0,500,500,0,fill="blue",width=7)
# # redLine = canvas.create_line(0,0,500,500,fill="red",width=7)
# # blackRecangle = canvas.create_rectangle(50,50,250,250,fill="black")
# # co_ordinates = [250,0,500,500,0,500]
# # purpleTriangle = canvas.create_polygon(co_ordinates,fill="purple",outline="black",width=4)
# # arc = canvas.create_arc(0,0,500,500,fill="red",style=PIESLICE,start=0,extent=90)

# ## Creating a pokeball
# canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
# canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
# canvas.create_oval(190,190,310,310,fill="white",width=10)

# windows.mainloop()






### keyboard events

# from tkinter import *

# def doSomething(event):
#     # print("You pressed: ",event.keysym)     ## Keysymbol
#     label.config(text=event.keysym)

# windows = Tk()


# windows.bind("<Key>",doSomething)

# label = Label(windows,font=("Helvetica",50))
# label.pack()

# windows.mainloop()





### mouse events

# from tkinter import *

# def doSomething(event):
#     print("Mouse coordinates",event.x,",",event.y)


# windows = Tk()


# # windows.bind("<Button-1>",doSomething)    ## left mouse click
# # windows.bind("<Button-2>",doSomething)      ## scrool wheel click
# # windows.bind("<Button-3>",doSomething)       ## right mouse click
# # windows.bind("<ButtonRelease>",doSomething)     
# # windows.bind("<Enter>",doSomething)       ## enter the windows
# # windows.bind("<Leave>",doSomething)         ## leave the windows
# windows.bind("<Motion>",doSomething)          ## where the mouse moved

# windows.mainloop()






### drag and drop 

# from tkinter import *


# def drag_start(event):
#     widget = event.widget
#     widget.startX = event.x
#     widget.startY = event.y

# def drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x() - widget.startX + event.x
#     y = widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x,y=y)

# windows = Tk()

# redLabel = Label(windows,bg="red",height=5,width=10)
# redLabel.place(x=0,y=0)

# blueLabel = Label(windows,bg="blue",height=5,width=10)
# blueLabel.place(x=100,y=100)

# redLabel.bind("<Button-1>",drag_start)
# redLabel.bind("<B1-Motion>",drag_motion)

# blueLabel.bind("<Button-1>",drag_start)
# blueLabel.bind("<B1-Motion>",drag_motion)

# windows.mainloop()





### move images with keys

# from tkinter import *

# def move_up(event):
#     label.place(x=label.winfo_x(),y=label.winfo_y()-10)

# def move_down(event):
#     label.place(x=label.winfo_x(),y=label.winfo_y()+10)

# def move_left(event):
#     label.place(x=label.winfo_x()-10,y=label.winfo_y())

# def move_right(event):
#     label.place(x=label.winfo_x()+10,y=label.winfo_y())

# window = Tk()
# window.geometry("500x500")

# window.bind("<w>",move_up)
# window.bind("<s>",move_down)
# window.bind("<a>",move_left)
# window.bind("<d>",move_right)
# window.bind("<Up>",move_up)
# window.bind("<Down>",move_down)
# window.bind("<Left>",move_left)
# window.bind("<Right>",move_right)

# image = PhotoImage(file="sports-car.png")
# label = Label(window,image=image)
# label.place(x=250,y=250)



# window.mainloop()





### move images on a canvas

# from tkinter import * 


# def move_up(event):
#     canvas.move(Myimage,0,-10)

# def move_down(event):
#     canvas.move(Myimage,0,10)

# def move_left(event):
#     canvas.move(Myimage,-10,0)

# def move_right(event):
#     canvas.move(Myimage,10,0)

# window = Tk()

# window.bind("<w>",move_up)
# window.bind("<s>",move_down)
# window.bind("<a>",move_left)
# window.bind("<d>",move_right)
# window.bind("<Up>",move_up)
# window.bind("<Down>",move_down)
# window.bind("<Left>",move_left)
# window.bind("<Right>",move_right)

# canvas = Canvas(window,width=500,heigh=500)
# canvas.pack()

# photoimage = PhotoImage(file="sports-car.png")
# Myimage = canvas.create_image(4,7,image=photoimage,anchor=NW)



# window.mainloop()





### 2D animation on a canvas

# from tkinter import *
# import time

# WIDTH = 500
# HEIGHT = 500
# xVelocity = 3
# yVelocity = 2

# window = Tk()

# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()

# bg_image = PhotoImage(file="space.png")
# background = canvas.create_image(0,0,image=bg_image,anchor=NW)

# photo_image = PhotoImage(file="enemy.png")
# Myimage = canvas.create_image(0,0,image=photo_image,anchor=NW)

# image_width = photo_image.width()
# image_height = photo_image.height()


# while True:
#     coordinates = canvas.coords(Myimage)
#     print(coordinates)

#     if (coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
#         xVelocity = -xVelocity 

#     if (coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
#         yVelocity = -yVelocity 

#     canvas.move(Myimage,xVelocity,yVelocity)
#     window.update()
#     time.sleep(0.01)


# window.mainloop()





### multiple animation

# from tkinter import *
# from Ball import *
# import time

# WIDTH = 500
# HEIGHT = 500


# window = Tk()

# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()

# vollyball = Ball(canvas,0,0,100,3,2,"white")
# tennisball = Ball(canvas,0,0,50,6,4,"green")
# basketball = Ball(canvas,0,0,150,10,2,"orange")


# while True:
#     vollyball.move()
#     tennisball.move()
#     basketball.move()
#     window.update()
#     time.sleep(0.01)

# window.mainloop()