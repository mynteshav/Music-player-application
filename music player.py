from tkinter import *
from PIL import Image,ImageTk
class Music_Player:
    def __init__(self,root):
        self.root=root
        self.root.title("Teshav Music Player")
        self.root.geometry("424x599+480+40")
        self.root.resizable(False,False)
        self.root.config(bg="#262626")
        
        self.logo_icon=ImageTk.PhotoImage(file="logo.gif")
        self.mute_icon=Image.open("mute.png")
        self.mute_icon = self.mute_icon.resize((30, 30), Image.LANCZOS)
        self.mute_icon = ImageTk.PhotoImage(self.mute_icon)
        #self.mute_icon=ImageTk.PhotoImage(file="mute.png")
        self.unmute_icon=Image.open("unmute.png")
        self.unmute_icon = self.unmute_icon.resize((30, 30), Image.LANCZOS)
        self.unmute_icon=ImageTk.PhotoImage(self.unmute_icon)
        self.prev_icon=ImageTk.PhotoImage(file="prev.png")
        self.next_icon=ImageTk.PhotoImage(file="next.png")
        self.play_icon=ImageTk.PhotoImage(file="play.png")
        self.pause_icon=ImageTk.PhotoImage(file="pause.png")
        self.loop_icon=ImageTk.PhotoImage(file="loop.png")
        self.shuffle_icon=ImageTk.PhotoImage(file="shuffle.png")
        
        self.lbl_mute=Label(self.root,image=self.mute_icon,bd=0).place(x=20,y=10)
        self.lbl_unmute=Label(self.root,image=self.unmute_icon,bd=0).place(x=370,y=10)
        self.volume=Label(self.root,bg='white')
        self.volume.place(x=70,y=25,width=280,height=5)
    
        hr=Label(self.root,bg='lightgray').place(x=0,y=65,relwidth=1,height=1)
    
    
    
root=Tk()
obj=Music_Player(root)
root.mainloop()
