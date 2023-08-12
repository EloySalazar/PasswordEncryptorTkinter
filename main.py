import tkinter as tk
from tkinter import messagebox

import bcrypt
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Encrypt-Decrypt")

        self.geometry("600x400")
        self.resizable(0,0)

        self.initialize_gui()

    def encrypt(self):
        password = self.entry_encrypt.get().encode('utf-8')
        salt = bcrypt.gensalt()
        self.hashed = bcrypt.hashpw(password, salt)

        self.file = open("data.dat","a")
        
        self.file.write(self.hashed.decode('utf-8'))
        self.file.write("\n")
        self.file.close()

        self.result_encrypt.delete(0,tk.END)
        
        self.result_encrypt.insert(tk.END,self.hashed)


    def decrypt(self):
        self.file = open("data.dat","r")
        view = False
       
        for h in self.file.readlines():

            if bcrypt.checkpw(self.entry_decrypt.get().encode('utf-8'), h.rstrip().encode('utf-8')) == True:
                view = True

        if view == True:
            messagebox.showinfo("Find","coincided!")

        else:
            messagebox.showinfo("Find","no match found!")
        

        

    def initialize_gui(self):
        self.label_encrypt = ctk.CTkLabel(self,text= "Encrypt:",font= ("Arial",18))
        self.label_encrypt.place(x = 0,y = 0)

        self.entry_encrypt = ctk.CTkEntry(self,font= ("Arial",18),width= 300)
        self.entry_encrypt.place(x = 100,y = 0)

        self.buton_encrypt = ctk.CTkButton(self,text ="Start encrypt",width= 40,command= self.encrypt)
        self.buton_encrypt.place(x = 400,y = 0)

        self.result_encrypt = ctk.CTkEntry(self,width = 500,border_color= "#0167e1")
        self.result_encrypt.place(x = 60,y = 100)

        self.label_decrypt = ctk.CTkLabel(self,text = "Find:",font= ("Arial",18)) 
        self.label_decrypt.place(x = 0,y = 200)

        self.entry_decrypt = ctk.CTkEntry(self,font= ("Arial",18),width= 300)
        self.entry_decrypt.place(x = 100,y = 200)

        self.buton_decrypt = ctk.CTkButton(self,text ="Start Find",width= 40,command= self.decrypt)
        self.buton_decrypt.place(x = 400,y = 200)




app = App()
app.mainloop()