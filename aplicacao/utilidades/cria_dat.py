arq = open('./aplicacao/utilidades/t1.dat', 'r+b')

num_1 = 30
bin_num_1 = num_1.to_bytes(4)
bytes_1 = bytes(26)

arq.write(bin_num_1)
arq.write(bytes_1)

tam = []
tam.append(28)
tam[0] = tam[0].to_bytes(2)
arq.write(tam[0])
arq.write('*'.encode())
num_2 = 60
bin_num_2 = num_2.to_bytes(4)
arq.write(bin_num_2)

bytes_2 = bytes(23)
arq.write(bytes_2)

arq.write(tam[0])
arq.write('*'.encode())
num_3 = 90
bin_num_3 = num_3.to_bytes(4)
arq.write(bin_num_3)

arq.close()
