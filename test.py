import unittest
from python_sql import *


class TestUM(unittest.TestCase):
    def setUp(self):
        name = 'hhmm.db'
        self.con = sqlite3.connect(name)
        self.cursor = self.con.cursor()
        init_db(self.cursor)
        self.con.commit()

    def tearDown(self):
        self.con.commit()
        self.con.close()

    def test_request1(self):
        task1(self.cursor)
        self.cursor.execute('SELECT registration_date FROM users;')
        mas = self.cursor.fetchall()
        for a in mas:
            self.assertTrue(a[0][4] == "-" and a[0][7] == "-")

    def test_request2(self):
        task1(self.cursor)
        self.assertEqual(task2(self.cursor), "bbb")

    def test_request3(self):
        task11(self.cursor)      
        m = {2008,2006,2000} 
        self.assertEqual(task3(self.cursor), m)

    def test_request4(self):
        self.assertEqual(task4(self.cursor),161)

    def test_request5(self):
        task1(self.cursor)
        task11(self.cursor)
        self.assertEqual(task5(self.cursor),15)
    

    


if __name__ == "__main__":
    unittest.main(failfast=True)
