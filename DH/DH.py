base = 3
mod = 68

PKey = int(input("Informe a chave privada: "))

print((base ** PKey) % mod)

IKey = int(input("Informe a chave intermediaria: "))

print("Chave compartilhada:", (IKey ** PKey) % mod)

input("Tecle enter para continuar.")
