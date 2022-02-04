# This project is a GUI interface for a networking tool that will be able to retrieve your IP adress and ping a website.
# Lauren Norcross - 2/2/22
import tkinter as tk
import socket
import platform
import subprocess
window = tk.Tk()

def ping_google():
  host = "www.google.com"
  hostname = socket.gethostname()
  IPadress = socket.gethostbyname(hostname)
  T = tk.Text(window, height=2, width=30)
  T.pack()
  T.insert(tk.END, hostname + "\n")  
  T.insert(tk.END, IPadress + "\n")
  param = '-n' if platform.system().lower()=='windows' else '-c'
  test = ['ping', param, '3', host]
  ping = subprocess.run(test) == 0
  print(hostname)
  print(IPadress)
  print(ping)
  T.pack()
  T.insert(tk.END, ping)
ping = tk.Button(text="ping", width=25,height=5, command=ping_google)
ping.pack()
window.mainloop()