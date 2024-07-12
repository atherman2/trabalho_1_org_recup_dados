import utilidades as u

def remove_registro(arqv: str, id: str) -> None:
    '''Toma como entrada um arquivo arqv e um id e remove o registro correspondente, deixando o
    espaço disponível para novas inserções a partir de uma LED worst fit.'''
    entrada = open(arqv, 'r+t')
    byte_os_id = u.byte_offset_d(arqv, id)
    if byte_os_id == -1:
        return None # Ou raise ValueError
    escrita_id =  ((4 - len(str(byte_os_id))) * ' ') + str(byte_os_id)
    tam_id = tam_reg_id(arqv, id)
    percorre_LED = entrada.read(4)
    if percorre_LED == '  -1':
        entrada.seek(byte_os_id + 2)
        entrada.write('*  -1')
        entrada.seek(0)
        entrada.write(escrita_id)
    else:
        byte_os_LED = int(percorre_LED)
        tam_LED = tam_reg_byte_os(arqv, byte_os_LED)
        if tam_id >= tam_LED:
            entrada.seek(byte_os_id + 2)
            entrada.write('*' + percorre_LED)
            entrada.seek(0)
            entrada.write(escrita_id)
        else:
            byte_os_LED_seek = 0
            while tam_id < tam_LED and percorre_LED != '  -1':
                byte_os_LED_seek = byte_os_LED
                entrada.seek(byte_os_LED + 3)
                percorre_LED = entrada.read(4)
                byte_os_LED = int(percorre_LED)
                tam_LED = tam_reg_byte_os(arqv, byte_os_LED)
            entrada.seek(byte_os_id + 2)
            entrada.write('*' + percorre_LED)
            entrada.seek(byte_os_LED_seek + 2)
            entrada.write('*' + escrita_id)

def tam_reg_byte_os(arqv: str, byte_offset_id: int) -> int:
    '''Função que toma como entrada um aquivo arqv e um byte offset de um registro e retorna o tamanho desse
    registro.'''
    if byte_offset_id < 0:
        return -1
    entrada = open(arqv, 'rt')
    entrada.seek(byte_offset_id)
    leitura = entrada.read(2)
    return ord(leitura[0]) + ord(leitura[1])

def tam_reg_id(arqv: str, id: str) -> int:
    '''Função que toma como entrada um aquivo arqv e um id de um registro e retorna o tamanho desse
    registro.'''
    byte_offset_id = u.byte_offset_d(arqv, id)
    return tam_reg_byte_os(arqv, byte_offset_id)

remove_registro('a.dat', '17')
