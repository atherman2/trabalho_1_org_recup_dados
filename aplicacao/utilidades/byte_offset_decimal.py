def byte_offset_d(arqv: str, id: str) -> int:
    ''' Toma como entrada uma String "arqv" correspondente ao nome de um arquivo e outra String 
    "id" correspondente ao id de um registro do já citado arquivo. Retorna o byte-offset do id.
    >>> byte_offset('dados.dat', '1')
    4
    >>> byte_offset('dados.dat', '2')
    86
    >>> byte_offset('dados.dat', '3')
    169
    >>> byte_offset('dados.dat', '13')
    743
    >>> byte_offset('dados.dat', '100')
    6386
    >>> byte_offset('dados.dat', 'UwU')
    -1
    '''
    
    entrada = open(arqv, 'rt')
    leitura = entrada.read(4) #leitura do cabeçalho que aqui aparentemente tem 12 bytes por alguma
    # razão, mas qualquer coisa é só mudar para 4.
    
    # Conferindo se o arquivo possui registros.
    if leitura == '':
        raise ValueError("O arquivo é inválido, pois não possui cabeçalho")
    
    # Essa varíável vai armazenando o byte offset de cada id até que o requisitado seja encontrado.
    offset_atual = 4
    
    # Laço que procura o id, compara para ver se é o requisitado e passa para o próximo caso não
    # Laço para caso o id seja encontrado ou o arquivo acabe.
    while (leitura := entrada.read(2)) != '' :
        tam_regis = ord(leitura[0]) + ord(leitura[1])
        id_atual = ''
        num_bytes_lidos_id_atual = 1
        caractere_atual = entrada.read(1)
        # Encontra o id certinho.
        while caractere_atual != '|':
            id_atual += caractere_atual
            num_bytes_lidos_id_atual += 1
            caractere_atual = entrada.read(1)
        # Compara para ver se é o certo.
        if id_atual == id:
            return offset_atual
        #Passa para o próximo.
        else:
            leitura = entrada.read(tam_regis - num_bytes_lidos_id_atual)
            offset_atual += tam_regis + 2 # "O + 2" refere-se aos campos que indicam o tamanho do registro 
    return -1