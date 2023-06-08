import random
import tkinter as tk
from tkinter import messagebox
import threading
import webbrowser
from tkinter.ttk import *
import tkinter.ttk
from tkinter import ttk
import sys

import pyperclip

class password(tk.Tk):
    
    
    def Passwod_generator(self):
      try:
        if self.entry_length.get()=="":
         messagebox.showerror("Eroor","Enter Password Length..")
         
        elif int(self.entry_length.get())>=130:
            messagebox.showinfo("Password Manager","You Have At Least Access To '129' Char\nAt All Options..")
            
             
        elif not self.with_numbers and not self.with_sympol and not self.with_upper and not self.with_lower:
            self.password_entry.delete(0,1000)
            messagebox.showerror("Eroor","Enable At Least One Option...")
        
        else:
          
         self.password_entry.delete(0,1000)
         self.all=""
         self.ubber_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ" # 26 char
         self.lower_case="abcdefghijklmnopqrstuvwxyz" # 26 char
         self.numbers=random.randint(1000,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000) # 75 num
         self.sympols="@''&!?\/|#$%^*()_-+=:;,``~><][" # 30 sym
         
         if self.with_sympol:
             self.all+=str(self.sympols)
             
         if self.with_upper:
            self.all+=str(self.ubber_case)
            
         if self.with_lower:
           self.all+=str(self.lower_case)
           
         if self.with_numbers:
            self.all+=str(self.numbers)
            
         many_latters=int(self.entry_length.get())
         many_time=1
         for latter in range(many_time):    
          finally_password="".join(random.sample(self.all,many_latters))
         
          entry_password=self.password_entry.insert(1,finally_password)
         
          return entry_password
      except:
          messagebox.showerror("Error","You Must Input Number In password Length")
    
    def  with_num(self):
        if not self.with_numbers:
            self.make_random_num_pass.configure(image=self.img2)
            self.with_numbers=True
        else:
           self.make_random_num_pass.configure(image=self.img1)
           self.with_numbers=False   
    
    
    
    def  with_sym(self):
        if not self.with_sympol:
            self.make_random_sym_pass.configure(image=self.img2)
            self.with_sympol=True
        else:
           self.make_random_sym_pass.configure(image=self.img1)
           self.with_sympol=False    
    
    
    def  with_Upper(self):
        if not self.with_upper:
            self.make_random_Upper.configure(image=self.img2)
            self.with_upper=True
        else:
           self.make_random_Upper.configure(image=self.img1)
           self.with_upper=False    
    
    def  with_Lower(self):
        if not self.with_lower:
            self.make_random_lower.configure(image=self.img2)
            self.with_lower=True
        else:
           self.make_random_lower.configure(image=self.img1)
           self.with_lower=False  
           
    def info(self):
        messagebox.showinfo('Info','''1) Dont Forget To Enter Length Of Your Password Then Click Generate Password...
2) Enable At Least One Option To Get Your Password...
3)You Have Access To '185' char With All Options....''')

    
    def copy_pass(self):
        if self.password_entry.get()=="":
            messagebox.showinfo("Error","No Password Found!!!")
        else:
         pyperclip.copy(self.password_entry.get())
         spam = pyperclip.paste()
         messagebox.showinfo("Successfully Copy","Copied!!!!!")
    def destroy(self):
        sys.exit()
    
   
    def __init__(self):
        
        self.with_numbers=False
        
        
        self.with_lower=False
        
        
        self.with_upper=False
        
        
        self.with_sympol=False
        
        
        
        super().__init__()
        
        self.geometry("500x330+600+200")
        
        self.title("Password Generator")
        
        self.resizable(0,0)
        
        self.iconbitmap("images//secure.ico")
        
        self.attributes("-topmost",True)
        
        
        self.img1=tk.PhotoImage(file="images\\off.png")
        
        self.img2=tk.PhotoImage(file="images\\on.png")
        
        self.img3=tk.PhotoImage(file="images\\about.png")
        
        self.img4=tk.PhotoImage(file="images\\github.png")
        
        self.img5=tk.PhotoImage(file="images\\ran.png")
        
        
        self.main_label=tk.Label(text="Offline Password Generator",font=("arial,20,bold"))
        self.main_label.place(x=110,y=10)
        
        self.ran_label=tk.Label(image=self.img5)
        
        self.ran_label.place(x=360,y=5)
        
        self.password_lablel=tk.Label(self,text="Your Password:",font=("arial,7,bold"),relief="solid")
        
        self.password_lablel.place(x=0,y=50)
        
        
        
        
        
        self.password_entry=tk.Entry(self,width=31,font=("arial,5,bold"),relief="solid",highlightcolor="red",highlightthickness=2)
        self.password_entry.place(x=150,y=50)
        
        
        
        self.length_label=tk.Label(self,text="Password Length:",font=("arial,7,bold"),relief="solid")
        
        self.length_label.place(x=0,y=100)
        
        self.test_pass_label=tk.Label(text="Remember Your Password😁",font=("arial,15,bold"),relief="solid")
        
        self.test_pass_label.place(x=227,y=102)
        
        
        
        self.entry_length=tk.Entry(self,width=5,font=("arial,10,bold"),relief="solid",highlightcolor="green",highlightthickness=2)
        
        self.entry_length.place(x=165,y=100)
        
        
        
        ########
        
        style=Style()

        style.configure("TButton",font=('calibri',20,'bold'),borderwidth="4")
        style.map("TButton",foreground=[('active','!disabled','green')],
        background=[('active','black')])
        self.make_random_pass=ttk.Button(self,text="Generate Password",command=self.Passwod_generator)
        
        self.make_random_pass.place(x=30,y=136)
        
        
        self.copy=ttk.Button(self,text="Copy Password",command=self.copy_pass)
        
        self.copy.place(x=270,y=136)
        
        self.exit=ttk.Button(self,text="Exit",width=5,command=self.destroy)
        
        self.exit.place(x=210,y=190)
        
        self.app_info=ttk.Button(self,text="Info",width=5,command=self.info)
        
        self.app_info.place(x=210,y=235)
        
        self.make_random_num_pass=tk.Button(self,text="numbers",command=self.with_num,bd=0)
        
        self.make_random_num_pass.place(x=140,y=180)
        self.make_random_num_pass.configure(image=self.img1)
        
        self.num_label=tk.Label(self,text="With numbers",font=("arial,7,bold"))
        
        self.num_label.place(x=0,y=190)
        #########
        
        
        #######
        self.make_random_sym_pass=tk.Button(self,text="symplols",command=self.with_sym,bd=0)
        
        self.make_random_sym_pass.place(x=440,y=180)
        
        self.make_random_sym_pass.configure(image=self.img1)
        
        self.sym_label=tk.Label(self,text="With Sympols",font=("arial,7,bold"))
        
        self.sym_label.place(x=300,y=190)
        #######
        
        ########
        self.make_random_Upper=tk.Button(self,text="upper",bd=0,command=self.with_Upper)
        
        self.make_random_Upper.place(x=140,y=230)
        
        self.make_random_Upper.configure(image=self.img1)
        
        self.ubb_label=tk.Label(self,text="With Upper Le",font=("arial,7,bold"))
        
        self.ubb_label.place(x=0,y=240)
        #########
        
        self.make_random_lower=tk.Button(self,text="Generate Password",bd=0,command=self.with_Lower)
        
        self.make_random_lower.place(x=440,y=230)
        
        self.make_random_lower.configure(image=self.img1)
        
        
        self.low_label=tk.Label(self,text="With Lower Le",font=("arial,7,bold"))
        
        self.low_label.place(x=300,y=240)
        ##########
        
        
        
        #############
        # self.info=tk.Button(self,text="info",bd=0,command=self.info)
        
        # self.info.place(x=0,y=0)
        
        # self.info.configure(image=self.img3)
        
        # ############
        
        
        # #############
        # self.github=tk.Button(self,text="Git",bd=0,command=self.my_git_hub)
        
        # self.github.place(x=40,y=0)
        
        # self.github.configure(image=self.img4)
        
        ############
        
        self.fram1=tk.Frame(width=1000,height=300,bg="#2C3E50")
        self.fram1.place(x=0,y=280)
        
        self.rights_label=tk.Label(text="All Rights Reserved® By Ahmed Ramadan",bg="#2C3E50",fg="white",font=("arial,20,bold"))
        self.rights_label.place(x=70,y=290)
        
app=password()
app.mainloop()
