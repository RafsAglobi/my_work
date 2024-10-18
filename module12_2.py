import unittest
import runner


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = runner.Runner('Усэйн', 10)
        self.r2 = runner.Runner('Андрей', 9)
        self.r3 = runner.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'{key}: {value.name}')

    def test1(self):
        t1 = runner.Tournament(90, self.r1, self.r3)
        result = t1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results = result
        print(self.all_results)

    def test2(self):
        t1 = runner.Tournament(90, self.r2, self.r3)
        result = t1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results = result
        print(self.all_results)

    def test3(self):
        t1 = runner.Tournament(90, self.r1, self.r2, self.r3)
        result = t1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results = result
        print(self.all_results)


if __name__ == '__main__':
    unittest.main()