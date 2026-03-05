

 
import socket
import random
 
client = socket.socket()
client.connect(('localhost', 12345))
 
data = client.recv(1024).decode()
p, g, h = map(int, data.split(','))
 
print("\n----- PUBLIC KEY RECEIVED -----")
print("Prime p:", p)
print("Generator g:", g)
print("Public Key h:", h)
 
m = int(input("\nEnter Message M: "))
 
k = random.randint(1, p - 2)
c1 = pow(g, k, p)
c2 = (m * pow(h, k, p)) % p
 
print("\n----- ENCRYPTION -----")
print("Random k:", k)
print("c1:", c1)
print("c2:", c2)
 
client.send(f"{c1},{c2}".encode())
 
client.close()
 
 
 
 
 