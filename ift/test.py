import unittest

import ift

class ImportTest(unittest.TestCase):
    def setUp(self):
        ift.configure()

    def test_import_from_twitter(self):
        m = ift.import_from_twitter('713091939805966337')

        output = m.left_pad('helloworld', 15)

        self.assertEqual(output, '     helloworld')
