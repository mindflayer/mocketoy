from mocket.registry import AbstractEntry, Mocket


class Droid(AbstractEntry):
    request_cls = str
    response_cls = str

    def can_handle(self, data):
        return True

    @staticmethod
    def register(response, addr=None):
        Mocket.register(Droid(addr or ('localhost', 80), [response]))
