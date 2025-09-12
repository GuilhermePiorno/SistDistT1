import rpyc
import sys
import time

start = time.time()

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

c = rpyc.connect(server, 18861)

p1 = c.root
p2 = c.root.get_answer()
p3 = c.root.the_real_answer_though

end = time.time()
tempo = end - start
with open("output_cliente.txt", "a") as my_file:
    my_file.write(str(tempo)+"\n")

print(p1)
print(p2)
print(p3)
