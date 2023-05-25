import random
import tkinter as tk
from tkinter import messagebox
import threading
import webbrowser
class password(tk.Tk):
    
    
    def Passwod_generator(self):
        if self.entry_length.get()=="":
         messagebox.showerror("Eroor","Enter Password Length..")
        elif not self.with_numbers and not self.with_sympol and not self.with_upper and not self.with_lower:
            messagebox.showerror("Eroor","Enable At Least One Option...")
        else:
         self.password_entry.delete(0,1000)
         self.all=""
         self.ubber_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
         self.lower_case="abcdefghijklmnopqrstuvwxyz"
         self.numbers="12345678910112233445566778899003344556677889900"
         self.sympols="''&!?\/|#$%^*()_-+=:;,``~"
         
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
         
          entry_password=self.password_entry.insert(0,finally_password)
         
          return entry_password
    
    
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
2) Enable At Least One Option To Get Your Password...''')

    def my_git_hub(self):
        webbrowser.open("https://github.com/KILLER-RAMADAN") 
    
   
    def __init__(self):
        
        self.with_numbers=False
        
        
        self.with_lower=False
        
        
        self.with_upper=False
        
        
        self.with_sympol=False
        
        
        
        super().__init__()
        
        self.geometry("400x270+600+200")
        
        self.title("Password Generator")
        
        self.resizable(0,0)
        
        self.iconbitmap("images//secure.ico")
        
        self.attributes("-topmost",True)
        
        
        self.img1=tk.PhotoImage(file="images\\off.png")
        
        self.img2=tk.PhotoImage(file="images\\on.png")
        
        self.img3=tk.PhotoImage(file="images\\about.png")
        
        self.img4=tk.PhotoImage(file="images\\github.png")
        
        self.password_lablel=tk.Label(self,text="Your Password:",font=("arial,7,bold"))
        
        self.password_lablel.place(x=0,y=30)
        
        
        self.password_entry=tk.Entry(self,width=19,font=("arial,5,bold"),relief="solid",highlightcolor="red",highlightthickness=2)
        self.password_entry.place(x=160,y=30)
        
        
        
        self.length_label=tk.Label(self,text="Password Length:",font=("arial,7,bold"))
        
        self.length_label.place(x=0,y=80)
        
        self.entry_length=tk.Entry(self,width=17,font=("arial,5,bold"),relief="solid",highlightcolor="green",highlightthickness=2)
        
        self.entry_length.place(x=180,y=80)
        
        
        
        ########
        self.make_random_pass=tk.Button(self,text="Generate Password",bg="green",height=2,relief="groove",fg="white",command=self.Passwod_generator)
        
        self.make_random_pass.place(x=140,y=125)
        
        self.make_random_num_pass=tk.Button(self,text="numbers",command=self.with_num,bd=0)
        
        self.make_random_num_pass.place(x=140,y=170)
        self.make_random_num_pass.configure(image=self.img1)
        
        self.num_label=tk.Label(self,text="With numbers",font=("arial,7,bold"))
        
        self.num_label.place(x=0,y=180)
        #########
        
        
        #######
        self.make_random_sym_pass=tk.Button(self,text="symplols",command=self.with_sym,bd=0)
        
        self.make_random_sym_pass.place(x=345,y=170)
        
        self.make_random_sym_pass.configure(image=self.img1)
        
        self.sym_label=tk.Label(self,text="With Sympols",font=("arial,7,bold"))
        
        self.sym_label.place(x=200,y=180)
        #######
        
        ########
        self.make_random_Upper=tk.Button(self,text="upper",bd=0,command=self.with_Upper)
        
        self.make_random_Upper.place(x=140,y=220)
        
        self.make_random_Upper.configure(image=self.img1)
        
        self.ubb_label=tk.Label(self,text="With Upper Le",font=("arial,7,bold"))
        
        self.ubb_label.place(x=0,y=230)
        #########
        
        self.make_random_lower=tk.Button(self,text="Generate Password",bd=0,command=self.with_Lower)
        
        self.make_random_lower.place(x=345,y=220)
        
        self.make_random_lower.configure(image=self.img1)
        
        
        self.low_label=tk.Label(self,text="With Lower Le",font=("arial,7,bold"))
        
        self.low_label.place(x=200,y=230)
        ##########
        
        
        
        #############
        self.info=tk.Button(self,text="info",bd=0,command=self.info)
        
        self.info.place(x=0,y=0)
        
        self.info.configure(image=self.img3)
        
        ############
        
        
        #############
        self.github=tk.Button(self,text="Git",bd=0,command=self.my_git_hub)
        
        self.github.place(x=40,y=0)
        
        self.github.configure(image=self.img4)
        
        ############
app=password()
app.mainloop()