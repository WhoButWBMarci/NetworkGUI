# This project is a GUI interface for a networking tool that will be able to retrieve your IP adress and ping a website.
# Lauren Norcross - 2/2/22
import tkinter as tk
import socket
import platform
import subprocess
# Creates the GUI window
window = tk.Tk()

def findIP():
  # .gethostname retrieves the system's host name
  hostname = socket.gethostname()
  # .gethostbyname retrieves the system's IP address. 
  IPadress = socket.gethostbyname(hostname)
  # Creates a Text box for the host name and ID adress
  T = tk.Text(window, height=2, width=30)
  l = tk.Label(window, text = "Output")
  l.config(font =("Courier", 14))
  l.pack()
  T.pack()
  # Inserts the hostname & IP address
  T.insert(tk.END, hostname + "\n")  
  T.insert(tk.END, IPadress + "\n")
  print(hostname)
  print(IPadress)
  # Creates a new function to ping google.
  def ping_google():
    # Sets the host as google, in later verisons, this will be based off of a user input.
    host = "www.google.com"
    # Checks if the computer's system is windows or UNIX-based (ie linux, Mac), and then decides what flag to use for the ping.
    param = '-n' if platform.system().lower()=='windows' else '-c'
    # Test inputs the command, certain demographics, how many file transfers that the user wants to occur, and the host name.
    test = ['ping', param, '3', host]
    ping = subprocess.run(test)
    # Creates the label for the ping results
    T = tk.Text(window, height=2, width=30)
    l= tk.Label(window, text="Ping Results")
    l.config(font =("Courier", 14))
    l.pack()
    T.pack()
    T.insert(tk.END, ping)
  ping_google()
ping = tk.Button(text="ping", width=25,height=5, command=findIP)
ping.pack()
window.mainloop()
