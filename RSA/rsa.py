# coding: utf-8
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

#Gera a chave privada e a pública.
RandomGenerator = Random.new().read
cPrivateKey = RSA.generate(1024, RandomGenerator)
cPublicKey = cPrivateKey.publickey()

#Criptografa.
cEncryptedMsg = cPublicKey.encrypt(str.encode('TestMessage123'),1024)
print ('Mensagem criptografada:', cEncryptedMsg)

#Descriptografa.
cDecryptedMsg = cPrivateKey.decrypt(cEncryptedMsg)
print ('Mensagem descriptografada:', cDecryptedMsg.decode())
