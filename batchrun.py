import subprocess
import sys

if len(sys.argv) < 3:
    exit("Argumentos necessários: \narg1: server_addr, \narg2: vet_size, \narg3: num_execucoes")

server = sys.argv[1]
tam = sys.argv[2]
n = int(sys.argv[3])

for _ in range(n):
    subprocess.run(["python3", "cliente_vetor.py", server, tam])
