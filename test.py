from unittest import TestCase
from droid import Droid
from mocket.registry import mocketize
from stormtrooper import Stormtrooper


class JedyTestCase(TestCase):
    def test_ok(self):
        stormtrooper = Stormtrooper()
        self.assertTrue(stormtrooper.identify())


class DroidTestCase(TestCase):
    @mocketize
    def test_ok(self):
        Droid.register('You don\'t need to see his identification.\r\n')
        stormtrooper = Stormtrooper()
        self.assertTrue(stormtrooper.identify())
