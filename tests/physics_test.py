import unittest

from repulsiveruby import physics
from repulsiveruby import sprites


class TestPhysics(unittest.TestCase):
    def testTwoBallDistance(self):
        sprites.ball1.position = (0, 0)
        sprites.ball2.position = (3, 4)
        result = physics.twoBallDistance(sprites.ball1, sprites.ball2)
        self.assertAlmostEqual(5, result)
