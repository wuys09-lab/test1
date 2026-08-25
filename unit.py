import unittest


class TestDemo(unittest.TestCase):
    """测试类必须继承 unittest.TestCase"""

    @classmethod
    def setUpClass(cls):
        print("\n整个类只执行一次的前置（如启动浏览器）")

    def setUp(self):
        print("每个测试方法前都执行（如打开页面）")

    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_str(self):
        self.assertIn("百度", "百度一下，你就知道")

    def tearDown(self):
        print("每个测试方法后都执行（如关闭页面）")

    @classmethod
    def tearDownClass(cls):
        print("整个类只执行一次的后置（如关闭浏览器）")


if __name__ == '__main__':
    unittest.main()