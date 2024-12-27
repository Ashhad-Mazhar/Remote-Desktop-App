from vidstream import StreamingServer
import threading
import tkinter as tk
from tkinter.messagebox import showinfo

#Can find this using IPConfig in CMD
myPrivateIPv4Address = '192.168.100.7'
my_generated_port = 9999
k = tk.Tk()
showinfo('Control Data','Host = '+myPrivateIPv4Address+'\nPort = '+str(my_generated_port))
k.destroy()
#Sending the data as parameters and saving them in receiver variable
receiver = StreamingServer(myPrivateIPv4Address,my_generated_port)

t = threading.Thread(target=receiver.start_server)

t.start()

while input("") != 'STOP':
    continue

receiver.stop_server()