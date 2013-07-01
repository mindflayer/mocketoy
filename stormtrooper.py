import asyncore
import socket


class StormTrooperClient(asyncore.dispatcher):
    def __init__(self, addr=None):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect(addr or ('localhost', 8080))
        self.buffer = 'Let me see your identification.\r\n'

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):
        data = self.recv(8192).strip()
        print data
        if data == 'You don\'t need to see his identification.':
            print 'Move along... move along.'

    def writable(self):
        return len(self.buffer) > 0

    def handle_write(self):
        print self.buffer.strip()
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

    def handle_error(self):
        pass


if __name__ == '__main__':
    client = StormTrooperClient()
    asyncore.loop()
