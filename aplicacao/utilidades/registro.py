import io, os

def le_registro(arq:io.BufferedReader) -> None:
    byte_offset_inicial = arq.tell()
    tam_regis = int.from_bytes(arq.read(2))
    registro = arq.read(tam_regis).decode()
    print(f'{registro} ({tam_regis} bytes)')
    arq.seek(byte_offset_inicial, os.SEEK_SET)