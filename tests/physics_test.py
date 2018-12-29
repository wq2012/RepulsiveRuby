import sys
import unittest

sys.path.append("./repulsiveruby")
import physics  # noqa: E402


class TestPhysics(unittest.TestCase):
    def testNorm(self):
        vec = (0, 1)
        self.assertEqual(1, physics.norm(vec))

    # def testTwoBallDistance(self):
    #     sprites.ball1.position = (0, 0)
    #     sprites.ball2.position = (3, 4)
    #     result = physics.twoBallDistance(sprites.ball1, sprites.ball2)
    #     self.assertAlmostEqual(5, result)


if __name__ == "__main__":
    unittest.main()
