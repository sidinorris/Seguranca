# coding: utf-8
from Crypto.Cipher import AES
from time import sleep

#Declaracao de Variáveis:
cMsg = "A mensagem de 16"
cXMsg = "THE X message"
key = "1234567890123456"

#Criptografando...
oCript = AES.new(key, AES.MODE_CBC, cXMsg)
cCripText= oCript.encrypt(cMsg)
print(cCripText)

#Descriptografando...
oDecript = AES.new(key, AES.MODE_CBC, cXMsg)
cDecText = oDecript.decrypt(cCripText)
cRetMsg = cDecText.decode()
print(cRetMsg)
sleep(5)
