import tkinter as tk
import datetime
import ctypes

class Countdown(tk.Frame):
    '''A Frame with label to show the time left, an entry to input the seconds to count
    down from, and a start button to start counting down.'''
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 0
        self._timer_on = False


    def show_widgets(self):

        self.label.grid(column=1, row=0)
        # self.entry.pack()
        # self.start.pack()
        # self.start_break.pack(side='bottom', expand=1, anchor='s')
        # self.stop.pack(side='bottom', expand=1, padx=0, pady=0, ipadx=0, ipady=0, anchor='se')
        self.start.grid(column=0, row=1)
        self.stop.grid(column=2, row=1)
        self.start_break.grid(column=1, row=1)


    def create_widgets(self):

        self.label = tk.Label(self, text="00:00:00")
        self.label.config(font=("Courier 60"))
        # self.entry = tk.Entry(self, justify='center')
        # self.entry.focus_set()
        self.start = tk.Button(self, text="Start", command=self.start_button, font=('Courier 16'))
        self.start_break = tk.Button(self, text="Start 15", command=self.start_fifteen, font=('Courier 16'))
        self.stop = tk.Button(self, text="Stop", command=self.stop_timer, font=('Courier 16'))

    def countdown(self):
        '''Update label based on the time left.'''
        self.label['text'] = self.convert_seconds_left_to_time()

        if self.seconds_left:
            self.seconds_left -= 1
            self._timer_on = self.after(1000, self.countdown)
        else:
            self._timer_on = False
            ctypes.windll.user32.MessageBoxW(0, "Time is up.", "Time is up.", 0x40000)

    def start_button(self):
        '''Start counting down.'''
        # self.seconds_left = 900   # 1. to fetch the seconds
        self.stop_timer()                           # 2. to prevent having multiple
        self.countdown()                            #    timers at once

    def start_fifteen(self):
        self.seconds_left = 900
        self.stop_timer()
        self.countdown()

    def stop_timer(self):
        '''Stops after schedule from executing.'''
        if self._timer_on:

            self.after_cancel(self._timer_on)
            self._timer_on = False


    def convert_seconds_left_to_time(self):

        return datetime.timedelta(seconds=self.seconds_left)


if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Time")
    root.attributes("-topmost", True)
    countdown = Countdown(root)
    countdown.pack()



    root.mainloop()
