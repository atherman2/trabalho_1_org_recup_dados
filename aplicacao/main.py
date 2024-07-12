# onde vai ficar a aplicação principal
# provavelmente o menu principal que ficou comigo, Alex
import os, io, sys
import funcionalidades as f
import utilidades as u

#arq:io.BufferedReader = open("./aplicacao/dados.dat", "rb")
#f.busca(arq, "22")

#u.testa_dat()
if __name__ == '__main__':
    arq = open('./aplicacao/dados2.dat', 'rb')
    f.busca(arq, '22')
    arq.close()
    '''if sys.argv[1] == '-e':
        arq_operacoes: io.BufferedReader = open(sys.argv[2], 'rt')
        while (leitura := arq_operacoes.readline()):
            if leitura[0] == 'b':
                arq: io.BufferedReader = open('./aplicacao/dados2.dat', 'rb')
                f.busca(arq, leitura[2:])
                print()
                arq.close()
            if leitura[0] == 'i':
                arq: io.BufferedRandom = open('./aplicacao/dados2.dat', 'r+b')
                f.insere_registro(arq, leitura[2:])
                print('/')
'''
#f.insere_registro(open('./aplicacao/dados2.dat', 'r+b'), '1|2|3|4|5|6|')
