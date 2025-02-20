## Actividad Diffie-Hellman
## Santiago Villanueva
## Anáhuac Mayab 
## 12/02/2025

import hashlib
import random

# Traemos el número primo de RFC3625 bits - MODP Group
p = int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF", 16)
g = 2

# Comenzamos generando los números secretos de Alice y Bob

# Llave secreta de Alice
sAlice = random.getrandbits(256) 
print("\n", "Llave secreta de Alice:", "\n", sAlice)
print("\n")

# Llave secreta de Bob
sBob = random.getrandbits(256)
print("\n", "Llave secreta de Bob:", "\n", sBob)
print("\n")

# Llave secreta de Eve
sEve = random.getrandbits(256)
print("\n", "Llave secreta de Eve:", "\n", sEve)
print("\n")

print("\n", "Ejemplo de conversación entre Alice y Bob y Alice e Eve")

# Alice manda mensaje a Eve -> g^a mod p
A = pow(g, sAlice, p)
print("\n", "Mensaje de Alice a Eve:", A)

# Eve le manda mensaje a Bob
B = pow(g, sEve, p)
print("\n", "Mensaje de Eve a Bob:", B)

# Bob le manda mensaje a Eve
C = pow(g,sBob,p)
print("\n", "Mensaje de Bob a Eve", C)

# Eve le manda mesaje a Alice
D = pow(g,sEve,p)
print("\n", "Mensaje de Eve a Alice", D)


# Calculamos llaves secretas

#Alice calcula la llave secreta compartida de Alice con Bob -> s1 = B^a mod p

s1 = pow(B,sAlice, p)

print("\n", "Llave secreta compartida de Alice con Bob:", s1)

# Bob calcula la llave secreta compartida de Bob con Alice -> s2 = A^b mod p

s2 = pow(A,sBob, p)

print("\n", "Llave secreta compartida de Bob con Alice:", s2)

# Alice calcula la llave secreta compartida de Alice con Eve -> s1 = B^a mod p

s3 = pow(C,sAlice, p)

print("\n", "Llave secreta compartida de Alice con Eve:", s3)

# Comparamos llaves secretas

h1 = hashlib.sha512(int.to_bytes(s1, length=1024, byteorder='big')).hexdigest()
h2 = hashlib.sha512(int.to_bytes(s1, length=1024, byteorder='big')).hexdigest()
h3 = hashlib.sha512(int.to_bytes(s1, length=1024, byteorder='big')).hexdigest()

print("\n,", "-----------------------------------------------------------")

print("\n", "Comparación de llave secreta de Alice con Eve:")

print("\n", "h1:", h1)
print("\n", "h3:", h3)


if(h1 == h3):
    print("TRUE", "\n")
else:
    print("FALSE",  "\n")

print("\n", "-----------------------------------------------------------")

print("\n", "Comparación de llave secreta de Bob con Eve:")
print("\n", "h2:", h2)
print("\n", "h3:", h3)

if(h2 == h3):
    print("TRUE", "\n")
else:
    print("FALSE",  "\n")
