import glob
import math
import sys

for filename in glob.glob("*.txt"):
    dados = []
    n = 0
    s = 0
    var = 0
    desvio = 0
    dispersao = 0
    with open(filename, "r") as my_file:
        for line in my_file:
            n += 1
            line = line.strip()
            dados.append(float(line))
            s+= float(line)
        avg = sum(dados)/n

    for number in dados:
        var = sum((x - avg)**2 for x in dados)/n
    desvio = math.sqrt(var)
    dispersao = desvio/avg


    print("=========")
    print(f"Filename: {filename}")
    print(f"numero de dados: {n}")
    print(f"avg: {avg}")
    print(f"desvio: {desvio}")
    print(f"dispersão: {dispersao*100}")
    # print(f"variancia: {var}")
    

