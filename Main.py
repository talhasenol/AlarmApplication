import customtkinter as tk
import Guest as g  
import Register as r
import Login as l
class Main:
    def __init__(self):
        def Guest():
            self.form.destroy()
            newForm = g.Guest()  
            newForm.FORM()  
        def Register():
            self.form.destroy()
            newForm = r.Register()
            newForm.FORM()
        def Login():
            self.form.destroy()
            newForm = l.Login()
            newForm.form()

        self.form = tk.CTk()
        self.form.title("Mission Program")
        self.form.geometry("800x600")

        self.button1 = tk.CTkButton(self.form,text="Misafir Olarak Giriş", command=Guest)
        self.button1.place(x=170,y=300)

        self.button2 = tk.CTkButton(self.form,text="Kullanıcı Olarak Giriş",command=Login)
        self.button2.place(x=330,y=300)

        self.button3 = tk.CTkButton(self.form,text="Kayıt Ol", command=Register)
        self.button3.place(x=490,y=300)
        self.form.mainloop()
#A = Main()