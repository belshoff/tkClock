from tkinter import Tk, Label, StringVar, Frame
from datetime import datetime
from threading import Event
from job import Job


class Clock():
    def __init__(self, win):
        self.win = win
        self.time = StringVar()
        self.event = Event()

        self.__update__()

        win.title("tkClock")
        win.geometry('500x200')

        container = Frame(
            self.win,
            height=200,
            width=500,
            bg="#000000"
        )
        container.pack()

        clock_label = Label(
            container,
            textvariable=self.time,
            font=("Press Start 2P", 80),
            bg="#000000",
            fg="#FFFFFF",
            borderwidth=2,
            relief="ridge",
            justify="center",
            height=150,
            width=450
        )
        clock_label.pack(padx=10, pady=10)

        Job(self.__update__, self.event, 1).start()

    def __update__(self):
        current = str(datetime.now().time())[:8]
        hour, minutes, seconds = current.split(':')
        separator = ':' if int(seconds)%2 == 0 else ' '
        self.time.set(f"{hour}{separator}{minutes}")
    