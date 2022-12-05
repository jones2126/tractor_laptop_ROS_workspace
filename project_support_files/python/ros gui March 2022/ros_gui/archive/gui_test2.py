"""A better Hello World for Tkinter"""

import tkinter as tk
from tkinter import ttk
import subprocess
import time
'''
issues: 
NameError: name 'RPi_login_steps' is not defined
'''

class HelloView(tk.Frame):
    """A friendly little module"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.name = tk.StringVar()
        self.title_string = tk.StringVar()
        self.title_string.set("Lawn Tractor Startup")

        name_label = ttk.Label(self, text="Step1:")
        name_entry = ttk.Entry(self, textvariable=self.name)
        step_1_button = ttk.Button(self, text="Step_1", command=self.on_change)
        title_label = ttk.Label(self, textvariable=self.title_string, font=("TkDefaultFont", 18), wraplength=400)

        # Layout form
        title_label.grid(row=0, column=0, columnspan=2)
        self.columnconfigure(0, weight=1)        
        name_label.grid(row=1, column=0, sticky=tk.W)
        name_entry.grid(row=1, column=1, sticky=(tk.W + tk.E))
        step_1_button.grid(row=1, column=2, sticky=tk.E)

    def RPi_login_steps(self):
        time.sleep(2)
        cmd_RPi_login = "plink RPI_on_ZeroTier -pw ubuntu"  # command to login to RPi
        time.sleep(.1)
        subprocess.check_output(["xdotool", "type", cmd_RPi_login + "\n"])
        time.sleep(5) # delay for the login process to the RPi
        subprocess.check_output(["xdotool", "type", "\n"])
        time.sleep(.5)


    def on_change(self):
        """Handle Change button clicks"""
        working_directory1 = "--working-directory=/home/al"
        subprocess.call(["xdotool", "exec", "gnome-terminal", "--geometry=50x20+450+200", working_directory1])
        self.RPi_login_steps()


class MyApplication(tk.Tk):
    """Hello World Main Application"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window properties
        self.title("ROS GUI")
        self.geometry("600x400")
        self.resizable(width=False, height=False)

        # Define the UI
        HelloView(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()