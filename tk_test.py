#!/usr/bin/python

from tkinter import *
import group_list
import pygame.mixer
from tkinter.messagebox import askokcancel

sounds = pygame.mixer
sounds.init()
name = sounds.Sound("hello.wav")

g='lightblue'
r='red'
b='blue'
w='white'

debug = False

class App:

   def __init__(self, master):
      self.theMaster = master
      frame = Frame(master, bg = b)
      frame.pack()
      menu = Menu(root)
      root.config(menu=menu)
      filemenu = Menu(menu)
      menu.add_cascade(label='File', menu=filemenu)
      filemenu.add_command(label='Quit', command=quit)
      infomenu= Menu(menu)
      menu.add_cascade(label='About...',menu=infomenu)
      infomenu.add_command(label='About BattlerIII')     

      self.text=Label(frame,bg=w, text="Contact List\n Please choose one", height= 3)
      self.text.pack()

      self.b1 = Button(frame, bg=w,text = "First_Name", width = 15, command = self.First_Name)
      self.b1.pack(padx=15, pady=15)
      self.b2 = Button(frame, bg=w,text = "Nick_Name", width= 15, command = self.Nick_Name)
      self.b2.pack(padx=15, pady=15)
      self.b3 = Button(frame, bg=w,text = "Phone_Number", width= 15, command = self.Phone_Number)
      self.b3.pack(padx=15, pady=15)
      self.b4 = Button(frame, bg=w,text = "E_Mail", width= 15, command = self.E_Mail)
      self.b4.pack(padx=15, pady=15)

      self.q1 = Button(frame, bg=w,text='Quit', command=self.quit)
      self.q1.pack(expand=YES, fill=BOTH, side=LEFT)
      
   def First_Name(self):
      # make onther window
      self.first=Toplevel(bg=b)
      self.first.geometry('280x290+400+185')
      Label(self.first,bg=w, text= "Group Name ID\n Enter one ID").pack()

      self.theMaster.second=Toplevel(bg =b)
      self.theMaster.second.geometry('160x290+230+185')
      Label(self.theMaster.second,bg=w, text= "Group Name Id's").pack()

      scrollbar = Scrollbar(self.theMaster)
      scrollbar.pack(side=RIGHT, fill=Y)    

      self.theMaster.Name_id = Text(self.theMaster.second, wrap=NONE, yscrollcommand=scrollbar.set, bg = g)
      self.theMaster.Name_id.pack()

      scrollbar.config(command=self.theMaster.Name_id.yview)

      ids= group_list.list_ID('name')
      for lists in ids:
         self.theMaster.Name_id.insert(END, lists +'\n')
         

      self.look= Entry(self.first)
      self.look.pack()
      self.look.focus()
      self.look.delete(0, END)
      
      self.b1 = Button(self.first,bg=w, text = "FIND", width = 15, command = self.Find)
      self.b1.pack(padx=15, pady=15)    

      self.lists = Text(self.first, bg = g)
      self.lists.pack()

      
   def Find(self):
      look = self.look.get()
      contact = group_list.group_lookup(look)
      prints = group_list.print_person(contact)
      self.lists.insert(END, prints)
      name.play()
      
   def Nick_Name(self):
      self.first=Toplevel(bg=b)
      self.first.geometry('280x290+400+185')
      Label(self.first,bg=w, text= "Group Name ID\n Enter one ID").pack()

      self.theMaster.second=Toplevel(bg =b)
      self.theMaster.second.geometry('160x290+230+185')
      Label(self.theMaster.second,bg=w, text= "Group Name Id's").pack()

      scrollbar = Scrollbar(self.theMaster)
      scrollbar.pack(side=RIGHT, fill=Y)    

      self.theMaster.Name_id = Text(self.theMaster.second, wrap=NONE, yscrollcommand=scrollbar.set, bg = g)
      self.theMaster.Name_id.pack()

      scrollbar.config(command=self.theMaster.Name_id.yview)

      ids= group_list.list_ID('nick')
      for lists in ids:
         self.theMaster.Name_id.insert(END, lists +'\n')
         

      self.look= Entry(self.first)
      self.look.pack()
      self.look.focus()
      self.look.delete(0, END)
      
      self.b1 = Button(self.first,bg=w, text = "FIND", width = 15, command = self.Find)
      self.b1.pack(padx=15, pady=15)    

      self.lists = Text(self.first, bg = g)
      self.lists.pack()

   def Phone_Number(self):
      self.first=Toplevel(bg=b)
      self.first.geometry('280x290+400+185')
      Label(self.first,bg=w, text= "Group Name ID\n Enter one ID").pack()

      self.theMaster.second=Toplevel(bg =b)
      self.theMaster.second.geometry('160x290+230+185')
      Label(self.theMaster.second,bg=w, text= "Group Name Id's").pack()

      scrollbar = Scrollbar(self.theMaster)
      scrollbar.pack(side=RIGHT, fill=Y)    

      self.theMaster.Name_id = Text(self.theMaster.second, wrap=NONE, yscrollcommand=scrollbar.set, bg = g)
      self.theMaster.Name_id.pack()

      scrollbar.config(command=self.theMaster.Name_id.yview)

      ids= group_list.list_ID('number')
      for lists in ids:
         self.theMaster.Name_id.insert(END, lists +'\n')
         

      self.look= Entry(self.first)
      self.look.pack()
      self.look.focus()
      self.look.delete(0, END)
      
      self.b1 = Button(self.first,bg=w, text = "FIND", width = 15, command = self.Find)
      self.b1.pack(padx=15, pady=15)    

      self.lists = Text(self.first, bg = g)
      self.lists.pack()
     

   def E_Mail(self):
      self.first=Toplevel(bg=b)
      self.first.geometry('280x290+480+185')
      Label(self.first,bg='white', text= "ID Number").pack()

      self.theMaster.second=Toplevel(bg =b)
      self.theMaster.second.geometry('250x290+220+185')
      Label(self.theMaster.second,bg='white', text= "Group Name Id's").pack()

      scrollbar = Scrollbar(self.theMaster)
      scrollbar.pack(side=RIGHT, fill=Y)    

      self.theMaster.Name_id = Text(self.theMaster.second, wrap=NONE, yscrollcommand=scrollbar.set, bg = g)
      self.theMaster.Name_id.pack()

      scrollbar.config(command=self.theMaster.Name_id.yview)

      ids= group_list.list_ID('E_mail')
      for lists in ids:
         self.theMaster.Name_id.insert(END, lists +'\n')


      self.look= Entry(self.first)
      self.look.pack()
      self.look.focus()
      
      self.b1 = Button(self.first, text = "FIND", width = 15, command = self.Find)
      self.b1.pack(padx=15, pady=15)    

      self.lists = Text(self.first, bg = g)
      self.lists.pack()
     

   def quit(self):
      ans = askokcancel('Verify exit', "Really quit?")
      if ans: root.destroy()


root = Tk()
root.geometry('100x280+100+180')
application = App(root)
root.mainloop()
