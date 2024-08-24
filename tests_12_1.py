from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        jonnie_walker = Runner('jonnie')
        for i in range(10):
            jonnie_walker.walk()
        self.assertEqual(jonnie_walker.distance, 50)
    def test_run(self):
        jonnie_runner = Runner('jonnie')
        for i in range(10):
            jonnie_runner.run()
        self.assertEqual(jonnie_runner.distance, 100)
    def test_challenge(self):
        jonnie_walker = Runner('jonnie')
        jonnie_runner = Runner('jonnie')
        for i in range(10):
            jonnie_walker.walk()
            jonnie_runner.run()
        self.assertNotEqual(jonnie_walker.distance, jonnie_runner.distance)
if __name__ == '__main__':
    unittest.main()