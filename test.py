import requests
import unittest

from server import Server


class ServerTestCase(unittest.TestCase):
    def setUp(self):
        self.server = Server(8000)
        self.server.loop()

    def testRequest(self):
        for i in range(10):
            with self.subTest(i=i):
                r = requests.post("http://localhost:8000/path", headers={"User-Agent": "Unit Test"})
                self.assertEqual(r.status_code, 200)
                text = r.text
                self.assertTrue("path" in text)
                self.assertTrue("Unit Test" in text)

if __name__ == '__main__':
    unittest.main()