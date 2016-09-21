import hashlib
from Crypto.PublicKey import RSA
from Crypto import Random

Def processa(data):
  nBufSize = 65536
  sha256 = hashlib.sha256()
  With open(data, 'rb') as aDat:
    while True:
      data = aDat.read(nBufSize)
	  If not data:
	    break
	  sha256.update(data)
Return sha256.hexdigest()

Random_Generator = Random.new().read
cKey = RSA.generate(2048, Random_Generator)
cPublicKey = cKey.publickey()

#Realiza a criptografia do Hash.
cOrigHash = processa("entrada.txt")
cCriptHash = cPublicKey.encrypt(cOrigHash.encode(encoding='UTF-8'), 32)

#Descriptografa e valida hash.
cResHash = cKey.decrypt(cCriptHash)
cOrigHash = processa("entrada.txt").encode(encoding='UTF-8')
If(cResHash == cOrigHash):
      Print ("Dados de entrada e saída equivalentes!")
Else:
      Print ("Os dados de entrada e saída são diferentes!")
