# Fazer matrix com os byte offsets e tamanhos de espaço disponíveis
# Deixar a formatação bonitinha numa String
# printar com a flag no main
import io
import funcionalidades as f
def matriz_LED(entrada: io.BufferedReader) -> list[list[int]]:
    '''Toma como entrada um arquivo "arqv", o byte offset "os" de um registro e o tamanho "tam"
    desse registro. Com isso, insere esses valores na LED do arquivo'''
    entrada.seek(0)
    percorre_LED = entrada.read(4)
    percorre_LED_int = int.from_bytes(percorre_LED, 'big', signed = True)
    m:list[list[int]] = []
    while percorre_LED_int != -1:
        m.append([percorre_LED_int, f.tam_reg_byte_os_b(entrada, percorre_LED_int)])
        entrada.seek(percorre_LED_int + 3)
        percorre_LED = entrada.read(4)
        percorre_LED_int = int.from_bytes(percorre_LED, 'big', signed = True)
    return m

def mensagem_LED(matriz_LED:list[list[int]]) -> str:
    mensagem:str = 'LED '
    for i in matriz_LED:
        mensagem += '-> [offset: ' + str(i[0]) + ', tam: '+ str(i[1]) + '] '
    mensagem += '-> [offset: -1] \n Total: ' + str(len(matriz_LED)) + ' espacos disponiveis'
    return mensagem