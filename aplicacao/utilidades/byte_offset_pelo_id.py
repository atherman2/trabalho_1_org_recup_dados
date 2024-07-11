import io
import os

def byte_offset(entrada: io.BufferedReader, id: str) -> int:
    ''' Toma como entrada uma String "arqv" correspondente ao nome de um arquivo e outra String 
    "id" correspondente ao id de um registro do já citado arquivo. Retorna o byte-offset do id.
    >>> byte_offset('dados.dat', '1')
    12
    >>> byte_offset('dados.dat', '2')
    94
    >>> byte_offset('dados.dat', '3')
    177
    >>> byte_offset('dados.dat', '13')
    751
    >>> byte_offset('dados.dat', '100')
    6394
    >>> byte_offset('dados.dat', 'UwU')
    Traceback (most recent call last):
    ...
    ValueError: O id não está no arquivo
    '''
    
    byte_offset:int = entrada.tell()
    entrada.seek(0,os.SEEK_SET)

    leitura:bytearray = entrada.read(4) #leitura do cabeçalho que aqui aparentemente tem 12 bytes por alguma
    # razão, mas qualquer coisa é só mudar para 4.
    
    # Conferindo se o arquivo possui registros.
    leitura = '0'.encode()
    if leitura.decode() == '':
        entrada.seek(byte_offset, os.SEEK_SET)
        raise ValueError("O arquivo é inválido, pois não possui cabeçalho")
    
    # Essa varíável vai armazenando o byte offset de cada id até que o requisitado seja encontrado.
    offset_atual:int = 4
    
    # Laço que procura o id, compara para ver se é o requisitado e passa para o próximo caso não
    # Laço para caso o id seja encontrado ou o arquivo acabe.
    while (leitura := entrada.read(2)).decode() != '' :
        tam_regis:int = int.from_bytes(leitura)
        id_atual:str = ''
        num_bytes_lidos_id_atual:int = 1
        caractere_atual:str = entrada.read(1).decode()
        # Encontra o id certinho.
        while caractere_atual != '|':
            id_atual += caractere_atual
            num_bytes_lidos_id_atual += 1
            caractere_atual = entrada.read(1).decode()
        # Compara para ver se é o certo.
        if id_atual == id:
            entrada.seek(byte_offset, os.SEEK_SET)
            return offset_atual
        # Passa para o próximo.
        else:
            leitura = entrada.read(tam_regis - num_bytes_lidos_id_atual).decode()
            offset_atual += tam_regis + 2 # "O + 2" refere-se aos campos que indicam o tamanho do registro.
    entrada.seek(byte_offset, os.SEEK_SET)
    raise ValueError("O id não está no arquivo")