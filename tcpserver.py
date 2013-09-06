# TCP Server Program
import socket,thread
from time import ctime,sleep
from sys import argv
HOST_TCP = ''               # Symbolic name meaning all available interfaces
PORT_TCP = int(argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST_TCP, PORT_TCP))
s.listen(1)
#s.settimeout(5)
FLAG = 0
def S_TCP(conn,addr):
 while(FLAG):
  conn.send(ctime()+'\n')
  sleep(1)
def TCP(conn,addr):
 global FLAG
 while 1:
  DATA = conn.recv(1024).strip()
  if DATA == 'send': 
   FLAG = 1
   thread.start_new_thread(S_TCP,(conn,addr))
  elif DATA == 'stop': FLAG = 0
  if DATA.strip() != "quit": conn.send(DATA.upper()+'\n')
  else:
   print addr[0], "connection closed" 
   break
while 1:
  conn, addr = s.accept()
  print('Connected by', addr[0])
  thread.start_new_thread(TCP,(conn,addr))