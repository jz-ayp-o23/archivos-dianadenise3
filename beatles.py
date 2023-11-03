f=open("beatles.txt", "r", encoding="utf8")
for line in f:
    print(line.strip())
# Siempre hay que cerrar el archivo al terminar de trabajar con él
f.close()