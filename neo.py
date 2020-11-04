import socket

from mocket.compat import encode_to_bytes


class Neo(object):
    def __init__(self, addr=None):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(addr or ('localhost', 8080))

    def iknow(self):
        self._fp = self.sock.makefile('rb')
        self.sock.sendall(encode_to_bytes('I know kung fu.\r\n'))
        return self._fp.read().strip() == encode_to_bytes('Show me.')


if __name__ == '__main__':
    neo = Neo()
    print(neo.iknow())
