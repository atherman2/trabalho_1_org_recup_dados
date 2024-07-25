import utilidades as u
import funcionalidades as f
import io

def remove_registro_b(entrada: io.BufferedReader, id: str) -> None:
    ''' Toma como entrada um arquivo já aberto/interpretado "entrada" e um id e remove o registro
    correspondente, deixando o espaço disponível para novas inserções a partir de uma LED worst
    fit. Além disso, printa se a operação foi realizada ou não '''
    # "byte_os_id" armazena o valor do byte_offset do id lido
    byte_os_id = u.byte_offset_b(entrada, id)
    # o byte offset -1 aqui representa o valor inválido
    if byte_os_id == -1:
        print('Remoção do registro de chave "' + id + '"\nErro: registro não encontrado!')
    # "tam_id" armazena o valor do tamanho do registro com o id lido
    else:
        tam_id = tam_reg_id_b(entrada, id)
        f.insere_na_LED_b(entrada, byte_os_id, tam_id, False)
        print('Remoção do registro de chave "' + id + '"\nRegistro removido! (' + str(tam_id) + ' bytes)\nLocal: offset = ' + str(byte_os_id) + ' bytes (' + str(hex(byte_os_id)) + ')')

def tam_reg_byte_os_b(entrada: io.BufferedReader, byte_offset_id: int) -> int:
    ''' Toma como entrada um arquivo já aberto/interpretado "entrada" e um byte offset de um
    registro e retorna o tamanho desse registro '''
    if byte_offset_id < 0:
        return -1
    entrada.seek(byte_offset_id)
    leitura = entrada.read(2)
    entrada.seek(0)
    return int.from_bytes(leitura, 'big', signed = True)

def tam_reg_id_b(entrada: io.BufferedReader, id: str) -> int:
    ''' Toma como entrada um arquivo já aberto/interpretado "entrada" e um id de um registro e
    retorna o tamanho desse registro '''
    byte_offset_id = u.byte_offset_b(entrada, id)
    return tam_reg_byte_os_b(entrada, byte_offset_id)