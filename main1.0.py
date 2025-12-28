from customtkinter import *
from PIL import Image
import socket 
import threading

#створи картинки CTKImage
FON = CTkImage(light_image=Image.open("fon.png"),size=(350,400))#fon 350,400
CONF = CTkImage(light_image=Image.open("conf.png"),size=(20,20))#conf 20,20
USER = CTkImage(light_image=Image.open("user.png"),size=(20,20))#user 20,20
ICONS = [] #user icons 20,20
for i in range(7):
    ICONS.append(CTkImage(light_image=Image.open(f"{i}.png"),size=(85,85)))

#кольори
BLUE= "#5D89EA"
CYAN = "#2EB3E4"
PURPULE = "#B43EF5"
MEDIUMBLUE = "#8D60F0"
PHLOX = "#EB0EFC"

class MyLbl(CTkLabel):
    def __init__(self, master, text , size=16,image=None):
        super().__init__(master=master,text=text,
                         font=("arial",size,"bold"),
                         text_color="white", image=image)

class MyBtn(CTkButton):
    def __init__(self, master=None, w = 150, h = 40,text = "CTkButton", command = None, image=None):
        super().__init__(master=master,text=text,width=w,height=h,
                         image=image,command=command,
                         font=("arial",16,"bold"),text_color="white",
                         fg_color=CYAN,hover_color=MEDIUMBLUE,corner_radius=15)

class Mess(CTkLabel):
    def __init__(self, master, user, icon, text, anchor ):
        icon = CTkImage(light_image=Image.open(f"{icon}.png"),size=(25,25))

        super().__init__(master=master,fg_color="#711b72",
                         text_color="white",font=("Arial",14),
                         image=icon,compound="left",
                         corner_radius=25,
                         padx=10,pady=10,text=f"{user}: {text}")
        self.pack(padx=50,pady=2,anchor=anchor)






class App(CTk):
    def __init__(self):
        super().__init__()
        self.USER = "ananim"
        self.ICON = 0
        self.HOST = "0"
        self.PORT = 8080
        self.geometry("600x400")
        self.configure(fg_color="#7a6c77")
        self.title("logiktolk")
        self.iconbitmap("icon.ico")
        self.resizable(False,False)

        self.lbl = MyLbl(self,text="WELCOM",size=40,image=FON)
        self.lbl.place(x=0,y=0)

        lbl2=MyLbl(self,text="logiktolk",size=25)
        lbl2.configure(text_color=PHLOX)
        lbl2.place(x=430,y=50)

        self.btn_name = MyBtn(self,text="mame",image=USER, command=self.open_name)
        self.btn_name.place(x=400,y=150)

        self.btn_icon= MyBtn(self,text="icon",image=CONF, command=self.open_icon)
        self.btn_icon.place(x=400,y=200)

        self.btn_chat= MyBtn(self,text="chat",command=self.open_chat)
        self.btn_chat.configure(fg_color=PHLOX)
        self.btn_chat.place(x=400,y=280)

        self.frame_name = CTkFrame(self,width=350,height=400,fg_color="#daaddb")
        self.frame_name.place(x=-350,y=0)

        lbl3 = MyLbl(self.frame_name,text="enter your name",size=20)
        lbl3.place(x=80,y=100)
        self.box_name = CTkEntry(self.frame_name,width=250,height=50,fg_color=BLUE,
                                 corner_radius=25)
        self.box_name.place(x=50,y=150)
        self.btn_save_name = MyBtn(self.frame_name,text="save name",command=self.seve_name)
        self.btn_save_name.place(x=100,y=220)

        self.frame_icon = CTkFrame(self,width=350,height=400,fg_color="#daaddb")
        self.frame_icon.place(x=-350,y=0)
        c,r = 0,0
        for i in range(7):
            if i%2==0:
               c +=1
            else:
               c=0
            btn = MyBtn(self.frame_icon,text = "",image=ICONS[i],
                        w=80,h=80,command=lambda i=i: self.seve_icon(i))
            
            btn.grid(row=int(r), column=c,padx=23,pady=20)
            
            r +=0.5

        self.frame_chat = CTkFrame(self,width=600,height=400,fg_color="#711b72")  

        self.frame_chat.place(x=0,y=-400)
        self.all_mess = CTkScrollableFrame(self.frame_chat,fg_color="#711b72", width=580,height=300)
        self.all_mess.place(x=0,y=0)

        self.inp_mess = CTkTextbox(self.frame_chat,width=350,height=50,fg_color=BLUE,corner_radius=25)
        self.inp_mess.place(x=20,y=320)
        self.btn_send_mess = MyBtn(self.frame_chat,text="send",w=100,h=50,command=self.send_mess)
        self.btn_send_mess.place(x=420,y=320)

        self.frame_start = CTkFrame(self,width=600,height=400,fg_color="#7a6c77")
        self.frame_start.place(x=0,y=0)
        self.frame_start.place(x=0,y=0)
        self.box_port = CTkEntry(self.frame_start,width=250,height=50,fg_color=BLUE,
                                 corner_radius=25,placeholder_text="port")
        self.box_port.place(x=100,y=150)
        self.box_host = CTkEntry(self.frame_start,width=250,height=50,fg_color=BLUE,
                                 corner_radius=25,placeholder_text="port")
        self.box_host.place(x=100,y=220)
        
        self.btn_begin = MyBtn(self.frame_start,text="begin",w=100,h=50,command=self.begin)
        self.btn_begin.place(x=420,y=320)

    def begin(self):
        self.PORT = int(self.box_port.get())
        self.HOST = int(self.box_host.get())
        self.frame_start.destroy()

    def start(self):
        self.HOST = self.int_host.get()
        self.PORT = int(self.input_port.get())
        self.frame_start.destroy()
    def open_name(self):

        self.new_x=-350
        def anime():
            self.new_x += 10
            self.frame_name.place(x=self.new_x,y=0)
            if self.new_x <0:
                self.after(10,anime)
        anime()
    def close_name(self):
        self.new_x=0
        def anime():
            self.new_x -=10
            self.frame_name.place(x=self.new_x,y=0)
            if self.new_x >-350:
                self.after(10,anime)
        anime()

    def open_icon(self):
        self.new_x=-350
        def anime():
            self.new_x += 10
            self.frame_icon.place(x=self.new_x,y=0)
            if self.new_x <0:
                self.after(10,anime)
        anime()
    def close_icon(self):
        self.new_x=0
        def anime():
            self.new_x -=10
            self.frame_icon.place(x=self.new_x,y=0)
            if self.new_x >-350:
                self.after(10,anime)
        anime()
    
    def seve_name(self):
        self.USER = self.box_name.get()
        print(self.USER)
        self.close_name()

    def seve_icon(self,i):
        self.ICON = i
        self.close_icon()

    def open_chat(self):
        try:
                
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((f"{self.HOST}.tcp.eu.ngrok.io", self.PORT))
                self.sock.send(f"{self.USER}|{self.ICON}".encode())
                Mess(self.all_mess,self.USER,self.ICON,"hello",anchor="w")
                input=threading.Thread(target=self.input_mess, daemon=True)
                input.start()
                self.new_y=-400
                def anime():
                    self.new_y += 10
                    self.frame_chat.place(x=0,y=self.new_y)
                    if self.new_y <0:
                        self.after(10,anime)
                anime()
        except:
            self.lbl.configure(text="error")

    def input_mess(self):
      while True:
          try:
            mess = self.sock.recv(1024).decode()
            user, icon, = mess.split("|")
            Mess(self.all_mess,user,icon,mess,"e")

          except:
              Mess(self.all_mess,"server",0,"be") 
              self.after(1000, self.close)
    def close(self):
        self.sock.close()
        self().destroy()

    def send_mess(self):
        mess = self.inp_mess.get("1.0","end").strip()
        self.inp_mess.delete("1.0","end")
        try:
            self.sock.send(mess.encode())
            Mess(self.all_mess,self.USER,self.ICON,mess,"w")
        except:
              Mess(self.all_mess,"server",0,"be") 
              self.after(1000, self.close)

app = App()
app.mainloop()