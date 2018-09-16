import unittest
import services


def clear(f):
    def wrapper(*args, **kwargs):
        services.Report.clear()
        return f(*args, **kwargs)
    return wrapper


class ReportTestCase(unittest.TestCase):
    @clear
    def test_add(self):
        services.Report.add({'Word': 6})
        self.assertEqual(services.Report.words(), {'word': 6})

    @clear
    def test_pre_process(self):
        result = services.Report.pre_process('Word?!')
        self.assertEqual('word', result)


class TXTReaderTestCase(unittest.TestCase):
    @clear
    def test_read(self):
        services.TXTReader.read('test.txt')
        self.assertEqual(services.Report.words(), {
            'one': 1,
            'two': 1,
            'three': 1})


class ZIPReaderTestCase(unittest.TestCase):
    @clear
    def test_read(self):
        pass


if __name__ == '__main__':
    unittest.main()
