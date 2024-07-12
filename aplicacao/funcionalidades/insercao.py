import io, os
import utilidades as u

def insere_registro(arq: io.BufferedRandom, registro: str) -> None:
    byte_offset_inicial: int = arq.tell()
    tam_regis: int = len(registro)
    tam_disp: int = u.tam_regis_da_led(arq, 0)
    if tam_regis >= tam_disp:
        # b_o_primeiro_da_led = u.b_o_prox_da_led(arq, 0)
        primeiro_da_led: u.Membro_led = u.remove_da_led(arq, 0)
        insere_registro(arq, registro, primeiro_da_led.byte_offset)
        if tam_disp - tam_regis >= 32:
            insere_registro(arq, registro, u.b_o_eof(arq))

def insere_registro(arq: io.BufferedRandom, registro: str, byte_offset: int) -> None:
    byte_offset_inicial = arq.tell()
    arq.seek(byte_offset, os.SEEK_SET)
    registro = registro.encode()
    arq.write(registro)
    arq.seek(byte_offset_inicial, os.SEEK_SET)