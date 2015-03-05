# TCP Server Program for Python3
import socket,_thread
from time import ctime,sleep
from sys import argv
HOST = ''               # Symbolic name meaning all available interfaces
PORT = int(argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
FLAG = 0
def S_TCP(conn,addr):
 while(FLAG):
  conn.send(bytes(input(),'utf'))
  sleep(1)
def TCP(conn,addr):
 global FLAG
 while 1:
  try:
   DATA = conn.recv(1024).strip().decode('utf')
   if DATA.strip() != "quit": 
    FLAG = 1
    print("Recd: %s" %DATA)
    _thread.start_new_thread(S_TCP,(conn,addr))
   else:
    FLAG = 0
    print(addr[0], "connection closed")
    break
  except Exception:
    _thread.exit()
while 1:
  conn, addr = s.accept()
  print('Connected by', addr[0])
  _thread.start_new_thread(TCP,(conn,addr))
