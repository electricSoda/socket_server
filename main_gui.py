from tkinter import *
from tkinter import messagebox
import socket
import select
import subprocess
from time import *
import os
import client_gui

#set default directories, etc.
os.chdir('C:\\teleport\\Code\\Socket')

def main():
    global ipvv, portvv, ipv, portv
    #Create window
    root = Tk()
    root.geometry('1200x700')
    root.title("Pychat")
    root.config(bg='turquoise1')

    #Public Variables
    ipv = StringVar()
    portv = StringVar()
    userv = StringVar()
    ipvv = StringVar()
    portvv = StringVar()


    #Functions

    #Clear Screen Function
    def cls():
        join.pack_forget()
        div.pack_forget()
        create.pack_forget()

    #Join into server host
    def client():
        ip11 = ipv.get()
        port11 = portv.get()
        user11 = userv.get()

        with open('ipjoin.txt', 'w') as p1:
            p1.write(ip11)
            p1.close()

        with open('portjoin.txt', 'w') as p2:
            p2.write(port11)
            p2.close()

        with open('userjoin.txt', 'w') as p3:
            p3.write(user11)
            p3.close()

        try:
            port11 = int(port11)
        except ValueError as e:
            messagebox.showerror('Invalid Value', 'The PORT field must be a number with less than or equal to 6 digits')
            return

        if ip11 == '' or port11 == '':
            messagebox.showerror('Empty Value', 'One or both of the fields are empty')
        else:
            root.destroy()
            client_gui.mainClient()


    #cl function for server101
    def cl1():
        ipt1.pack()
        ip1.pack()
        portt1.pack()
        port1.pack()
        div3.pack()
        joinin1.pack()
        div4.pack()
        back2.pack()

        ip_port.pack_forget()

    #clear function for the server console
    def cls2():
        initial.pack_forget()
        Back.pack_forget()
        ip_port.pack_forget()
        console1.pack_forget()

        join.pack()
        div.pack()
        create.pack()

    #Call function for the server
    def extra_call():
        initial.pack_forget()
        subprocess.run('python server.py')

    #Create server
    def server101():
        global ip_port, initial, console1, ip22, port22, Back

        ip22 = ipvv.get()
        port22 = portvv.get()

        with open('ipcreate.txt', 'w') as p1:
            p1.write(ip22)
            p1.close()

        with open('portcreate.txt', 'w') as p2:
            p2.write(port22)
            p2.close()

        ipt1.pack_forget()
        ip1.pack_forget()
        portt1.pack_forget()
        port1.pack_forget()
        div3.pack_forget()
        div4.pack_forget()
        joinin1.pack_forget()
        back2.pack_forget()

        ip_port = Label(root, text=f'Server Created on IP:{ip22} | PORT:{port22}')
        ip_port.config(bg='turquoise1', fg='black', font=('Times New Roman bold', 20))
        ip_port.pack()

        try:
            port22 = int(port22)
        except ValueError as e:
            messagebox.showerror('Invalid Value', 'The PORT field must be a number with less than or equal to 6 digits')
            cl1()
            return


        if ip22 == '' or port22 == '':
            messagebox.showerror('Empty Value', 'One or both of the fields are empty')
            cl1()
        else:
            initial = Button(root, text=f'Initialize The Server On {ip22}:{port22}', command=extra_call)
            initial.config(bg='gray', fg='white', height=5, font=('Times New Roman', 15))
            initial.pack()

            Back = Button(root, text='Back', command=cls2)
            Back.config(bg='gray', fg='white', height=5, width = 15,font=('Times New Roman', 15))
            Back.pack()

            console1 = Listbox(root)
            console1.config(bg='black', fg='white', width=200, height=30, font=('TImes New Roman', 18))
            console1.pack()

    #Main Menu function 1
    def main1():
        ipt.pack_forget()
        ip.pack_forget()
        portt.pack_forget()
        port.pack_forget()
        usser.pack_forget()
        usserv.pack_forget()
        div1.pack_forget()
        div2.pack_forget()
        joinin.pack_forget()
        back1.pack_forget()

        join.pack()
        div.pack()
        create.pack()

    #Main Menu Function 2
    def main2():
        ipt1.pack_forget()
        ip1.pack_forget()
        portt1.pack_forget()
        port1.pack_forget()
        div3.pack_forget()
        div4.pack_forget()
        joinin1.pack_forget()
        back2.pack_forget()

        join.pack()
        div.pack()
        create.pack()

    #Joining Function
    def joining():
        global ipt, ip, portt, port, div1, joinin, div2, back1, usser, usserv
        cls()

        ipt = Label(root, text='ENTER IP OF SERVER')
        ipt.config(bg='turquoise1',fg='black',font=('Times New Roman bold', 20))
        ipt.pack()
        ip = Entry(root, textvariable=ipv)
        ip.config(width=50)
        ip.pack()

        portt = Label(root, text='ENTER PORT OF SERVER')
        portt.config(bg='turquoise1', fg='black', font=('Times New Roman bold', 20))
        portt.pack()
        port = Entry(root, textvariable = portv)
        port.config(width=50)
        port.pack()

        usser = Label(root, text='ENTER YOUR PREFERED USERNAME')
        usser.config(bg='turquoise1', fg='black', font=('Times New Roman bold', 20))
        usser.pack()
        usserv = Entry(root, textvariable=userv)
        usserv.config(width=50)
        usserv.pack()

        div1 = Label(root, text='---------------------------------------------')
        div1.config(fg='white', bg='turquoise1', font=('Times New Roman bold', 25))
        div1.pack()

        joinin = Button(root, text='Join!', command = client,activebackground='grey23', activeforeground='white')
        joinin.config(bg='gray', fg='white', height=5, width=25, font=('Times New Roman', 15))
        joinin.pack()

        div2 = Label(root, text='---------------------------------------------')
        div2.config(fg='white', bg='turquoise1', font=('Times New Roman bold', 25))
        div2.pack()

        back1 = Button(root, text='Back', command = main1, activebackground='grey23', activeforeground='white')
        back1.config(bg='gray', fg='white', height=5, width=25, font=('Times New Roman', 15))
        back1.pack()

    #Creating Function
    def creating():
        global ipt1, ip1, portt1, port1, div3, joinin1, div4, back2
        cls()

        ipt1 = Label(root, text='ENTER YOUR PUBLIC IP (so people can connect to your computer)')
        ipt1.config(bg='turquoise1', fg='black', font=('Times New Roman bold', 20))
        ipt1.pack()
        ip1 = Entry(root, textvariable=ipvv)
        ip1.config(width=50)
        ip1.pack()

        portt1 = Label(root, text='''ENTER PORT OF SERVER (can be any port number, but can't have more than 6 digits)''')
        portt1.config(bg='turquoise1', fg='black', font=('Times New Roman bold', 20))
        portt1.pack()
        port1 = Entry(root, textvariable=portvv)
        port1.config(width=50)
        port1.pack()

        div3 = Label(root, text='---------------------------------------------')
        div3.config(fg='white', bg='turquoise1', font=('Times New Roman bold', 25))
        div3.pack()

        joinin1 = Button(root, text='Create!', command=server101, activebackground='grey23', activeforeground='white')
        joinin1.config(bg='gray', fg='white', height=5, width=25, font=('Times New Roman', 15))
        joinin1.pack()

        div4 = Label(root, text='---------------------------------------------')
        div4.config(fg='white', bg='turquoise1', font=('Times New Roman bold', 25))
        div4.pack()

        back2 = Button(root, text='Back', command=main2, activebackground='grey23', activeforeground='white')
        back2.config(bg='gray', fg='white', height=5, width=25, font=('Times New Roman', 15))
        back2.pack()

    #Create Header
    header = Label(root, text='PYCHAT v1.0 BETA')
    header.config(bg='turquoise1', fg='white', font=('Times New Roman bold', 30))
    header.pack()

    #Create join buttoh
    join = Button(root, text='Join a chat server', command = joining,activebackground='grey23', activeforeground='white')
    join.config(bg = 'gray', fg='white', height=5, width=25, font=('Times New Roman', 15))
    join.pack()

    #Create a divider
    div = Label(root, text = '---------------------------------------------')
    div.config(fg='white', bg='turquoise1', font=('Times New Roman bold', 25))
    div.pack()

    #Create a server create button (not recommended for beginners)
    create = Button(root, text='Create a chat server', command = creating, activebackground='grey23', activeforeground='white')
    create.config(bg = 'gray', fg='white', height=5, width=25, font=('Times New Roman', 15))
    create.pack()

    root.mainloop()
