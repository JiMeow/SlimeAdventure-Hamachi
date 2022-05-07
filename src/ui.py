from tkinter import *
from PIL import ImageTk, Image


class Login():

    image_sizes = [(50, 34), (60, 34), (50, 34), (50, 34), (62, 34),
                   (50, 34), (45, 34), (50, 34), (52, 34), (50, 34),
                   (55, 34), (45, 34), (45, 34), (45, 34), (45, 34)]

    def __init__(self, data):
        """
        set tkinter root, windowsize, and title

        Args:
            data (list): send data from main by reference to return back
        """
        while(data != []):
            data.pop()
        self.data = data
        self.root = Tk()
        self.root.geometry('480x570+720+255')
        self.root.title("SlimeAdventure 2.0")
        self.root.resizable(0, 0)
        self.skinid = 1

        
    def play(self, log):
        canvas = Canvas(self.root, height=600, width=1000, bg="pink")
        canvas.place(x=0, y=0)
        canvas = Canvas(self.root, height=290, width=300, bg="lightblue")
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
        self.showimg.place(x=200, y=165)

        self.inputusername = Label(self.root, text="Username:", font=(
            "bold", 12), fg='black', bg='lightblue')
        self.inputusername.place(x=150, y=50)
        self.entry_username = Entry(self.root, width=30)
        self.entry_username.place(x=150, y=80)
        self.inputusername = Label(self.root, text="Password:", font=(
            "bold", 12), fg='black', bg='lightblue')
        self.inputusername.place(x=150, y=105)
        self.entry_password = Entry(self.root, width=30,show="*")
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
        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)
        self.root.quit()
        
    def show(self,log=None):
        """
        reset username and show window by draw() function
        """
        while(self.data != []):
            self.data.pop()
        self.play(log)
        self.root.mainloop()

# Login([]).show()