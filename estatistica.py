import numpy as np

data = []

with open("batchn1000servidorrede.txt", "r") as my_file:
    linhas = my_file.readlines()
    for linha in linhas:
        data.append(float(linha))

media = np.mean(data)

desvio_padrao = np.std(data)

coef_variacao = (desvio_padrao / media) * 100

print(f"Média: {media}")
print(f"Desvio padrão: {desvio_padrao}")
print(f"Coeficiente de variação: {coef_variacao}")