from unittest import TestCase

from mocket.mocket import Mocket, MocketEntry, mocketize

from neo import Neo


# Note: `morpheus.py` server must be running
class RealTestCase(TestCase):

    def test_ok(self):
        neo = Neo()
        self.assertTrue(neo.iknow())
        self.assertEqual(len(Mocket._requests), 0)


class MockTestCase(TestCase):

    addr = ('localhost', 8080)

    @mocketize
    def test_ok(self):
        Mocket.register(MocketEntry(self.addr, ['Show me.\r\n']))
        neo = Neo(addr=self.addr)
        self.assertTrue(neo.iknow())
        self.assertEqual(len(Mocket._requests), 1)

    @mocketize
    def test_ko(self):
        Mocket.register(MocketEntry(self.addr, ['Blue Pill.\r\n']))
        neo = Neo(addr=self.addr)
        self.assertFalse(neo.iknow())
        self.assertEqual(len(Mocket._requests), 1)
