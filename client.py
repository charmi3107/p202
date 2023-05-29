import socket
from threading import Thread
from tkinter import *

# nickname=input('choose your name: ')
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address='127.0.0.1'
port= 8000
client.connect((ip_address,port))
print('connected with the server....')

class GUI :
    def __init__(self):
       
       self.Window=Tk()
       self.Window.withdraw()

       self.login=Toplevel()
       self.login.title('title')

       self.login.resizable(width=False,height=False) 
       self.login.configure(width=400,height=400)

       self.pls=Label(self.login, text='please login to cotinue',justify=CENTER, font='Helvetica 14 bold')
       self.pls.place(relheight=0.15,relx=0.2,rely=0.07)

       self.labelname= Label(self.login,text='Name ', font='Helvetica 12')
       self.labelname.place(relheight=0.2,relx=0.1,rely=0.2)

       self.entryname= Entry(self.login,font='Helvetica 14')
       self.entryname.place(relheight=0.12,relwidth=0.4,relx=0.35,rely=0.2)
       self.entryname.focus()

       self.go= Button(self.login,text='continue',font='Helvetica 14 bold',command=lambda:self.goAhead(self.entryname.get()))
       self.go.place(relx=0.4,rely=0.55)

       self.Window.mainloop()

    def layout(self,name):
       self.name=name
       self.Window.deiconify()
       self.Window.title('CHATROOM')
       self.Window.resizable(width=False,height=False)
       self.Window.configure(width=470,height=550,bg='#17202a')

       self.labelhead=Label(self.Window,bg='#17202a',fg='#eaecee',text=self.name,font='Helvetica 13 bold',pady=5)
       self.labelhead.place(relwidth=1)

       self.line=Label(self.Window,width=450,bg='#abb2b9')
       self.line.place(relwidth=1,rely=0.07,relheight=0.012)

       self.text=Text(self.Window,width=20,height=2,bg='#17202a',fg='#eaecee',font="Helvetica 14",padx=5,pady=5)
       self.text.place(relheight=0.745,relwidth=1,rely=0.08)

       self.labelbottom=Label(self.Window,height=80,bg='#abb2b9')
       self.labelbottom.place(relwidth=1,rely=0.825)

       self.entrymessage=Entry(self.labelbottom,bg='#2c3e50',fg='#eaecee',font='Helvetica 13')
       self.entrymessage.place(relwidth=0.74,rely=0.008,relheight=0.06,relx=0.011)

       self.entrymessage.focus()

       self.buttonmessage=Button(self.labelbottom,text='send ',width=20,bg='#abb2b9',font='Helvetica 10 bold',command=lambda:self.sendbutton(self.entrymessage.get()))
       self.buttonmessage.place(relwidth=0.22,rely=0.008,relheight=0.06,relx=0.77)

       self.text.config(cursor='arrow')

       scrollbar=Scrollbar(self.text)
       scrollbar.place(relheight=1,relx=0.974)
       scrollbar.config(command=self.text.yview)

       self.text.config(state=DISABLED)
    def sendbutton(self,msg):
       self.text.config(state=DISABLED)
       self.msg=msg
       self.entrymessage.delete(0,END)

       send=Thread(target=self.write)
       send.start()

    def showmessage(self,message):
       self.text.config(state=NORMAL)
       self.text.insert(END,message + '\n\n')
       self.text.config(state=DISABLED)
       self.text.see(END)

    
    def write(self):
        self.text.config(state=DISABLED)
        while True:
         message=(f'{self.name}:{self.msg}')
         client.send(message.encode('utf-8'))
         self.showmessage(message)
         break


    def goAhead(self,name):
        self.login.destroy()
        self.layout(name)
        recv=Thread(target=self.recieve)
        recv.start()
    def recieve(self):
      while True:
        try:
            message=client.recv(2048).decode('utf-8')
            if message=='NICKNAME':
                client.send(self.name.encode('utf-8'))
            else:
                 self.showmessage(message)

        except:
            print('an error occured...')
            client.close()
            break

g=GUI()






"""def recieve():
    while True:
        try:
            message=client.recv(2048).decode('utf-8')
            if message=='NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)

        except:
            print('an error occured...')
            client.close()
            break

def write():
    while True:
        message='{}: {}'.format(nickname,input(''))
        client.send(message.encode('utf-8'))
recieve_Thread=Thread(target=recieve)
recieve_Thread.start()
write_thread=Thread(target=write)
write_thread.start()"""


            