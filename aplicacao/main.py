# onde vai ficar a aplicação principal
# provavelmente o menu principal que ficou comigo, Alex
import os, io
import funcionalidades as f
import utilidades as u

a = open('aplicacao/dados.dat', 'r+b')
f.remove_registro_b(a, '100')
f.imprime_mensagem_LED(f.matriz_LED(a))