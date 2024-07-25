import io
import funcionalidades as f

def matriz_LED(entrada: io.BufferedReader) -> list[list[int]]:
    ''' Toma como entrada um arquivo já aberto/interpretado "entrada". Retorna uma matriz que
    armazena os valores dos byte offset e tamanhos dos espaços disponíveis da LED'''
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

def imprime_mensagem_LED(matriz_LED:list[list[int]]) -> str:
    ''' Toma como entrada a matriz retornada pela função "matriz_LED", que armazena os valores dos
    byte offset e tamanhos dos espaços disponíveis da LED. Retorna uma Strig com a formatação
    correta dos valores já descritos. Além disso, printa-a'''
    mensagem:str = 'LED '
    for i in matriz_LED:
        mensagem += '-> [offset: ' + str(i[0]) + ', tam: '+ str(i[1]) + '] '
    mensagem += '-> [offset: -1] \n Total: ' + str(len(matriz_LED)) + ' espacos disponiveis'
    print(mensagem)
    return mensagem