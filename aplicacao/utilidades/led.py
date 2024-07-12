import os, io

class Membro_led:
    def __init__(self) -> None:
        self.byte_offset:int = 0
        self.tam:int = 0
        self.prox:int = 0

def acessa_prox_led(arq: io.BufferedRandom, b_o_ant: int) -> None:
    arq.seek(b_o_ant, os.SEEK_SET)

    b_o_regis = int.from_bytes(arq.read(4))
    arq.seek(b_o_regis)

def tam_regis_da_led(arq: io.BufferedRandom, b_o_ant: int) -> int:
    byte_offset_inicial = arq.tell()
    acessa_prox_led(arq, b_o_ant)

    tam_regis = arq.read(2)
    tam_regis = int.from_bytes(tam_regis)

    arq.seek(byte_offset_inicial, os.SEEK_SET)
    return tam_regis


def remove_da_led(arq: io.BufferedRandom, b_o_ant: int) -> Membro_led:
    byte_offset_inicial = arq.tell()
    
    acessa_prox_led(arq, b_o_ant)
    b_o_regis = arq.tell()

    antigo_primeiro = Membro_led()
    antigo_primeiro.byte_offset = b_o_regis
    
    antigo_primeiro.tam = int.from_bytes(arq.read(2))

    arq.seek(1, os.SEEK_CUR)
    prox = int.from_bytes(arq.read(4))
    antigo_primeiro.prox = prox

    arq.seek(0, os.SEEK_SET)
    bin_prox = prox.to_bytes(4)
    arq.write(bin_prox)
    
    arq.seek(byte_offset_inicial, os.SEEK_SET)
    return antigo_primeiro
