import hashlib
import sys

argument = len(sys.argv)

print("*******************************************************************************")
texto = sys.argv[1]
sha256 = hashlib.sha256(texto.encode()).hexdigest()

print("SHA256: " , sha256)
print("*******************************************************************************")