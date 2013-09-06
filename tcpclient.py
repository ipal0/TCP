import socket
from sys import argv
import thread
HOST,PORT = argv[1],int(argv[2]) 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
Flag = True
def Read(s):
  while Flag:
    try:
      rdata = s.recv(1024)
      print "<<< %s" %rdata.strip()
    except Exception:
      thread.exit()
thread.start_new_thread(Read,(s,))
while Flag:
  wdata = raw_input()
  s.send(bytes(wdata+'\r'))
  if wdata.strip() == 'quit':
    print "connection closed"
    Flag = False
s.close()