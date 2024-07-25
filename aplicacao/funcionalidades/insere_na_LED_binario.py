import funcionalidades as f
import io

def insere_na_LED_b(entrada: io.BufferedReader, os:int, tam:int, insere_tam:bool) -> None:
    ''' Toma como entrada um arquivo já aberto/interpretado "entrada", o byte offset "os" de um
    registro, o tamanho "tam" desse registro e um booleano "insere_tam, que indica se é necessário
    escrever no arquivo o tamanho do espaço vazio. Com isso, insere esses valores na LED do arquivo
    '''
    # "percorre_LED" é onde fica armazenado os indicadores da LED (offsets ou -1) lidos em bytes;
    # "percorre_LED_int" é o valor de "percorre_LED" traduzido para inteiros;
    # "byte_os_LED_seek" é o int que representa onde deve ser inserido offset do registro inserido
    # "tam_LED" indica o tamanho do registro que estamos lendo atualmete na LED

    # Valores de byte offset ("os") e tamanho do registro ("tam") devem ser válidos.
    if os < 0 or tam < 0:
        return None
    
    entrada.seek(0)
    percorre_LED:bytes = entrada.read(4)
    percorre_LED_int:int = int.from_bytes(percorre_LED, 'big', signed = True)
    byte_os_LED_seek = 0
    while tam < (tam_LED := f.tam_reg_byte_os_b(entrada, percorre_LED_int)) and percorre_LED_int != -1:
        byte_os_LED_seek = percorre_LED_int + 3
        entrada.seek(byte_os_LED_seek)
        percorre_LED = entrada.read(4)
        percorre_LED_int = int.from_bytes(percorre_LED, 'big', signed = True)
    # Aqui é onde entra o condicional do booleano descrito na documentação da função
    if insere_tam:
        entrada.seek(os)
        entrada.write(tam.to_bytes(2, 'big', signed = True))
    else:
        entrada.seek(os + 2)
    # Escreve o offset que tomamos o lugar no nosso antigo espaço
    entrada.write(b'*' + percorre_LED)
    entrada.seek(byte_os_LED_seek)
    # Escreve o nosso offset no espaço onde ficava o outro
    entrada.write(os.to_bytes(4, 'big', signed = True))
    entrada.seek(0)