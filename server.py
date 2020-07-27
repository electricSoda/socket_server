import socket
import time
import sys
import select
import os
from tkinter import *
from tkinter import messagebox

os.chdir('C:\\teleport\\Code\\Socket')

try:
    HEADER_LENGTH = 10
    with open('ipcreate.txt', 'r') as r1:
        IP = r1.read()
        r1.close()
    with open('portcreate.txt', 'r') as r2:
        PORT1 = r2.read()
        try:
            PORT=int(PORT1)
        except Exception as e:
            print(e)
            print('System exit')
            input('Press any key to exit')

    root = Tk()
    #root.geometry('1200x750')
    root.title("Pychat")
    root.config(bg='turquoise1')

    # Create Header
    header = Label(root, text='PYCHAT v1.0 BETA')
    header.config(bg='turquoise1', fg='white', font=('Times New Roman bold', 30))
    header.pack()

    # Create Ip and port header
    ip_port = Label(root, text=f'Server Joined on IP:{IP} | PORT:{PORT}')
    ip_port.config(bg='turquoise1', fg='black', font=('Times New Roman bold', 20))
    ip_port.pack()

    #Console
    console1 = Listbox(root)
    console1.config(bg='black', fg='white', height=20, font=('TImes New Roman', 18))
    console1.pack(fill=BOTH)
    console1.insert(END, f'Listening for connections on {IP}:{PORT}')

    #exit (with functions)
    def exite():
        root.destroy()
        sys.exit()

    exitbtn = Button(root, text='Exit', command = exite)
    exitbtn.config(font=('Times new roman bold', 32))
    exitbtn.pack()

    #Start of the mainloop

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((IP, PORT))

    server_socket.listen()

    sockets_list = [server_socket]

    clients = {}


    def receive_message(client_socket):

        try:

            message_header = client_socket.recv(HEADER_LENGTH)

            if not len(message_header):
                return False

            message_length = int(message_header.decode('utf-8').strip())

            return {'header': message_header, 'data': client_socket.recv(message_length)}

        except:

            return False

    while True:
        time.sleep(0.1)
        root.update_idletasks()
        root.update()

        read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

        for notified_socket in read_sockets:
            if notified_socket == server_socket:

                client_socket, client_address = server_socket.accept()

                user = receive_message(client_socket)

                if user is False:
                    continue

                sockets_list.append(client_socket)

                clients[client_socket] = user

                console1.insert(END, 'Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
                console1.see(END)

            else:
                user = clients[notified_socket]
                message = receive_message(notified_socket)

                if message is False:
                    console1.insert(END, 'Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
                    console1.see(END)

                    sockets_list.remove(notified_socket)

                    del clients[notified_socket]

                    continue

                console1.insert(END, f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')
                console1.see(END)

                for client_socket in clients:

                    if client_socket != notified_socket:

                        client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

        for notified_socket in exception_sockets:

            sockets_list.remove(notified_socket)

            del clients[notified_socket]
            

except Exception as e:
    messagebox.showerror('Error', f"Error: {e}")
    sys.exit()
