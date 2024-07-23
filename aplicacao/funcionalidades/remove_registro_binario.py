import utilidades as u
import funcionalidades as f
import io

def remove_registro_b(entrada: io.BufferedReader, id: str) -> None:
    '''Toma como entrada um arquivo arqv e um id e remove o registro correspondente, deixando o
    espaço disponível para novas inserções a partir de uma LED worst fit.'''
    byte_os_id = u.byte_offset_b(entrada, id)
    tam_id = tam_reg_id_b(entrada, id)
    f.insere_na_LED_b(entrada, byte_os_id, tam_id)

def tam_reg_byte_os_b(entrada: io.BufferedReader, byte_offset_id: int) -> int:
    '''Função que toma como entrada um aquivo arqv e um byte offset de um registro e retorna o tamanho desse
    registro.'''
    if byte_offset_id < 0:
        return -1
    entrada.seek(byte_offset_id)
    leitura = entrada.read(2)
    entrada.seek(0)
    return int.from_bytes(leitura, 'big', signed = True)

def tam_reg_id_b(entrada: io.BufferedReader, id: str) -> int:
    '''Função que toma como entrada um aquivo arqv e um id de um registro e retorna o tamanho desse
    registro.'''
    byte_offset_id = u.byte_offset_b(entrada, id)
    return tam_reg_byte_os_b(entrada, byte_offset_id)