import utilidades as u
import funcionalidades as f

def insere_na_LED(arqv:str, os:int, tam:int) -> None:
    '''Toma como entrada um arquivo "arqv", o byte offset "os" de um registro e o tamanho "tam"
    desse registro. Com isso, insere esses valores na LED do arquivo'''
    if os < 0 or tam < 0:
        return None
    entrada = open(arqv, 'r+t')
    percorre_LED = entrada.read(4)
    escrita =  ((4 - len(str(os))) * ' ') + str(os)
    if percorre_LED == '  -1':
        entrada.seek(os + 2)
        entrada.write('*  -1')
        entrada.seek(0)
        entrada.write(escrita)
    else:
        byte_os_LED = int(percorre_LED)
        tam_LED = f.tam_reg_byte_os(arqv, byte_os_LED)
        if tam >= tam_LED:
            entrada.seek(os + 2)
            entrada.write('*' + percorre_LED)
            entrada.seek(0)
            entrada.write(escrita)
        else:
            byte_os_LED_seek = 0
            while tam < tam_LED and percorre_LED != '  -1':
                byte_os_LED_seek = byte_os_LED
                entrada.seek(byte_os_LED + 3)
                percorre_LED = entrada.read(4)
                byte_os_LED = int(percorre_LED)
                tam_LED = f.tam_reg_byte_os(arqv, byte_os_LED)
            entrada.seek(os + 2)
            entrada.write('*' + percorre_LED)
            entrada.seek(byte_os_LED_seek + 2)
            entrada.write('*' + escrita)