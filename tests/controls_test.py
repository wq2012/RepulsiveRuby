import unittest

from repulsiveruby import controls
from repulsiveruby import sprites


class TestDetectKey(unittest.TestCase):
    def testNoKey(self):
        result = controls.detectKey(sprites.ball_main)
        self.assertEqual("", result)
