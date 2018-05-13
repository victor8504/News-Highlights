import unittest
from .models import news_source
NewsSource = news_source.NewsSource

class NewsSourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the NewsSource class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new_source = NewsSource("tmz","TMZ News","Your trusted source for celebrity entertainment news",
                                     "http://www.tmz.com","Breaking News","country")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, NewsSource))

if __name__ == '__main__':
    unittest.main()