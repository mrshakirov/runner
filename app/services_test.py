import unittest
import services


class ReportTest(unittest.TestCase):
    def test_add(self):
        services.Report.add({'Word': 6})
        self.assertEqual(services.Report.words(), {'word': 6})

    def test_pre_process(self):
        result = services.Report.pre_process('Word?!')
        self.assertEqual('word', result)


if __name__ == '__main__':
    unittest.main()
