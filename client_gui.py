from tkinter import *
from tkinter import messagebox
import socket
import select
import errno
import sys
import time

def mainClient():
    #Variables
    message1 = False

    #Create window
    root = Tk()
    root.geometry('1200x750')
    root.title("Pychat")
    root.config(bg='turquoise1')

    #Open the three text files
    with open('ipjoin.txt', 'r') as r1:
        IP = r1.read()
        r1.close()

    with open('portjoin.txt', 'r') as r2:
        PORT = r2.read()
        try:
            PORT = int(PORT)
        except Exception as e:
            messagebox.showerror('Error', e)
        r2.close()

    with open('userjoin.txt', 'r') as r3:
        my_username = r3.read()
        r3.close()

    # Create Header
    header = Label(root, text='PYCHAT v1.0 BETA')
    header.config(bg='turquoise1', fg='white', font=('Times New Roman bold', 30))
    header.pack()

    #Create Ip and port header
    ip_port = Label(root, text=f'Server Joined on IP:{IP} | PORT:{PORT}')
    ip_port.config(bg='turquoise1', fg='black', font=('Times New Roman bold', 20))
    ip_port.pack()

    #Create chat box
    console = Listbox(root)
    console.config(bg='grey', fg='white', width=98, height=18, font=('Comic Sans MS', 15), justify=LEFT)
    console.pack()
    console.insert(END, 'Welcome to the chatroom!')

    #HEADER_SPACE
    HEADER_SPACE = '    '

    #Chat entry text
    entry_text = Label(root, text='Type something...')
    entry_text.config(bg='turquoise1', fg='black', font=('Times New Roman bold', 25))
    entry_text.pack()

    #Chat entry box (with function)
    message_content = ''
    def send(event):
       global message1, message_content
       message_content = sente.get()
       console.insert(END, f'{my_username} > {sente.get()}')
       console.see(END)
       sente.set('')
       message_c = message_content.encode("utf-8")
       message_header = f"{len(message_c):<{HEADER_LENGTH}}".encode("utf-8")
       client_socket.send(message_header + message_c)
       return message_content

    sente = StringVar()

    message = Entry(root, width=80, textvariable = sente)
    message.config(font=('Comic Sans ms bold', 16))
    message.bind('<Return>', send)
    message.pack()

    #Exit Button (with function)
    def btne():
        root.destroy()
        sys.exit()
        quit()

    exitbtn = Button(root, text='Exit', command = btne)
    exitbtn.config(font=('Times new roman bold', 32))
    exitbtn.pack()

    #mainloop for chat
    try:
        HEADER_LENGTH = 10

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((IP, PORT))
        client_socket.setblocking(False)

        username = my_username.encode("utf-8")
        username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(username_header + username)
        try:

            while True:
                try:
                    while True:
                        root.update_idletasks()
                        root.update()
                        # receive things
                        username_header = client_socket.recv(HEADER_LENGTH)
                        if not len(username_header):
                            messagebox.showinfo('Connnection Closed', 'The server was closed by the host.')
                            time.sleep(0.5)
                            sys.exit()

                        username_length = int(username_header.decode("utf-8").strip())
                        username = client_socket.recv(username_length).decode("utf-8")

                        message_header = client_socket.recv(HEADER_LENGTH)
                        message_length = int(message_header.decode("utf-8"))
                        message = client_socket.recv(message_length).decode("utf-8")

                        console.insert(END, f'{username} > {message}')
                        console.see(END)

                except IOError as e:
                    if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                        messagebox.showinfo('Reading Error', f'Reading error: {str(e)}')
                        time.sleep(0.5)
                        sys.exit()
                    continue

                except Exception as e:
                    sys.exit()

        except Exception as e:
            messagebox.showerror('Error', f'Loop Error: ({e})')
    except Exception as e:
        messagebox.showerror('Error', f'Main Join Error:({e})')
