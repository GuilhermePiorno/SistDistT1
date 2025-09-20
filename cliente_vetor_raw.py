import rpyc
import sys
import random
import time

start = time.time()
if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

tam = int(sys.argv[2])
vet = [random.randint(0, tam - 1) for _ in range(tam)]
raw_data = bytes(vet)

c = rpyc.connect(server, 18861)
c._config['sync_request_timeout'] = None

sum = c.root.get_sum(raw_data)

end = time.time()
tempo = end - start

# print("sum: " + str(sum))
print(end - start)
with open("output_cliente_vetor.txt", "a") as my_file:
    # my_file.write(str(sum)+"\n")
    my_file.write(str(tempo) + "\n")

