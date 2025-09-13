import rpyc
import time


class MyService(rpyc.Service):
    def on_connect(self, conn):
        # código que é executado quando uma conexão é iniciada, caso seja necessário
        pass

    def on_disconnect(self, conn):
        # código que é executado quando uma conexão é finalizada, caso seja necessário
        pass

    def exposed_get_sum(self, raw_data):
        v = list(raw_data)
        start = time.time()
        s = 0
        for i in range(len(v)):
            s += v[i]

        end = time.time()
        tempo = end - start
        print(tempo)

        with open("output_server_vetor.txt", "a") as my_file:
            my_file.write(str(tempo) + "\n")
        return s


# Para iniciar o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    t = ThreadedServer(MyService, port=18861)
    t.start()

