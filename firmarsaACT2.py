## Santiago Villanueva Muzzi 00466355
## Anáhuac Mayab
## 19/02/2025
## Actividad de Firmado Digital Usando RSA


## En la firma, se firma con mi llave privada y un segundo, para verificar, lo hará con mi llave privada.
## Importamos las librerías

import Crypto.Random
import Crypto.Util.number
import hashlib

## Para "e" vamos a usar el número 4 de Fermat

e = 65537

## Calculamos la llave pública de Alice

# Estos pA y qA se usan para sacar phi
pA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

nA = pA * qA

print("\n", "RSA Llave Pública de nAlice:", nA)

## Calculamos la llave pública de Bob
## pB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
## qB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

## nB = pB * qB

## print("\n", "RSA Llave Pública de nBob:", nB)


## Calculamos la llave privada de Alice, primero calculamos phi de Alice
phiA = (pA - 1) * (qA - 1)

dA = Crypto.Util.number.inverse(e, phiA)

print("\n", "RSA Llave Privada de Alice dA", dA )


## Calculamos la llave privada de Bob, primero calculamos phi de Bob
## phiB = (pB - 1) * (qB - 1)

## dB = Crypto.Util.number.inverse(e, phiB)

## print("\n", "RSA Llave Privada de Bob dB", dB)

## Firmamos el mensaje
mensaje = "Hola Mundo"
print("\n", "Mensaje", mensaje)

## Generamos el HASH del Mensaje

hM = int.from_bytes(hashlib.sha256(mensaje.encode('utf-8')).digest(), byteorder='big')
print("\n", "HASH de hM", hex(hM))

## Firmamos el HASH usado la llave privada de Alice y se lo enviamos a Bob

sA = pow(hM, dA, nA)
print("\n", "Firma: ", sA)

## Bob verifica la firma de Alice, usando la llave pública de Alice

hM1 = pow(sA, e, nA)
print("\n", "HASH de hM1: ", hex(hM1))

## Verificamos

print("\n", "Firma Válida: ", hM==hM1, "\n")