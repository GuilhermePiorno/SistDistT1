import rpyc
import time

class MyService(rpyc.Service):
    def on_connect(self, conn):
        # código que é executado quando uma conexão é iniciada, caso seja necessário
        pass

    def on_disconnect(self, conn):
        end = time.time()
        tempo = end - self.start
        with open("output_server.txt", "a") as my_file:
            my_file.write(str(tempo)+"\n")

    def exposed_get_answer(self):  # este é um método exposto
        self.start = time.time()
        return 42

    exposed_the_real_answer_though = 43  # este é um atributo exposto

    def get_question(self):  # este método não é exposto
        return "Qual é a cor do cavalo branco de Napoleão?"


# Para iniciar o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    t = ThreadedServer(MyService, port=18861)
    t.start()

