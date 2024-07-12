import utilidades as u

def testa_dat() -> None:
    arq = open('./aplicacao/utilidades/t1.dat', 'r+b')

    regis = u.remove_da_led(arq,0)
    print(regis.byte_offset, regis.tam, regis.prox)

    arq.close()
