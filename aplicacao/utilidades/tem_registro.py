import os, io
def tem_registro(arq:io.BufferedReader):
    byte_offset_inicial = arq.tell()
    bin_lido = arq.read(1)
    if ord(bin_lido) == 255:
        lido = '1'
    else:
        lido = bin_lido.decode()
    #lido:bytearray = arq.read(3)
    #lido = lido[2].decode()
    arq.seek(byte_offset_inicial, os.SEEK_SET)
    return lido