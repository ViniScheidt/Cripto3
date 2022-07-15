import text_chunk
#Chave privada
with open('private.txt') as file:
    lines = file.readlines()

#separando chave privada
modulusStr = (lines[0])
modulus = int(modulusStr)
keyStr = (lines[1])
key = int(keyStr)


with open('dest.txt') as file:
    linesEcp = file.readlines()
    linesEcp1 = ''.join(linesEcp)

   

