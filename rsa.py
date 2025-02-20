# Ejemplo de cifrado usando RSA
# 06/02/2025
# Anáhuac Maya
# Santiago Villanueva Muzzi

import Crypto.Util.number

# Vamos a usar 2^16 + 1 = 65537, el número 4 de Fermat por eficiencia
# Debemos tomar en cuenta que "e" será parte de la llave pública, por eso, no ha problema en usar el número de Fermat

e = 65537
print("\n", "Número 4 de Fermat 2^16 + 1 = 65537", e)
# Calculamos las llaves públicas de Alice

pA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
print ("\n", "RSA - Primo de Alice pA:", pA)

qA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
print ("\n", "RSA - Primo de Alice qA:", qA)

# Calculamos nA = pA * qA

nA = pA * qA
print ("\n", "RSA - nA:", nA)

# Calculamos phiA

phiA = (pA - 1) * (qA - 1)
print ("\n", "RSA - phiA:", phiA)

# Calculamos la llave privada de Alice

dA = Crypto.Util.number.inverse(e,phiA)
print("\n", "RSA Llave Privada - dA:", dA)


# El mensaje a cifrar va a ser el número de 450

m = 450
print("\n", "RSA Mensaje - :", m)


# Bob cifra el mensaje con la llave pública de Alice

mC = pow(m, e, nA)
print("\n", "RSA Mensaje Cifrado - :", mC)

# Alice descifra el mensaje de Bob con su llave privada

mA = pow(mC, dA, nA)
print("\n", "Mensaje Descifrado de Bob - :", mA)
