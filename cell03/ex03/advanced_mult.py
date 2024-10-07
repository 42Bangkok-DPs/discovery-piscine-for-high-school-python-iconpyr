num = 0

while num <= 10:
    j = 0
    table = []

    while j <= 10:
        x = table.append(num*j)
        j+=1

    print(f"table de {num} : {' '.join(map(str, table))}")

    num += 1
