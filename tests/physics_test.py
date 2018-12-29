import sys
import unittest

sys.path.append("./repulsiveruby")
import physics  # noqa: E402


class Namespace(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class TestPhysics(unittest.TestCase):
    def testNorm(self):
        vec = (0, 1)
        self.assertAlmostEqual(1, physics.norm(vec))
        vec = (3, 4)
        self.assertAlmostEqual(5, physics.norm(vec))
        vec = (1, 1)
        self.assertAlmostEqual(1.414, physics.norm(vec), places=3)

    def testTwoBallDistance(self):
        ball1 = Namespace()
        ball2 = Namespace()
        ball1.position = (0, 0)
        ball2.position = (3, 4)
        ball1.radius = 32
        ball2.radius = 32
        result = physics.twoBallDistance(ball1, ball2)
        self.assertAlmostEqual(5, result)


if __name__ == "__main__":
    unittest.main()
