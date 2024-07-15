from utilidades import byte_offset_d
import funcionalidades as f

def remove_registro(arqv: str, id: str) -> None:
    '''Toma como entrada um arquivo arqv e um id e remove o registro correspondente, deixando o
    espaço disponível para novas inserções a partir de uma LED worst fit.'''
    byte_os_id = byte_offset_d(arqv, id)
    tam_id = tam_reg_id(arqv, id)
    f.insere_na_LED(arqv, byte_os_id, tam_id)

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
    byte_offset_id = byte_offset_d(arqv, id)
    return tam_reg_byte_os(arqv, byte_offset_id)

remove_registro('a.dat', '9')