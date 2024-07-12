import io, os
import utilidades as u

def insere_registro(arq: io.BufferedRandom, registro: str) -> None:
    tam_regis = len(registro)
    tam_disp: int = u.tam_regis_da_led(arq, 0)