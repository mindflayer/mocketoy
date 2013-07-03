import asyncore
import socket


class MorpheusHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(8192).strip()
        if data == 'I know kung fu.':
            reply = 'Show me.'
        else:
            reply = 'Blue Pill.'
        self.send(reply + '\r\n')
        self.close()


class Morpheus(asyncore.dispatcher):
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
            MorpheusHandler(sock)

    def handle_error(self):
        pass

if __name__ == '__main__':
    server = Morpheus('localhost', 8080)
    asyncore.loop()
