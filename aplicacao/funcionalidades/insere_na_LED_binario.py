import funcionalidades as f
import io, os

def insere_na_LED_b(entrada: io.BufferedReader, offset:int, tam:int, insere_tam:bool) -> None:
    '''Toma como entrada um arquivo "arqv", o byte offset "os" de um registro e o tamanho "tam"
    desse registro. Com isso, insere esses valores na LED do arquivo'''
    if offset < 0 or tam < 0:
        return None
    entrada.seek(0)
    percorre_LED = entrada.read(4)
    percorre_LED_int = int.from_bytes(percorre_LED, 'big', signed = True)
    byte_os_LED_seek = 0
    while tam < (tam_LED := f.tam_reg_byte_os_b(entrada, percorre_LED_int)) and percorre_LED_int != -1:
        byte_os_LED_seek = percorre_LED_int + 3
        entrada.seek(byte_os_LED_seek)
        percorre_LED = entrada.read(4)
        percorre_LED_int = int.from_bytes(percorre_LED, 'big', signed = True)
    if insere_tam:
        entrada.seek(offset)
        if tam == 10:
            sub_tam = 4
            bin_sub_tam = sub_tam.to_bytes(2, 'big', signed = True)
            entrada.write(bin_sub_tam)
            entrada.seek(sub_tam, os.SEEK_CUR)
            entrada.write(bin_sub_tam)
        elif tam == 13:
            sub_tam = 4
            bin_sub_tam = sub_tam.to_bytes(2, 'big', signed = True)
            entrada.write(bin_sub_tam)
            entrada.seek(sub_tam, os.SEEK_CUR)
            sub_tam = 7
            bin_sub_tam = sub_tam.to_bytes(2, 'big', signed = True)
            entrada.write(bin_sub_tam)
        else:
            entrada.write(tam.to_bytes(2, 'big', signed = True))
    else:
        entrada.seek(offset + 2)
    entrada.write(b'*' + percorre_LED)
    entrada.seek(byte_os_LED_seek)
    entrada.write(offset.to_bytes(4, 'big', signed = True))
    entrada.seek(0)