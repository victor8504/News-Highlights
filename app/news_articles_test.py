import unittest
from .models import news_articles
NewsArticles = news_articles.NewsArticles

class NewsArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the NewsArticles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new_article = NewsArticles("tmz","TMZ News", "Barbara Cohan","Social Media","Celebrity news",
                                     "http://www.tmz.com","https://immage.tmdb.org/t/p/w500/khsjha27hbs", "2017-04-30T12:00:00Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, NewsArticles))

if __name__ == '__main__':
    unittest.main()