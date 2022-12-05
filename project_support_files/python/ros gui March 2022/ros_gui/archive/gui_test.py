from tkinter import *
from threading import Thread
from time import sleep
from random import randint
import subprocess
import time

windowid1 = ''

class GUI():

    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root)
        self.frame.pack()
        self.root.geometry("200x200")
        self.frame0 = Frame(frame)
        self.frame01 = Frame(frame,borderwidth=2,relief=RAISED)
        self.frame1 = Frame(frame)
        self.frame2 = Frame(frame)
        self.frame3 = Frame(frame)
        self.frame4 = Frame(frame)        

        self.btn1 = Button(self.root,text="launch1")
        self.btn1.pack(expand=True)
        self.btn1.config(command=self.action1)
        self.btn2 = Button(self.root,text="launch2")
        self.btn2.pack(expand=True)
        self.btn2.config(command=self.action2)

    def run(self):
        self.root.mainloop()

    def add(self,string,buffer):
        while  self.txt:
            msg = str(randint(1,100))+string+"\n"
            self.txt.insert(END,msg)
            sleep(0.5)

    def reset_lbl(self):
        self.txt = None
        self.second.destroy()

    def action1(self):
        self.second = Toplevel()
        self.second.geometry("100x100")
        self.txt = Text(self.second)
        self.txt.pack(expand=True,fill="both")
        self.t = Thread(target=self.add,args=("new",None))
        self.t.setDaemon(True)
        self.t.start()
        self.second.protocol("WM_DELETE_WINDOW",self.reset_lbl)
    def action2(self):
        working_directory1 = "--working-directory=/home/al"
        subprocess.call(["xdotool", "exec", "gnome-terminal", "--geometry=50x20+450+200", working_directory1])
        time.sleep(.1)
      

a = GUI()
a.run()