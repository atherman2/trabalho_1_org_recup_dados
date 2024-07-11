import io, os
import utilidades as u
#from utilidades.le_chave import le_chave

# def busca(arq:io.BufferedReader, chave:str):
def busca(arq: io.BufferedReader, chave:str):
    byte_offset_inicial = arq.tell()
    bin_cabecalho = arq.read(4)
    contador = 1
    while u.tem_registro(arq):
        #print(u.le_chave())
        u.le_chave()
        print(contador)
        tam_regis:int = int.from_bytes(arq.read(2))
        arq.seek(tam_regis, os.SEEK_CUR)
        contador += 1
