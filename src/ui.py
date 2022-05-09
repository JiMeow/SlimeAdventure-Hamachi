from tkinter import *
from PIL import ImageTk, Image
import webbrowser
import pygame
from pygame.locals import *


class Login():

    image_sizes = [(50, 34), (60, 34), (50, 34), (50, 34), (62, 34),
                   (50, 34), (45, 34), (50, 34), (52, 34), (50, 34),
                   (55, 34), (45, 34), (45, 34), (45, 34), (45, 34)]

    def __init__(self, data):
        '''It creates a window and binds the key_pressed function to the window.

        Parameters
        ----------
        data
            a list of all the data from the database

        '''
        while(data != []):
            data.pop()
        self.data = data
        self.root = Tk()
        self.root.geometry('480x570+720+255')
        self.root.title("SlimeAdventure 2.0")
        self.root.resizable(0, 0)
        self.skinid = 1
        self.difficult = 5  # 0 for easy, 1 for normal, 2 for hard, 3 for very hard
        self.sprites = []
        self.soundstatus = 1
        for i in range(1, 16):
            name = f"src/photo/player{i}.png"
            photo = Image.open(name).copy()
            photo = photo.resize(Login.image_sizes[i-1], Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(photo)
            self.sprites.append(photo)

        checkbox = Image.open("src/photo/checkbox.png").copy()
        self.checkboximg = ImageTk.PhotoImage(
            checkbox.resize((50, 50), Image.ANTIALIAS))
        check = Image.open("src/photo/check.png").copy()
        self.checkimg = ImageTk.PhotoImage(
            check.resize((30, 30), Image.ANTIALIAS))
        self.sound = []
        soundoff = Image.open("src/photo/soundoff.png").copy()
        self.sound.append(ImageTk.PhotoImage(
            soundoff.resize((30, 30), Image.ANTIALIAS)))
        soundon = Image.open("src/photo/soundon.png").copy()
        self.sound.append(ImageTk.PhotoImage(
            soundon.resize((30, 30), Image.ANTIALIAS)))

        self.root.iconphoto(False, self.sprites[13])
        self.root.bind("<Key>", self.key_pressed)

    def menu(self):
        '''It creates a menu for the game.

        '''
        canvas = Canvas(self.root, height=600, width=1000, bg="lightblue")
        canvas.place(x=0, y=0)

        self.BSound = Button(self.root, image=self.sound[self.soundstatus], bg='lightblue', font=(
            "bold", 10), fg='black', command=self.changeSoundStatus, borderwidth=0, activebackground="lightblue")
        self.BSound.place(x=430, y=515)
        self.gamename = Label(self.root, text="SlimeAdventure", font=(
            "bold", 40), fg='black', bg='lightblue')
        self.gamename.place(x=55, y=20)
        self.vername = Label(self.root, text="2.0", font=(
            "bold", 20), fg='black', bg='lightblue')
        self.vername.place(x=220, y=90)
        self.icon = Label(self.root, image=self.sprites[0], bg="lightblue")
        self.icon.place(x=150, y=160)
        self.icon = Label(self.root, image=self.sprites[1], bg="lightblue")
        self.icon.place(x=205, y=160)
        self.icon = Label(self.root, image=self.sprites[2], bg="lightblue")
        self.icon.place(x=270, y=160)
        self.BPlay = Button(self.root, text="play", width=25, height=3, bg='pink', font=(
            "", 10), command=lambda: self.play(None))
        self.BPlay.place(x=135, y=240)
        self.BSetting = Button(self.root, text="setting", width=25, height=3, bg='pink', font=(
            "", 10), command=self.setting)
        self.BSetting.place(x=135, y=320)
        self.BBeta = Button(self.root, text="credit", width=25, height=3, bg='pink', font=(
            "", 10), command=self.open_browser)
        self.BBeta.place(x=135, y=400)
        self.BQuit = Button(self.root, text="quit", width=25, height=3, bg='pink', font=(
            "", 10), command=self.root.quit)
        self.BQuit.place(x=135, y=480)

    def setting(self):
        '''It creates a canvas, and then creates a label and a button for each difficulty level. 
        The button is a checkbox, and the label is the name of the difficulty level. 
        The function also creates a label that explains the difficulty level, and a checkmark that shows
        which difficulty level is selected.

        '''
        canvas = Canvas(self.root, height=600, width=1000, bg="lightblue")
        canvas.place(x=0, y=0)

        Bback = Button(self.root, text=" <- back ", bg='lightblue', font=(
            "bold", 10), fg='black', command=self.menu, borderwidth=0)
        Bback.place(x=10, y=10)
        self.difficulttext = Label(self.root, text="Difficultity", font=(
            "bold", 45), fg='black', bg='lightblue')
        self.difficulttext.place(x=110, y=50)
        self.easy = Label(self.root, text="Easy", font=(
            "bold", 30), fg='black', bg='lightblue')
        self.easy.place(x=180, y=200)
        self.Beasy = Button(self.root, image=self.checkboximg, bg="lightblue",
                            borderwidth=0, activebackground="lightblue", command=lambda: self.change_difficult(0))
        self.Beasy.place(x=100, y=200)

        self.normal = Label(self.root, text="Nomal", font=(
            "bold", 30), fg='black', bg='lightblue')
        self.normal.place(x=180, y=280)
        self.Bnormal = Button(self.root, image=self.checkboximg, bg="lightblue",
                              borderwidth=0, activebackground="lightblue", command=lambda: self.change_difficult(1))
        self.Bnormal.place(x=100, y=280)

        self.hard = Label(self.root, text="Hard", font=(
            "bold", 30), fg='black', bg='lightblue')
        self.hard.place(x=180, y=360)
        self.Bhard = Button(self.root, image=self.checkboximg, bg="lightblue",
                            borderwidth=0, activebackground="lightblue", command=lambda: self.change_difficult(2))
        self.Bhard.place(x=100, y=360)

        self.insane = Label(self.root, text="Insane", font=(
            "bold", 30), fg='black', bg='lightblue')
        self.insane.place(x=180, y=440)
        self.Binsane = Button(self.root, image=self.checkboximg, bg="lightblue",
                              borderwidth=0, activebackground="lightblue", command=lambda: self.change_difficult(3))
        self.Binsane.place(x=100, y=440)

        if self.difficult == 1:
            self.explain = Label(self.root, text="Check point on every stage", font=(
                "", 14), fg='red', bg='lightblue')
            self.explain.place(x=100, y=150)
            self.check = Label(self.root, image=self.checkimg, bg="lightblue")
            self.check.place(x=110, y=210)
        if self.difficult == 5:
            self.explain = Label(self.root, text="Check point on every 5 stages", font=(
                "", 14), fg='red', bg='lightblue')
            self.explain.place(x=100, y=150)
            self.check = Label(self.root, image=self.checkimg, bg="lightblue")
            self.check.place(x=110, y=290)
        if self.difficult == 10:
            self.explain = Label(self.root, text="Check point on every 10 stages", font=(
                "", 14), fg='red', bg='lightblue')
            self.explain.place(x=100, y=150)
            self.check = Label(self.root, image=self.checkimg, bg="lightblue")
            self.check.place(x=110, y=370)
        if self.difficult == 30:
            self.explain = Label(self.root, text="Check point on every 20 stages", font=(
                "", 14), fg='red', bg='lightblue')
            self.explain.place(x=100, y=150)
            self.check = Label(self.root, image=self.checkimg, bg="lightblue")
            self.check.place(x=110, y=450)

    def play(self, log):
        '''It creates a GUI with a username and password entry, a button to submit the username and
        password, and a grid of buttons to select a skin.

        Parameters
        ----------
        log
            the log of the last game

        '''
        canvas = Canvas(self.root, height=600, width=1000, bg="pink")
        canvas.place(x=0, y=0)
        canvas = Canvas(self.root, height=290, width=300, bg="lightblue")
        canvas.place(x=90, y=30)
        Bback = Button(self.root, text=" <- back ", bg='pink', font=(
            "bold", 10), fg='black', command=self.menu, borderwidth=0)
        Bback.place(x=10, y=10)
        self.showimg = Label(
            self.root, image=self.sprites[self.skinid-1], bg="lightblue")
        self.showimg.place(x=200, y=165)

        self.inputusername = Label(self.root, text="Username:", font=(
            "bold", 12), fg='black', bg='lightblue')
        self.inputusername.place(x=150, y=50)
        self.entry_username = Entry(self.root, width=30)
        self.entry_username.place(x=150, y=80)
        self.inputusername = Label(self.root, text="Password:", font=(
            "bold", 12), fg='black', bg='lightblue')
        self.inputusername.place(x=150, y=105)
        self.entry_password = Entry(self.root, width=30, show="*")
        self.entry_password.place(x=150, y=135)

        self.BCheck = Button(self.root, text="GoPlay",
                             command=self.get, width=25, height=3)
        self.BCheck.place(x=150, y=255)
        self.warning1 = Label(
            self.root, text="length of username must less than 8", font=("", 8), fg='red', bg='lightblue')
        self.warning1.place(x=150, y=210)
        self.warning2 = Label(
            self.root, text="and not be empty.", font=("", 8), fg='red', bg='lightblue')
        self.warning2.place(x=150, y=227)

        self.buttonlist = []

        def setshowimg(event):
            self.skinid = event.widget.cget("text")
            self.showimg.config(image=self.sprites[int(self.skinid)-1])

        for i in range(3):
            for j in range(5):
                button = Button(self.root, text=i*5+j+1, image=self.sprites[i*5+j], bg="pink",
                                borderwidth=0, activebackground="pink")
                button.bind("<Button-1>", setshowimg)
                self.buttonlist.append([button, i, j])

        for button in self.buttonlist:
            button[0].place(x=65+75*button[2], y=350+60*button[1])

        if log is not None:
            self.warning1.config(text=log[:-8])
            self.warning2.config(text=log[-8:])

    def get(self):
        """
        function to get username from entry and detect
        if length of username is >= 6 or username is empty
        function will warn user then hide and quit ui
        """
        if len(self.entry_username.get()) > 8 or self.entry_username.get() == "":
            self.entry_username.delete(0, END)
            self.warning1.config(text="length of username must less than 8")
            self.warning2.config(text="and not be empty")
            return None
        self.data.append(self.entry_username.get())
        self.data.append(self.entry_password.get())
        self.data.append(self.skinid)
        self.data.append(self.difficult)
        self.data.append(self.soundstatus)
        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)
        self.root.withdraw()
        self.root.quit()

    def show(self, log=None):
        """
        reset username and show window by draw() function
        """

        pygame.mixer.init()
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.2)

        while(self.data != []):
            self.data.pop()
        self.root.deiconify()
        if log is not None:
            self.play(log)
        else:
            self.menu()
        # self.setting()
        self.root.mainloop()

    def key_pressed(self, event):
        '''If the user presses the escape key, the menu function is called.

        Parameters
        ----------
        event
            The event that was triggered.

        '''
        if event.keysym == "Escape":
            self.menu()

    def change_difficult(self, val):
        '''The function changes the difficult of the game

        Parameters
        ----------
        val
            the value of the button that was clicked

        '''
        if val == 0:
            self.check.place_configure(x=110, y=210)
            self.explain.configure(text="Check point on every stage")
            self.difficult = 1
        if val == 1:
            self.check.place_configure(x=110, y=290)
            self.explain.configure(text="Check point on every 5 stages")
            self.difficult = 5
        if val == 2:
            self.check.place_configure(x=110, y=370)
            self.explain.configure(text="Check point on every 10 stages")
            self.difficult = 10
        if val == 3:
            self.check.place_configure(x=110, y=450)
            self.explain.configure(text="Check point on every 30 stages")
            self.difficult = 30

    def open_browser(self):
        webbrowser.open("https://github.com/jiratQ")  # Go to example.com

    def changeSoundStatus(self):
        self.soundstatus = 1 - self.soundstatus
        self.BSound.configure(image=self.sound[self.soundstatus])
        if self.soundstatus == 0:
            pygame.mixer.music.set_volume(0)
        else:
            pygame.mixer.music.set_volume(0.2)
