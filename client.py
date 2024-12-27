import pyautogui as pg
import socket
import tkinter as tk
from tkinter import simpledialog, messagebox

# Function to prompt for host and port using tkinter
def get_host_and_port():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask for the host
    host = simpledialog.askstring("Input", "Enter the host address:", parent=root)
    if not host:
        messagebox.showerror("Error", "Host is required!")
        root.destroy()
        exit()

    # Ask for the port
    port = simpledialog.askinteger("Input", "Enter the port number:", parent=root, minvalue=1, maxvalue=65535)
    if not port:
        messagebox.showerror("Error", "Port is required!")
        root.destroy()
        exit()

    root.destroy()
    return host, port

# Get host and port from the popup
host, port = get_host_and_port()

# Set up the client socket
client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

message = 'done'
while True:
    try:
        while message.lower().strip() != 'bye':
            client_socket.send(message.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response

            if data == 'c':
                pg.click(x, y)
            elif data == 'del':
                pg.typewrite(['backspace'])
            elif data.startswith('cde:'):
                pg.write(data.replace('cde:', ''))
            elif data == 'r':
                pg.click(button='right')
            elif data == 'd':
                pg.click(clicks=2)
            elif data == 'nl':
                pg.typewrite(['enter'])
            else:
                x = int(data.split(' ')[0])
                y = int(data.split(' ')[1])
                pg.moveTo(x, y)

            message = 'done'  # reset message

        client_socket.close()  # close the connection
    except Exception as e:
        print(f"An error occurred: {e}")
        pass
