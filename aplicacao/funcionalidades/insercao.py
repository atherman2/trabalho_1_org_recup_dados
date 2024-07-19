import io, os
import utilidades as u

def insere_registro(arq: io.BufferedRandom, registro: str) -> None:
    chave = registro.split('|')[0]
    byte_offset_inicial: int = arq.tell()
    tam_regis: int = len(registro)
    tam_disp: int = u.tam_regis_da_led(arq, 0)
    print(f'Inserção do registro de chave "{chave}" ({tam_regis} bytes)')
    if tam_disp >= tam_regis:
        # b_o_primeiro_da_led = u.b_o_prox_da_led(arq, 0)
        primeiro_da_led: u.Membro_led = u.remove_da_led(arq, 0)
        b_o_1o_led = primeiro_da_led.byte_offset
        insere_registro_2(arq, registro, b_o_1o_led)
        print(f'Local: offset = {b_o_1o_led} bytes (){hex(b_o_1o_led)}')
        if tam_disp - tam_regis >= 32:
            pass
            #insere_na_led(arq, primeiro_da_led, tam_regis)
    else:
        insere_registro_2(arq, registro, -1)
    arq.seek(byte_offset_inicial, os.SEEK_SET)

def insere_registro_2(arq: io.BufferedRandom, registro: str, byte_offset: int) -> None:
    byte_offset_inicial = arq.tell()
    if byte_offset == -1:
        arq.seek(0, os.SEEK_END)
    else:
        arq.seek(byte_offset, os.SEEK_SET)
    registro = registro.encode()
    arq.write(registro)
    arq.seek(byte_offset_inicial, os.SEEK_SET)