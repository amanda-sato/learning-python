arquivo = float(input("Tamanho do arquivo (MB): "))
link = float(input("Velocidade de Internet (MBps): "))
tempo = (arquivo/link) / 60

print(f"Tempo de download (aproximado): {tempo:6.2f} Minutos ")
