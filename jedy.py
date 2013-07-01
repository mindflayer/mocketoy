import asyncore
import socket


class JedyHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(8192).strip()
        print 'Stormtrooper: {0!r}'.format(data)
        if data == 'Let me see your identification.':
            reply = 'You don\'t need to see his identification.'
        else:
            reply = 'W0T???'
        print 'Obi-Wan: {0!r}'.format(reply)
        self.send(reply + '\r\n')
        self.close()


class JedyServer(asyncore.dispatcher):
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
            JedyHandler(sock)

    def handle_error(self):
        pass

if __name__ == '__main__':
    server = JedyServer('localhost', 8080)
    asyncore.loop()
