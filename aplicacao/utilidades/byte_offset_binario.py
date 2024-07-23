import io

def byte_offset_b(entrada: io.BufferedReader, id: str) -> int:
    ''' Toma como entrada um arquivo aberto em modo 'r+b' e uma String "id" correspondente ao id de
    um registro do já citado arquivo. Retorna o byte-offset do id.
    >>> a = open('dados.dat', 'r+b')
    >>> byte_offset_b(a, '1')
    4
    >>> byte_offset_b(a, '2')
    86
    >>> byte_offset_b(a, '3')
    169
    >>> byte_offset_b(a, '13')
    743
    >>> byte_offset_b(a, '100')
    6386
    >>> byte_offset_b(a, 'UwU')
    -1
    '''
    
    leitura = entrada.read(4) #leitura do cabeçalho com 4 bytes
    
    # Conferindo se o arquivo possui registros.
    if leitura == b'':
        raise ValueError("O arquivo é inválido, pois não possui cabeçalho")
    
    # Essa varíável vai armazenando o byte offset de cada id até que o requisitado seja encontrado.
    offset_atual = 4
    
    # Laço que procura o id, compara para ver se é o requisitado e passa para o próximo caso não
    # Laço para caso o id seja encontrado ou o arquivo acabe.
    while (leitura := entrada.read(2)) != b'' :
        tam_regis = int.from_bytes(leitura, 'big', signed = True)
        id_atual = b''
        num_b = 1 # Número de bytes lidos atual
        caractere_atual = entrada.read(1)
        # Encontra o id certinho.
        while caractere_atual != b'|':
            id_atual += caractere_atual
            num_b += 1
            caractere_atual = entrada.read(1)
        # Compara para ver se é o certo.
        if id_atual == id.encode():
            entrada.seek(0)
            return offset_atual
        #Passa para o próximo.
        else:
            entrada.read(abs(tam_regis - num_b))
            offset_atual += tam_regis + 2 # "O + 2" refere-se aos campos que indicam o tamanho do registro 
    entrada.seek(0)
    return -1