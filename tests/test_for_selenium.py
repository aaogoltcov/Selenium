import unittest
from selenium import webdriver


class YaTestCase(unittest.TestCase):

    def setUp(self):
        self.chrome_path = r'../venv/bin/chromedriver'
        self.driver = webdriver.Chrome(executable_path=self.chrome_path)
        self.addCleanup(self.driver.quit)

    def testPageTitle(self):
        self.driver.get('https://passport.yandex.ru/auth/')
        self.assertIn('Авторизация', self.driver.title)


if __name__ == '__main__':
    unittest.main()
