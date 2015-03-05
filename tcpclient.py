#TCP Client for Python3
import socket
from sys import argv
import _thread
HOST,PORT = argv[1],int(argv[2]) 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
Flag = True
def Read(s):
  while Flag:
    try:
      rdata = s.recv(1024)
      print("Recd: %s" %rdata.strip().decode('utf'))
    except Exception:
      _thread.exit()
_thread.start_new_thread(Read,(s,))
while Flag:
  wdata = input()
  if wdata.strip() == 'quit':
    print("connection closed")
    Flag = False
  s.send(bytes(wdata,'utf'))
s.close()
