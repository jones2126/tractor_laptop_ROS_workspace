#!/usr/bin/env python
from Tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
    def init_window(self):
    	self.master.title("Hello_World_GUI")
        #canvas1 = tk.Canvas(root, width=600, height=500, bg='gray90', relief='raised')
        self.canvas1 = Canvas(master, width=600, height=500, bg='gray90', relief='raised')
        self.canvas1.pack(side='left')
        #canvas2 = tk.Canvas(root, width=400, height=500, bg='gray90', relief='raised')
        self.canvas2 = Canvas(master, width=400, height=500, bg='gray90', relief='raised')
        self.canvas2.pack(side='right')
        self.canvas1.create_window(151, buttonx_orig, window=buttonA)


def main():
	root = Tk() # initialize tkinter
	app = Window(root)
	root.wm_title("Tkinter window") # set window title
	#canvas1.create_window(151, buttonx_orig, window=buttonA)
	root.mainloop() # show window

if __name__ == '__main__':
    main()