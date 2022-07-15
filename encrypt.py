import base64
from distutils.command.build_scripts import first_line_re
from turtle import position
import text_chunk

#Chave pública
with open('public.txt') as file:
    lines = file.readlines()

#separando modulo e chave
modulusStr = (lines[0])
modulus = int(modulusStr)
keyStr = (lines[1])
key = int(keyStr)

  
#source
with open('source.txt') as file:
    linesSrc = file.readlines()
    linesSrc1 = ''.join(linesSrc)
    

#gerando os chunks
chunk_size = text_chunk.block_size(modulus)

#transformando para b64
encoded_source = base64.b64encode(bytes(linesSrc1, "utf-8"))



chunks = [encoded_source[i:i + chunk_size] for i in range(0, len(encoded_source), chunk_size)]

encoded_chunks = []


for chunk in chunks: 
    original_chunk = text_chunk._int_to_str(chunk).int_value()
    encoded_chunk = pow(original_chunk,key, modulus)
    encoded_chunks.append(str(encoded_chunk))





        