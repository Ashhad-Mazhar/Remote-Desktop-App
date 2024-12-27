from vidstream import ScreenShareClient
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox

# Function to prompt for IP address and port using tkinter
def get_ip_and_port():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask for the IP address
    ip_address = simpledialog.askstring("Input", "Enter IP Address:", parent=root)
    if not ip_address:
        messagebox.showerror("Error", "IP Address is required!")
        root.destroy()
        exit()

    # Ask for the port number
    port = simpledialog.askinteger("Input", "Enter Port Number:", parent=root, minvalue=1, maxvalue=65535)
    if not port:
        messagebox.showerror("Error", "Port Number is required!")
        root.destroy()
        exit()

    root.destroy()
    return ip_address, port

# Get IP address and port from the popup
myPrivateIPv4Address, my_generated_port = get_ip_and_port()

# Sending the data as parameters and saving them in sender variable
sender = ScreenShareClient(myPrivateIPv4Address, my_generated_port)

# Send the stream thread to start sharing
t = threading.Thread(target=sender.start_stream)
t.start()

# If STOP is the call, break the loop and connection with the server
while input("") != 'STOP':
    continue

# To stop the client stream connected to the server
sender.stop_stream()
