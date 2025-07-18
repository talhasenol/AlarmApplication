import customtkinter as tk
from PIL import Image
import Main as m
import Login_2 as L
from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client

url = os.environ.get("urll")
key = os.environ.get("anahtarr")
supabase = create_client(url,key)

tk.set_appearance_mode("dark")  
tk.set_default_color_theme("green")  
class Login:
    def __init__(self):
        self.form = tk.CTk()
        self.form.title("Kayıt Ol")
        self.form.geometry("600x600")

        #-------------------------------------
        def control(username, userpassword):
            data = supabase.table("personeller").select("UserId,UserName,UserPassword").execute()
            data = list(data)
            
            for user in data[0][1]:
                if user["UserName"] == username and user["UserPassword"] == userpassword:
                    return user["UserId"]
            return False
        def Return():
            self.form.destroy()
            newForm = m.Main()
        def Giris():
            kontrol = control(self.entry3.get(),self.entry1.get())
            if kontrol:
                print(f"Hesap mevcut = {kontrol}")
                self.form.destroy()
                L.Login_2().Show(kontrol)
            else:
                print("Hesap Yok")
        image = tk.CTkImage(Image.open("MissionProject//Pictures//ok.png"), size=(20, 20))
        self.button2 = tk.CTkButton(self.form,text="Geri Dön",command=Return,width=20,image=image)
        self.button2.place(x=10,y=0)

        #-------------------------------------

        self.entry3 = tk.CTkEntry(self.form,placeholder_text="Kullanıcı Adınızı Giriniz")
        self.entry3.place(x=300,y=200)
        self.label3 = tk.CTkLabel(self.form,text="Kullanıcı Adı :")
        self.label3.place(x=212,y=200)

        #--------------------------------------
        self.entry1 = tk.CTkEntry(self.form,placeholder_text="şifre giriniz",show="*")
        self.entry1.place(x=300,y=250)
        self.label1 = tk.CTkLabel(self.form,text="Şifre :")
        self.label1.place(x=260,y=250)

        #----------------------------------------

        self.button = tk.CTkButton(self.form,text="Giriş",command=Giris,width=280)
        self.button.place(x=160,y=300)

        self.form.mainloop()
if __name__ == "__main__":
    app = Login()
    app.form()