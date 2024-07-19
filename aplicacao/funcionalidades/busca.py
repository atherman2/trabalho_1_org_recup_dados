import io, os
import utilidades as u
#from utilidades.le_chave import le_chave

# def busca(arq:io.BufferedReader, chave:str):
def busca(arq: io.BufferedReader, chave:str):
    print(f'Busca pelo registro de chave "{chave}"')
    byte_offset_inicial = arq.tell()
    #bin_cabecalho = arq.read(4)
    #contador = 1
    #while u.tem_registro(arq):
    #    print(u.le_chave())
    #    u.le_chave()
    #    print(contador)
    #    tam_regis:int = int.from_bytes(arq.read(2))
    #    arq.seek(tam_regis, os.SEEK_CUR)
    #    contador += 1

    byte_offset_com_a_chave = u.byte_offset(arq, chave)
    arq.seek(byte_offset_com_a_chave, os.SEEK_SET)
    u.le_registro(arq)
    arq.seek(byte_offset_inicial, os.SEEK_SET)
