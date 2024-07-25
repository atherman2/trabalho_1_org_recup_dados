# onde vai ficar a aplicação principal
# provavelmente o menu principal que ficou comigo, Alex
import os, io, sys
import funcionalidades as f
import utilidades as u

#arq:io.BufferedReader = open("./aplicacao/dados.dat", "rb")
#f.busca(arq, "22")

#u.testa_dat()
if __name__ == '__main__':
    #arq = open('./aplicacao/dados2.dat', 'rb')
    #f.busca(arq, '22')
    #arq.close()
    endereco_arq = './aplicacao/dados_o2.dat'
    print()
    if sys.argv[1] == '-e':
        arq_operacoes: io.BufferedReader = open(sys.argv[2], 'rt')
        #leitura = arq_operacoes.readline()
        while (leitura := arq_operacoes.readline()):
            nova_leitura = ''
            for char in leitura:
                if char != '\n':
                    nova_leitura += char
            leitura = nova_leitura
            if len(leitura) > 0:
                if leitura[0] == 'b':
                    arq: io.BufferedReader = open(endereco_arq, 'rb')
                    f.busca(arq, leitura[2:])
                    print()
                    arq.close()
                elif leitura[0] == 'i':
                    arq: io.BufferedRandom = open(endereco_arq, 'r+b')
                    f.insere_registro(arq, leitura[2:])
                    print()
                    arq.close()
                elif leitura[0] == 'r':
                    arq: io.BufferedRandom = open(endereco_arq, 'r+b')
                    f.remove_registro_b(arq, leitura[2:])
                    print()
                    arq.close()
        arq_operacoes.close()
    elif sys.argv[1] == '-p':
        arq: io.BufferedReader = open(endereco_arq, 'rb')
        matriz = f.matriz_LED(arq)
        string = f.imprime_mensagem_LED(matriz)
        arq.close()
        #print(string)
        print()

#f.insere_registro(open('./aplicacao/dados2.dat', 'r+b'), '1|2|3|4|5|6|')
