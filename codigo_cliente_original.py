import rpyc
import sys

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

conn = rpyc.connect(server, 18861)

p1 = c.root
p2 = c.root.get_answer()
p3 = c.root.the_real_answer_though

print(p1)
print(p2)
print(p3)
