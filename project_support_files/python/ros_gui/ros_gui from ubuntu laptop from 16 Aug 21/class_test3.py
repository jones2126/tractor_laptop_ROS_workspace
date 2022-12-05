#! /usr/bin/env python
 
import tkinter as tk
import time
 
class Event(object):
    """ Event Class for timing repetitive events. """
 
    event_list = []
 
    def __init__(self, name, interval, method_to_call):
        self.name = name
        self.interval = interval # The time delay (in seconds) between subsequent triggers of this event.
        self.method_to_call = method_to_call # The function to be executed when this event is triggered.
        self.init_time = time.time() # Keep the timestamp of when the event was initialized for later use.
        self.last_time = self.init_time
        Event.event_list.append(self)
 
    def __str__(self):
        return f"EVENT -- Name: {self.name}, Interval: {self.interval}, Method Called: {self.method_to_call.__name__}."
 
    def check_event_ready(self):
        """ Test whether an event interval has elapsed and it's ready to run again. """
 
        if time.time() - self.last_time >= self.interval:
            self.last_time = time.time()
            return True
        else:
            return False
 
 
class App():
    def __init__(self):
        self.root = tk.Tk()
 
        self.event_listbox = tk.Listbox(width=50, height=25)
        self.event_listbox.pack()
 
        self.status_listbox = tk.Listbox(width=50, height=5)
        self.status_listbox.pack()
 
        self.setup() # Load up the Events to run.
        self.run_events() # Start the Event checking loop.
        self.root.mainloop() # Start the Tk GUI.
 
    def setup(self):
        """ Setup the events with their interval timing and function to execute. """
 
        ev1 = Event("Collect Data", 2, self.collect_data)
        ev2 = Event("Update Network", 5, self.update_network)
        for e in Event.event_list:
            print(e)
 
#####################################################################################################################
    def run_events(self):
        """ Spins a fast loop (using Tk.root.after()) to constantly check whether it's time to trigger an event. """
 
        for event in Event.event_list:
            if event.check_event_ready():
                self.event_listbox.insert(tk.END, event.name)
                event.method_to_call ### HOW DO I CALL THIS METHOD???
                print(event.method_to_call.__name__) # It prints just fine.
######################################################################################################################
 
        self.root.after(10, self.run_events) # Repeat at 10mS resolution.
 
    def collect_data(self):
        self.status_listbox.insert(tk.END, "Collect Data Running")
        time.sleep(500) # Add time delay to see if I need to use threading.
 
    def update_network(self):
        self.status_listbox.insert(tk.END, "Update Network Running")
        time.sleep(500)
 
app = App()