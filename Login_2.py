import customtkinter as ctk
from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client
import customtkinter as ctk
from tkcalendar import Calendar
from PIL import Image

import Guest_3
from datetime import datetime
import threading
import pystray
from plyer import notification
import time
import sys
import os
from playsound3 import playsound



# PyInstaller için kaynak yolu fonksiyonu
import sys
import os

url = os.environ.get("urll")
key = os.environ.get("anahtarr")
supabase = create_client(url,key)
def get_resource_path():
    if getattr(sys, 'frozen', False):  # EXE olarak çalışıyorsa
        return sys._MEIPASS  # PyInstaller'ın geçici klasörü
    else:  # Script olarak çalışıyorsa
        return os.path.dirname(os.path.abspath(__file__))


class Login_2:
    def __init__(self):
        self.form = None
        self.id = None
        self.item_frames = []
        self.item_buttons = []
        self.items2_frames = []
        self.items2_buttons = []
        self.alarm_active = False
        self.alarm_thread = None
        self.index = 0
        self.current_time = datetime.now().strftime("%H:%M")
    def FORM(self):
        pass   
    def Show(self,id):
        self.id = id
        data = supabase.table("Missions").select("*").eq("UserId", self.id).execute()
        data = list(data)
        #print(data[0][1])
        #print(type(data))

        self.form = ctk.CTk()
        self.form.title("User Mode")
        self.form.geometry("1200x600")
        self.form.resizable(False, False)
        def show_notification(alarm_time):
            #select MissionAdi,MissionExplanation,MissionTime,MissionMusic from Missions where MissionRemember='{id
            vericekimi = supabase.table("Missions").select("*").eq("UserId", self.id).gte("MissionRemember",alarm_time).execute().data
            liste = []
            for mission in vericekimi:
                    liste.append((mission['MissionName'], mission['MissionExplanation'], mission['MissionTime'],mission["MissionMusic"]))
            notifications=liste
            #notifications = database1.Notification(alarm_time)[0]

            notification.notify(
                title='⏰ Alarm Çalıyor!',
                message=f'Alarm Zamanı: {notifications[2]}\n{notifications[0]}\n{notifications[1]}',
                app_name='Alarm Uygulaması',
                timeout=10,  # 10 saniye
                app_icon=None  # 'icon.ico' yolunu verebilirsiniz
            )
            time.sleep(10)  # Bildirimin kapanmasını bekle

            if notifications[3]=="Davul Sesi":
                voice_path = os.path.join(get_resource_path(), "Voice", "1.mp3")
                playsound(voice_path)
                #playsound("MissionProject//Voice/1.mp3")
            elif notifications[3]=="Piano Sesi":
                voice_path = os.path.join(get_resource_path(), "Voice", "1.mp3")
                playsound(voice_path)
                #playsound("MissionProject//Voice//3.mp3")
            elif notifications[3]=="Çalar Saat":
                voice_path = os.path.join(get_resource_path(), "Voice", "1.mp3")
                playsound(voice_path)
                #playsound("MissionProject//Voice//2.mp3")

        def start():
            global alarm_active, alarm_thread
            vericekimi = supabase.table("Missions").select("*").eq("UserId", self.id).eq("MissionDate",formatted).execute().data
            liste = []
            for mission in vericekimi:
                liste.append((mission['MissionId'], mission['MissionName'], mission['MissionTime']))
            veritabani = Database.veritabani()
            aA = veritabani.todaytime(self.current_time)
            while not aA:
                aA = [('00', '00', '00', '00', '00', '00:00', '00')]
            alarm_time = str(aA[0][5])
            
            if alarm_time and not self.alarm_active:
                try:
                    datetime.strptime(alarm_time, "%H:%M")
                    self.alarm_active = True
                    self.alarm_thread = threading.Thread(target=check_alarm, args=(alarm_time,), daemon=True)
                    self.alarm_thread.start()
                except ValueError:
                    print("Geçersiz zaman formatı! Lütfen HH:MM formatında girin.")
        def check_alarm(alarm_time):
            while self.alarm_active:
                self.index = 0
                self.current_time = datetime.now().strftime("%H:%M")
                veritabani = Database.veritabani()
                print(f"Şu anki zaman: {self.current_time}, Alarm zamanı: {alarm_time}")
                if self.current_time == alarm_time:
                    #print("bura çalıştı")
                    if self.index==0:
                        show_notification(alarm_time)
                        self.index = 1
                    aA = veritabani.todaytime(self.current_time)
                    while not aA:
                        print("boşmuş")
                        aA = [('00', '00', '00', '00', '00', '99:99', '00')]
                    alarm_time = str(aA[0][5])
                else:
                    aA = veritabani.todaytime(self.current_time)
                    print(aA)
                    #print("eşit değil")
                    while not aA:
                        print("boşmuş")
                        aA = [('00', '00', '00', '00', '00', '99:99', '00')]
                    alarm_time = str(aA[0][5])
                    aA=[]
                time.sleep(3)  # 3 saniyede bir kontrol
        def bursa():
            self.form.withdraw()
            #create_icon()
        self.form.after(100,start)
        self.form.protocol("WM_DELETE_WINDOW", bursa)
        ctk.set_appearance_mode("dark")  
        ctk.set_default_color_theme("blue") 

        self.listbox = ctk.CTkScrollableFrame(self.form, width=300, height=480, corner_radius=10)
        self.listbox.place(x=25, y=65)
        self.listbox2 = ctk.CTkScrollableFrame(self.form, width=300, height=480, corner_radius=10)
        self.listbox2.place(x=380, y=65)
        from datetime import datetime
        now = datetime.now()
        formatted = now.strftime("%Y-%m-%d")  
        print(self.id)
        vericekimi = supabase.table("Missions").select("*").eq("UserId", self.id).gte("MissionDate",formatted).execute().data
        liste = []
        for mission in vericekimi:
            print((mission['MissionId'], mission['MissionName'], mission['MissionTime']))
            liste.append((mission['MissionId'], mission['MissionName'], mission['MissionTime']))
        self.items=liste
        print(f"burası ===== {self.items}")
        #KLFSDMLKSMDALKASFMLKASMDLMSDALKMDSAL
        self.item_frames = []
        self.item_buttons = []
        def add_mission():
            if self.entry1.get()=="" or self.hour_spinbox.get()=="" or self.minute_spinbox.get()=="":
                self.label7.configure(text="Lütfen Boş Bırakmayınız\nSadece Acıklama Boş Kalabilir",text_color="red")
            elif self.hour_spinbox.get().isalpha()==True or self.minute_spinbox.get().isalpha==True:
                self.label7.configure(text="Lütfen Sadece Sayı Giriniz",text_color="red")
            elif int(self.hour_spinbox.get())>24 or int(self.minute_spinbox.get())>59:
                self.label7.configure(text="Lütfen Saati En Fazla 24\nDakikayı da En Fazla 59 Girin",text_color="red")
            elif (datetime.now().strftime("%H%M")>f"{self.hour_spinbox.get()}{self.minute_spinbox.get()}" and self.calendar.get_date()==f"{datetime.now().strftime("%Y-%m-%d")}"):
                self.label7.configure(text="Dikkat Geçmiş Bir Saati Giriyorsunuz\nYa Da Yanlış Tarihi",text_color="red")
            else:
                def remembertime(text):
                    hour = 0
                    new_hour = 0
                    new_minute = 0
                    if int(self.hour_spinbox.get())==00:
                        hour == 24
                    else:
                        hour = int(self.hour_spinbox.get())
                    if text=="10 dakika kala":
                        minute = int(self.minute_spinbox.get())
                        total_minutes = hour * 60 + minute - 10
                        new_hour = total_minutes // 60
                        new_minute = total_minutes % 60
                    elif text=="30 dakika kala":
                        minute = int(self.minute_spinbox.get())
                        total_minutes = hour * 60 + minute - 30
                        new_hour = total_minutes // 60
                        new_minute = total_minutes % 60
                    elif text=="1 saat kala":
                        minute = int(self.minute_spinbox.get())
                        total_minutes = hour * 60 + minute - 60
                        new_hour = total_minutes // 60
                        new_minute = total_minutes % 60
                    elif text=="2 saat kala":
                        minute = int(self.minute_spinbox.get())
                        total_minutes = hour * 60 + minute - 120
                        new_hour = total_minutes // 60
                        new_minute = total_minutes % 60
                    elif text=="1 gün kala":
                        new_hour = int(self.hour_spinbox.get())
                        new_minute = int(self.minute_spinbox.get())
                        pass
                    if new_hour<0:
                        new_hour= new_hour+24
                    return f"{new_hour:02d}:{new_minute:02d}"
                index = 0
                if database.index()[0][0]==None:
                    index==0
                else:
                    index == database.index()[0][0]
                
                mission_data = (
                    f"{str(index+1)}"f"{" "}"
                    f"{self.entry1.get()}"f"{" "}"
                    f"{self.hour_spinbox.get()}:{self.minute_spinbox.get()}"
                )
                remembertime = remembertime(str(self.combo2.get()))
                now = datetime.now()
                formatted = now.strftime("%Y-%m-%d")
                if self.combo2.get()=="1 gün kala":
                        tarih = self.calendar.get_date()
                        index = int(tarih[-2:])-1
                        index2 = tarih[0:-3]
                        tarih = f"{index2}-{index}"
                        print(tarih)
                else:
                    tarih = self.calendar.get_date()
                if formatted>tarih:
                    tarih = formatted
                time_str = f"{self.hour_spinbox.get()}:{self.minute_spinbox.get()}"
                data = supabase.table("Missions").insert({
                    "MissionName": self.entry1.get(),
                    "MissionExplanation": self.entry2.get(),
                    "MissionDate": tarih,
                    "MissionTime": time_str,
                    "MissionRemember":remembertime,
                    "MissionMusic":self.combo.get(),
                    "UserId":self.id
                }).execute()
                """
                database.addmission(
                    self.entry1.get(),
                    self.entry2.get(),
                    tarih,
                    time_str,
                    remembertime,
                    self.combo.get(),
                )
                """
                #database.connectionclose()
                now = datetime.now()
                formatted = now.strftime("%Y-%m-%d")
                if self.combo3.get()=="Güncel Görevleriniz":
                    #mission data tuple olmalı
                    add_item_to_listbox(mission_data)
                    if formatted >= tarih:
                        add_item_to_listbox2(mission_data)
        def delete_item2(item_text):
            print(f"itemintexti === {item_text }")
            item_id = item_text[0]  
            for i, (data, frame) in enumerate(self.items2_frames):
                print(data[0])
                if data[0] == item_id:
                    frame.destroy()
                    self.items2_frames.pop(i)
                    data = supabase.table("Missions").delete().eq("MissionId",item_id).execute()
                    break        
            for i, (id, frame) in enumerate(self.item_frames):
                if id == item_id:
                    frame.destroy()
                    self.item_frames.pop(i)
                    break
        def select_item(item_text):
            for text, frame in self.item_frames:
                for widget in frame.winfo_children():
                    if isinstance(widget, ctk.CTkButton) and widget.cget("text") == text:
                        widget.configure(fg_color="#3b8Ced0" if text == item_text else "transparent")

        def on_double_click(text):
            editor = Guest_3.guest_3()
            print(text)
            editor.Show(text)

        def delete_item(item_id):
            print(f"itemintexti === {item_id}")
            for i, (id, frame) in enumerate(self.item_frames):
                if id == item_id:
                    frame.destroy()
                    self.item_frames.pop(i)
                    data = supabase.table("Missions").delete().eq("MissionId",item_id).execute()
                    break
        def add_item_to_listbox(item_data):
            print(f"burası çalışıyor şuan === {item_data}")
            if type(item_data)==str:
                item_data = tuple(item_data.split())
            # item_data örneğin: (id, görev_adı, açıklama, tarih, zaman, hatırlatma_zamanı, müzik)
            item_id = item_data[0]
            item_text = f"{item_data[1]} {item_data[2]}"  # ID + görev adı + hatırlatma saati

            item_frame = ctk.CTkFrame(self.listbox, fg_color="transparent")
            item_frame.pack(fill="x", pady=2, padx=5)

            btn = ctk.CTkButton(
                item_frame,
                text=item_text,
                fg_color="transparent",
                anchor="w",
                command=lambda data=item_data: select_item(data),
                width=200
            )
            btn.bind("<Double-Button-1>", lambda e, data=item_data: on_double_click(data))
            btn.pack(side="left", expand=True, fill="x")
            image_path = os.path.join(get_resource_path(), "Pictures", "resim2.png")
            image = ctk.CTkImage(Image.open(image_path), size=(20, 20))
            #image = ctk.CTkImage(Image.open("MissionProject/Pictures/resim2.png"), size=(20, 20))
            delete_btn = ctk.CTkButton(
                item_frame,
                image=image,
                text="",
                width=30,
                height=30,
                fg_color="transparent",
                hover_color="#d33b3b",
                command=lambda id=item_id: delete_item(item_id)
            )
            
            delete_btn.pack(side="right", padx=5)

            self.item_frames.append((item_id, item_frame))
            self.item_buttons.append(btn)
            
        def add_item_to_listbox2(item_data):
            if type(item_data)==str:
                item_data = tuple(item_data.split())
            # item_data örneğin: (id, görev_adı, açıklama, tarih, zaman, hatırlatma_zamanı, müzik
            item_text = f" {item_data[1]} {item_data[2]}"  # ID + görev adı + hatırlatma saati
            items2_frames = ctk.CTkFrame(self.listbox2, fg_color="transparent")
            items2_frames.pack(fill="x", pady=2, padx=5)
            
            btn = ctk.CTkButton(
                items2_frames,
                text=item_text,
                fg_color="transparent",
                anchor="w",
                command=lambda data=item_data: select_item(data),
                width=200
            )
            btn.bind("<Double-Button-1>", lambda e, data=item_data: on_double_click(data))
            btn.pack(side="left", expand=True, fill="x")
            image_path = os.path.join(get_resource_path(), "Pictures", "resim2.png")
            image = ctk.CTkImage(Image.open(image_path), size=(20, 20))
            #image = ctk.CTkImage(Image.open("MissionProject/Pictures/resim2.png"), size=(20, 20))
            delete_btn = ctk.CTkButton(
                items2_frames,
                image=image,
                text="",
                width=30,
                height=30,
                fg_color="transparent",
                hover_color="#d33b3b",
                command=lambda t=item_data: delete_item2(t)
            )
            delete_btn.pack(side="right", padx=5)
            
            self.items2_frames.append((item_data, items2_frames))
            self.items2_buttons.append(btn)
        for item in self.items:
            add_item_to_listbox(item)
        vericekimi = supabase.table("Missions").select("*").eq("UserId", self.id).eq("MissionDate",formatted).execute().data
        liste = []
        for mission in vericekimi:
            print((mission['MissionId'], mission['MissionName'], mission['MissionTime']))
        liste.append((mission['MissionId'], mission['MissionName'], mission['MissionTime']))
        self.items2=liste
        self.items2_frames = []
        self.items2_buttons = []
        for item2 in self.items2:
            add_item_to_listbox2(item2)
        self.calendar = Calendar(
            self.form,
            selectmode='day',
            date_pattern='yyyy-mm-dd',
            background='#2b2b2b',  # Koyu arka plan
            foreground='white',     # Yazı rengi
            selectbackground='#3b8ed0',  # Seçili gün arka plan rengi
            selectforeground='white',    # Seçili gün yazı rengi
            headersbackground='#3b3b3b',  # Başlık arka plan rengi
            headersforeground='white',   # Başlık yazı rengi
            normalbackground='#2b2b2b',  # Normal günlerin arka plan rengi
            normalforeground='white',   # Normal günlerin yazı rengi
            weekendbackground='#2b2b2b', # Hafta sonu arka plan rengi
            weekendforeground='#ff6b6b', # Hafta sonu yazı rengi (kırmızımsı)
            othermonthbackground='#1f1f1f',  # Diğer ayların günleri
            othermonthforeground='gray50',   # Diğer ayların yazı rengi
            bordercolor='#3b3b3b',      # Kenarlık rengi
            borderwidth=1,
            font=('Arial', 10, 'bold'), # Yazı tipi
            cursor='hand2'              # Fare imleci
            )
        self.calendar.place(x=1000, y=25,width=350)

        self.label4 = ctk.CTkLabel(self.form,text="Görevleriniz :")
        self.label4.place(x=30,y=25)
        def on_combobox_select(choice):
            if choice == "Güncel Görevleriniz":
                for _,frame in self.item_frames:
                    frame.destroy()
                self.item_frames = []
                self.item_buttons = []
                vericekimi = supabase.table("Missions").select("*").eq("UserId", self.id).gte("MissionDate",formatted).execute().data
                liste = []
                for mission in vericekimi:
                    print((mission['MissionId'], mission['MissionName'], mission['MissionTime']))
                    liste.append((mission['MissionId'], mission['MissionName'], mission['MissionTime']))
                self.items=liste
                for item in self.items:
                    add_item_to_listbox(item)
            elif choice =="Geçmiş Görevleriniz":
                for _,frame in self.item_frames:
                    frame.destroy()
                vericekimi = supabase.table("Missions").select("*").eq("UserId", self.id).lt("MissionDate",formatted).execute().data
                liste = []
                for mission in vericekimi:
                    print((mission['MissionId'], mission['MissionName'], mission['MissionTime']))
                    liste.append((mission['MissionId'], mission['MissionName'], mission['MissionTime']))
                self.items=liste
                self.item_frames = []
                self.item_buttons = []
                for item in self.items:
                    add_item_to_listbox(item)
        screnn_options = ["Güncel Görevleriniz","Geçmiş Görevleriniz"]
        self.combo3 = ctk.CTkComboBox(self.form,values=screnn_options,command=on_combobox_select)
        self.combo3.place(x=110,y=25)
        
        self.label5 = ctk.CTkLabel(self.form,text="Bugünün Görevlerini")
        self.label5.place(x=380,y=25)
        
        self.label1 = ctk.CTkLabel(self.form, text="Görev Adı :")
        self.label1.place(x=830, y=220)
        
        self.entry1 = ctk.CTkEntry(self.form, width=250, placeholder_text="Görev Adı")
        self.entry1.place(x=900, y=220)

        self.label2 = ctk.CTkLabel(self.form, text="Görev Acıklama :")
        self.label2.place(x=795, y=270)
        
        self.entry2 = ctk.CTkEntry(self.form, width=250, placeholder_text="Görev Acıklaması")
        self.entry2.place(x=900, y=270)

        self.label3 = ctk.CTkLabel(self.form, text="Muzik :")
        self.label3.place(x=850, y=320)
        
        music_options = ["Davul Sesi", "Piano Sesi", "Çalar Saat"]
        self.combo = ctk.CTkComboBox(self.form, values=music_options, width=250)
        self.combo.place(x=900, y=320)

        remember_options = ["10 dakika kala", "30 dakika kala", "1 saat kala", "2 saat kala","1 gün kala"]
        self.combo2 = ctk.CTkComboBox(self.form, values=remember_options, width=250)
        self.combo2.place(x=900, y=410)

        self.label6 = ctk.CTkLabel(self.form, text="Hatırlatma Zamanı :")
        self.label6.place(x=780, y=410)

        self.time_label = ctk.CTkLabel(self.form, text="Zaman:")
        self.time_label.place(x=845, y=370)
        
        self.hour_spinbox = ctk.CTkEntry(self.form, width=50, placeholder_text="HH")
        self.hour_spinbox.place(x=900, y=370)
        
        self.minute_spinbox = ctk.CTkEntry(self.form, width=50, placeholder_text="MM")
        self.minute_spinbox.place(x=955, y=370)
        self.label7 = ctk.CTkLabel(self.form,text="")
        self.label7.place(x=950,y=500)
        self.button = ctk.CTkButton(
            self.form,
            text="Görev Ekle",
            command=add_mission,
            width=250,
            height=40,
            corner_radius=8
        )
        self.button.place(x=900, y=450)         
        self.form.mainloop()
