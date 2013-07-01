import socket


class Stormtrooper(object):
    def __init__(self, addr=None):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(addr or ('localhost', 8080))

    def identify(self):
        self._fp = self.sock.makefile('rb')
        self.sock.sendall('Let me see your identification.\r\n')
        return self._fp.read().strip() == 'You don\'t need to see his identification.'


if __name__ == '__main__':
    st = Stormtrooper()
    print st.identify()
