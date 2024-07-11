# onde vai ficar a aplicação principal
# provavelmente o menu principal que ficou comigo, Alex
import os, io
import funcionalidades as f

arq:io.BufferedReader = open("./aplicacao/dados.dat", "rb")
f.busca(arq, "22")