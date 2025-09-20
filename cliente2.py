import rpyc
import sys


if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

c = rpyc.connect(server, 18861)

# print(c.root.get_question)
# print(c.root.get_question()) # correta
print(c.get_question)
# print(c.get_question())
