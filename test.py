from unittest import TestCase
from mocket.mocket import Mocket, Mocketizer, MocketEntry
from neo import Neo


class RealTestCase(TestCase):
    def test_ok(self):
        neo = Neo()
        self.assertTrue(neo.iknow())
        self.assertEqual(len(Mocket._requests), 0)


class DroidTestCase(TestCase):
    @Mocketizer.wrap
    def test_ok(self):
        Mocket.register(MocketEntry(('localhost', 8080), ['Show me.\r\n']))
        neo = Neo()
        self.assertTrue(neo.iknow())
        self.assertEqual(len(Mocket._requests), 1)

    @Mocketizer.wrap
    def test_ko(self):
        Mocket.register(MocketEntry(('localhost', 8080), ['Blue Pill.\r\n']))
        neo = Neo()
        self.assertFalse(neo.iknow())
        self.assertEqual(len(Mocket._requests), 1)