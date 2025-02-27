## Parcial 1 Santigao Villanueva Muzzi 00466355
## Anáhuac Mayab 
## Seguridad Informática y Análisis Forense
## 19/02/2025

## hacer un loop que tome el archivo completo y lo divida en chunks y almacenarlo en una lista de python, poner el tamaño del chunk y cifrar cada chunk, descifrar cada chunk y juntarlo para leerlo
## buscar como hacer un recorrido de la lista de chunks en python
## Primero importamos las librerías necesarias
import Crypto.Util.number
import Crypto.Random
import hashlib
import base64

# Usaremos el número "4" de Fermat
e=65537



## primer

## Ahora calculamos p y q para Alice
pA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

## Sacamos la llave pública de Alice
nA = pA * qA

print("\n", "Llave pública de Alice: ", nA)

## Ahora calculamos p y q para Bob
pB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

## Sacamos la llave pública de Bob
nB = pB * qB

print("\n", "Llave pública de Bob: ", nB)

## Ahora calculamos p y q para la AC (Autoridad Acreditadora)
pAC = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qAC = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

## Sacamos la llave pública de AC
nAC = pAC * qAC

print("\n", "Llave pública de Bob: ", nAC)

## Calculamos phi de Alice para luego calcular la llave privada de Alice

phiA = (pA - 1) * (qA - 1)

dA = Crypto.Util.number.inverse(e, phiA)

print("\n", "Llave Privada de Alice dA", dA)

## Calculamos phi de Bob para luego calcular la llave privada de Bob

phiB = (pB - 1) * (qB - 1)

dB = Crypto.Util.number.inverse(e, phiB)

print("\n", "Llave Privada de Bob dB", dB)

## Calculamos phi de AC para luego calcular la llave privada de AC

phiAC = (pAC - 1) * (qAC - 1)

dAC = Crypto.Util.number.inverse(e, phiAC)

print("\n", "Llave Privada de AC dAC", dAC)


mensaje = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris pharetra nec diam cursus lacinia. Proin ut mi et lorem maximus cursus. Aliquam erat volutpat. Integer tristique, dolor eu hendrerit posuere, quam risus porttitor ante, ac scelerisque quam erat vitae ante. Integer ac nulla vel mauris feugiat rutrum nec vitae turpis. Proin eget risus ac nibh dignissim commodo. Vivamus porta magna at consectetur vehicula. Fusce in massa lacus. Morbi ultrices lacus vel enim fermentum, et fermentum metus blandit. Vestibulum sit amet finibus orci. Aliquam sodales arcu id nunc dignissim ullamcorper. Integer sit amet nisl in ligula convallis suscipit ut vel quam. Aenean varius mattis turpis a pellentesque. Ut id pulvinar risus, nec fringilla leo. Suspendisse sed condimentum arcu. Sed mattis lectus et metus pellentesque euismod. Donec sit amet pulvinar diam. In hac habitasse platea dictumst. Suspendisse potenti. Nulla luctus lacinia odio a feugiat. Curabitur tempor, magna ac iaculis efficitur, justo libero ultrices nisi, eget eleifend ante blandit."
chunk_size = 128
def split_into_chunks(mensaje, chunk_size):
    for i in range(0, len(mensaje), chunk_size):
        yield mensaje[i:i + chunk_size]

## Alice cifra los chunks con la llave pública de Bob

chunks = list(split_into_chunks(mensaje, chunk_size))

## Hacemos el loop para convertir 

for i in range(len(chunks)):
    mensaje = int.from_bytes(hashlib.sha256(chunks[i].encode('utf-8')).digest(), byteorder='big')
    mC = pow(mensaje, e, nB)
    print("\n", "RSA Mensaje Cifrado: ", mC)

   # Bob descifra el mensaje con su llave privada
    mD = pow(mC, dB, nA)
    m1 = int.to_bytes(mD, length=1024, byteorder='big').decode('utf-8')
    mdc = ''.join(m1, length=1024, byteorder='big')
    print("\n", "Mensaje Descifrado de Alice: ", mdc)





## pasar a bytes y cifrar 
## int from bytes int to byes


## cifrar y descifrar en el mismo recorrido

## hacer un loop que tome el archivo completo y lo divida en chunks y almacenarlo en una lista de python,
# despues hacer un recorrido de la lista y por cada elemento cifrar (pasar a bytes) y descifrar y el texto descifrado, y concatenar los chunks
# 
#  poner el tamaño del chunk y cifrar cada chunk, descifrar cada chunk y juntarlo para leerlo
