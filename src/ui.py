from tkinter import *
from PIL import ImageTk, Image


class Login():

    image_sizes = [(50, 34), (60, 34), (50, 34), (50, 34), (62, 34),
                   (50, 34), (45, 34), (50, 34), (52, 34), (50, 34),
                   (55, 34), (45, 34), (45, 34), (45, 34), (45, 34)]

    def __init__(self, username):
        """
        set tkinter root, windowsize, and title

        Args:
            username (list): send username from main by reference to return back
        """
        while(username != []):
            username.pop()
        self.username = username
        self.root = Tk()
        self.root.geometry('480x570+720+255')
        self.root.title("SlimeAdventure 2.0")
        self.root.resizable(0, 0)
        self.skinid = 1

        canvas = Canvas(self.root, height=600, width=1000, bg="pink")
        canvas.place(x=0, y=0)
        canvas = Canvas(self.root, height=240, width=300, bg="lightblue")
        canvas.place(x=90, y=30)

        self.sprites = []
        for i in range(1, 16):
            name = f"src/photo/player{i}.png"
            photo = Image.open(name).copy()
            photo = photo.resize(Login.image_sizes[i-1], Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(photo)
            self.sprites.append(photo)
        self.showimg = Label(
            self.root, image=self.sprites[self.skinid-1], bg="lightblue")
        self.showimg.place(x=200, y=110)

        self.inputusername = Label(self.root, text="Username:", font=(
            "bold", 12), fg='black', bg='lightblue')
        self.inputusername.place(x=150, y=50)
        self.entry_name = Entry(self.root, width=30)
        self.entry_name.place(x=150, y=80)
        self.BCheck = Button(self.root, text="GoPlay",
                             command=self.get, width=25, height=3)
        self.BCheck.place(x=150, y=200)

        self.warning = Label(
            self.root, text="length of username must less than 8", font=("", 8), fg='red', bg='lightblue')
        self.warning.place(x=150, y=155)
        self.warning = Label(
            self.root, text="and not be empty.", font=("", 8), fg='red', bg='lightblue')
        self.warning.place(x=150, y=172)

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
            button[0].place(x=65+75*button[2], y=300+60*button[1])

    def get(self):
        """
        function to get username from entry and detect
        if length of username is >= 6 or username is empty
        function will warn user then hide and quit ui
        """
        if len(self.entry_name.get()) > 8 or self.entry_name.get() == "":
            self.entry_name.delete(0, END)
            return None
        self.username.append(self.entry_name.get())
        self.username.append(self.skinid)
        self.entry_name.delete(0, END)
        self.root.quit()
        self.hide()

    def hide(self):
        """
        hide ui
        """
        self.root.update()
        self.root.withdraw()
        self.root.update()

    def show(self):
        """
        reset username and show window by draw() function
        """
        while(self.username != []):
            self.username.pop()
        self.root.update()
        self.root.deiconify()
        self.root.mainloop()
