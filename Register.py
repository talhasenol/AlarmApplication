import customtkinter as tk
from PIL import Image
import Main as m
import Login as L
from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client

url = os.environ.get("urll")
key = os.environ.get("anahtarr")
supabase = create_client(url,key)
tk.set_appearance_mode("dark")  
tk.set_default_color_theme("green")  
class Register:
    def __init__(self):
        self.form = tk.CTk()
        self.form.title("Kayıt Ol")
        self.form.geometry("600x600")

        #-------------------------------------

        def aaa():
            if self.a.get()==0:
                self.entry1.configure(show="*")
            else:
                self.entry1.configure(show="")
        def bbb():
            if self.b.get()==0:
                self.entry6.configure(show="*")
            else:
                self.entry6.configure(show="")
        def Return():
            self.form.destroy()
            newForm = m.Main()
        def giris():
            self.form.destroy()
            newform = L.Login()
        def Registering():
            if self.entry1.get()=="" or self.entry6.get()=="":
                self.label7.configure(text="Herhangi bir Şifre Girmediniz",text_color="red")
                self.label7.place(x=230,y=400)
            else:
                if self.entry1.get()==self.entry6.get():
                    if len(self.entry1.get())<8 or len(self.entry6.get())<8:
                        self.label7.configure(text="Girdiğiniz Şifre Çok Kısa",text_color="red")
                        self.label7.place(x=230,y=400)
                    else:
                        """
                        data = supabase.table("personeller").insert({
                            "UserName": str(self.entry3.get()),
                            "UserRealName": str(self.entry4.get()),
                            "UserMail": str(self.entry5.get()),
                            "UserPassword": str(self.entry6.get())
                        }).execute()
                        """
                        self.label7.configure(text="Kayıt Oluşturuldu",text_color="green")
                        self.label7.place(x=250,y=400)

                        self.button3 = tk.CTkButton(self.form,text="Giriş Yapın",command=giris,width=280,height=50)
                        self.button3.place(x=160,y=450)
                else:
                    self.label7.configure(text="Şifreler Birbirleriyle Uyuşmuyor",text_color="red")
                    self.label7.place(x=200,y=400)
            
            """
            data = supabase.table("personeller").insert({
                "UserName": str(self.entry3.get()),
                "UserRealName": str(self.entry4.get()),
                "UserMail": str(self.entry5.get()),
                "UserPassword": str(self.entry6.get())
            }).execute()
            """

        image = tk.CTkImage(Image.open("MissionProject//Pictures//ok.png"), size=(20, 20))
        self.button2 = tk.CTkButton(self.form,text="Geri Dön",command=Return,width=20,image=image)
        self.button2.place(x=10,y=0)

        #-------------------------------------

        self.entry3 = tk.CTkEntry(self.form,placeholder_text="Kullanıcı Adınızı Giriniz")
        self.entry3.place(x=300,y=100)
        self.label3 = tk.CTkLabel(self.form,text="Kullanıcı Adı :")
        self.label3.place(x=212,y=100)
        #-------------------------------------

        self.entry4 = tk.CTkEntry(self.form,placeholder_text=" Adınızı Giriniz")
        self.entry4.place(x=300,y=150)
        self.label4 = tk.CTkLabel(self.form,text="Adınızı giriniz :")
        self.label4.place(x=210,y=150)
        #-------------------------------------

        self.entry5 = tk.CTkEntry(self.form,placeholder_text=" Mail Adresinizi Giriniz")
        self.entry5.place(x=300,y=200)
        self.label5 = tk.CTkLabel(self.form,text="Mail Adresinizi giriniz :")
        self.label5.place(x=165,y=200)
        #-------------------------------------

        self.entry6 = tk.CTkEntry(self.form,placeholder_text=" Şifrenizi Giriniz",show="*")
        self.entry6.place(x=300,y=250)
        self.label6 = tk.CTkLabel(self.form,text="Şifrenizi giriniz :")
        self.label6.place(x=200,y=250)
        self.b = tk.CTkCheckBox(self.form,text="Göster/Gizle",command=bbb)
        self.b.place(x=450,y=250)
        #--------------------------------------
        self.entry1 = tk.CTkEntry(self.form,placeholder_text="şifre giriniz",show="*")
        self.entry1.place(x=300,y=300)
        self.label1 = tk.CTkLabel(self.form,text="Şifre :")
        self.label1.place(x=260,y=300)
        self.a = tk.CTkCheckBox(self.form,text="Göster/Gizle",command=aaa)
        self.a.place(x=450,y=300)
        self.button = tk.CTkButton(self.form,text="Kayıt Ol",command=Registering,width=280)
        self.button.place(x=160,y=350)
        self.label7 = tk.CTkLabel(self.form,text="",text_color="red")
        self.label7.place(x=250,y=400)

        self.form.mainloop()
if __name__ == "__main__":
    app = Register()
    app.FORM()