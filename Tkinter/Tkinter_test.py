from tkinter import *
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel = Label(self,text="Hello , world!")
        self.helloLabel.pack()
        self.quitButton = Button(self,text="Quit",command=self.quit())
        self.quitButton.pack()

appFrame = Application()
appFrame.master.title("hello world")
appFrame.mainloop()