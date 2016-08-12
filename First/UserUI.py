from tkinter import *
from socket import *
from _thread import *


class UserUI(Tk):

    def __init__(self):
        self.root = Tk.__init__(self)
        self.__initUI()
        self.myUsername = 'test2'
        self.clientSocket = socket(AF_INET, SOCK_DGRAM)

        self.serverAddress = ('192.168.192.6', 6001)

        self.address = ('192.168.192.24', 6000)
        self.clientSocket.bind(self.address)
        self.clientSocket.settimeout(1)
        start_new_thread(self.listenInMessage, ())

    def __initUI(self):
        self.frameTop = Frame(self.root, height=100)
        self.frameInput = Frame(self.root, width=100, height=40)

        self.frameTop.pack()
        self.frameInput.pack(side=BOTTOM)

        self.entry = Entry(self.frameInput, width=25)
        self.text = Text(self.frameTop, bg="white", width=60, height=30, state=DISABLED)
        self.button = Button(self.frameInput, text="Send", width=10, command=self.typeMessage)

        self.entry.grid(row=0, column=0, rowspan=2)
        self.button.grid(row=0, column=1, rowspan=2)
        self.text.grid(row=0, column=0)

    def typeMessage(self):
        message = self.entry.get()
        if message != "":
            self.sendMessage(self.myUsername, message)
            self.entry.delete(0, END)

    def sendMessage(self, username, message):
        self.writeOnText(username + ": " + message)
        self.clientSocket.sendto((username + ": " + message).encode(), self.serverAddress)

    def writeOnText(self, message):
        self.text.config(state=NORMAL)
        self.text.insert(END, '%s\n' % message)
        self.text.config(state=DISABLED)

    def listenInMessage(self):
        while True:
            try:
                data = self.clientSocket.recv(1024)
                self.writeOnText(data.decode())
            except:
                pass

if __name__ == '__main__':
    d = UserUI()
    d.mainloop()