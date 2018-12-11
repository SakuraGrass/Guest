import requests
import unittest


class GetEventListTest(unittest.TestCase):
    """查询发布会接口测试"""

    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"

    def test_set_event_null(self):
        """发布会id为空"""
        r = requests.get(self.url, params={'eid': ''})
        results = r.json()
        self.assertEqual(results['status'], '10021')
        self.assertEqual(results['message'], "parameter error")


if __name__ == '__main__':
    unittest.main()
