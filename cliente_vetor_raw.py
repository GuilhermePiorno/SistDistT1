import rpyc
import sys
import random
import time

start = time.time()
if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

output_name = "cliente_"
suffix = str(sys.argv[2])
output_name += suffix
output_name += ".txt"

server = sys.argv[1]

tam = int(sys.argv[2])
vet = [random.randint(0, tam - 1) for _ in range(tam)]
raw_data = bytes(vet)

c = rpyc.connect(server, 18861)
c._config['sync_request_timeout'] = None

sum = c.root.get_sum(raw_data)

end = time.time()
tempo = end - start

print(end - start)
with open(output_name, "a") as my_file:
    my_file.write(str(tempo) + "\n")

