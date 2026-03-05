


 
import socket
import random
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def generate_prime():
    while True:
        p = random.randint(200, 500)
        if is_prime(p):
            return p
def primitive_root(p):
    required = set(range(1, p))
    for g in range(2, p):
        actual = set(pow(g, powers, p) for powers in range(1, p))
        if required == actual:
            return g
p = generate_prime()
g = primitive_root(p)
x = random.randint(1, p - 2)
h = pow(g, x, p)
print("\n----- KEY GENERATION -----")
print("Prime p:", p)
print("Generator g:", g)
print("Private Key x:", x)
print("Public Key (p, g, h):", (p, g, h))
server = socket.socket()
server.bind(('localhost', 12345))
server.listen(1)
print("\nWaiting for client...")
conn, addr = server.accept()
print("Connected to:", addr)
conn.send(f"{p},{g},{h}".encode())
data = conn.recv(1024).decode()
c1, c2 = map(int, data.split(','))
print("\n----- RECEIVED CIPHERTEXT -----")
print("c1:", c1)
print("c2:", c2)
s = pow(c1, x, p)
s_inv = pow(s, -1, p)
m = (c2 * s_inv) % p
print("\n----- DECRYPTION -----")
print("Shared Secret s:", s)
print("Inverse of s:", s_inv)
print("Decrypted Message M:", m)
conn.close()
server.close()
 
 