#!/user/bin/env.python
# -*- coding:utf-8 -*-
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("do something before test.Prepare environment.")

    def tearDown(self):
        print("do something after test.Clean up.")

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
