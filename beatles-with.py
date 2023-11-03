with  open("beatles.txt", "r", encoding="utf8") as f:
    for line in f:
        print(line.strip())
# No se necesita f.close()