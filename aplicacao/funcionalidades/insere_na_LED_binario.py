import funcionalidades as f
import io

def insere_na_LED_b(entrada: io.BufferedReader, os:int, tam:int) -> None:
    '''Toma como entrada um arquivo "arqv", o byte offset "os" de um registro e o tamanho "tam"
    desse registro. Com isso, insere esses valores na LED do arquivo'''
    if os < 0 or tam < 0:
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
    entrada.seek(os + 2)
    entrada.write(b'*' + percorre_LED)
    entrada.seek(byte_os_LED_seek)
    entrada.write(os.to_bytes(4, 'big', signed = True))