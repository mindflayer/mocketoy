import asyncore
import socket


class Morpheus(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(8192).strip()
        if data == 'I know kung fu.':
            reply = 'Show me.'
        else:
            reply = 'Blue Pill.'
        self.send(reply + '\r\n')
        self.close()


class MorpheusServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            Morpheus(sock)

    def handle_error(self):
        pass

if __name__ == '__main__':
    server = MorpheusServer('localhost', 8080)
    asyncore.loop()
