from tkinter import *


class Login():
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
        self.root.geometry('480x270')
        self.root.title("Dota3 test")

    def draw(self):
        """
        draw login window ui and loop while input username
        """
        canvas = Canvas(self.root, height=600, width=1000, bg="pink")
        canvas.place(x=0, y=0)
        canvas = Canvas(self.root, height=220, width=270, bg="lightblue")
        canvas.place(x=100, y=30)
        self.inputusername = Label(self.root, text="Username:", font=(
            "bold", 12), fg='black', bg='lightblue')
        self.inputusername.place(x=150, y=50)
        self.entry_name = Entry(self.root, width=30)
        self.entry_name.place(x=150, y=80)
        self.BCheck = Button(self.root, text="GoPlay",
                             command=self.get, width=25, height=3)
        self.BCheck.place(x=150, y=150)
        mainloop()

    def get(self):
        """
        function to get username from entry and detect 
        if length of username is >= 6 or username is empty 
        function will warn user then hide and quit ui
        """
        if len(self.entry_name.get()) >= 6 or self.entry_name.get() == "":
            self.entry_name.delete(0, END)
            self.warning = Label(
                self.root, text="length of username must less than 6 and not empty", font=("", 8), fg='red', bg='lightblue')
            self.warning.place(x=150, y=105)
            return None
        self.username.append(self.entry_name.get())
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
        self.draw()
