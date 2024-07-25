import io, os
import utilidades as u
import funcionalidades as f

def insere_registro(arq: io.BufferedRandom, registro: str) -> None:
    chave = registro.split('|')[0]
    byte_offset_inicial: int = arq.tell()
    tam_regis: int = len(registro)
    tam_disp: int = u.tam_regis_da_led(arq, 0)
    print(f'Inserção do registro de chave "{chave}" ({tam_regis} bytes)')
    if tam_disp - 4 >= tam_regis:
        # b_o_primeiro_da_led = u.b_o_prox_da_led(arq, 0)
        primeiro_da_led: u.Membro_led = u.remove_da_led(arq, 0)
        b_o_1o_led = primeiro_da_led.byte_offset
        insere_registro_2(arq, registro, b_o_1o_led)
        if tam_disp - tam_regis >= 32:
            #insere_na_led(arq, primeiro_da_led, tam_disp - tam_regis - 2)
            b_o_restante = b_o_1o_led + tam_regis + 2
            tam_restante = tam_disp - tam_regis - 2
            #print(f'Tam_restante em insere_registro = {tam_restante}')
            f.insere_na_LED_b(arq, b_o_restante, tam_restante, True)
        else:
            b_o_restante = b_o_1o_led + tam_regis + 2
            arq.seek(b_o_restante, os.SEEK_SET)
            tam_restante = tam_disp - 2 - tam_regis
            bin_tam_restante = tam_restante.to_bytes(2, 'big', signed = True)
            arq.write(bin_tam_restante)
    else:
        insere_registro_2(arq, registro, -1)
    arq.seek(byte_offset_inicial, os.SEEK_SET)

def insere_registro_2(arq: io.BufferedRandom, registro: str, byte_offset: int) -> None:
    byte_offset_inicial = arq.tell()
    if byte_offset == -1:
        arq.seek(0, os.SEEK_END)
        print(f'Local: fim do arquivo')
    else:
        arq.seek(byte_offset, os.SEEK_SET)
        print(f'Local: offset = {byte_offset} bytes ({hex(byte_offset)})')
    registro = registro.encode()
    tam = (len(registro)).to_bytes(2, 'big', signed = True)
    arq.write(tam)
    arq.write(registro)
    arq.seek(byte_offset_inicial, os.SEEK_SET)