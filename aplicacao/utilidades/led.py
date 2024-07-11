import os, io

class Membro_led:
    def __init__(self) -> None:
        self.byte_offset:int = 0
        self.tam:int = 0
        self.prox:int = 0

def remove_da_led(arq: io.BufferedRandom, b_o_ant) -> Membro_led:
    byte_offset_inicial = arq.tell()
    arq.seek(b_o_ant, os.SEEK_SET)

    b_o_regis = int.from_bytes(arq.read(4))
    
    antigo_primeiro = Membro_led()
    antigo_primeiro.byte_offset = b_o_regis
    
    arq.seek(b_o_regis, os.SEEK_SET)
    antigo_primeiro.tam = int.from_bytes(arq.read(2))

    arq.seek(1, os.SEEK_CUR)
    prox = int.from_bytes(arq.read(4))
    antigo_primeiro.prox = prox

    arq.seek(0, os.SEEK_SET)
    bin_prox = prox.to_bytes(4)
    arq.write(bin_prox)
    
    arq.seek(byte_offset_inicial, os.SEEK_SET)
    return antigo_primeiro
