class NewsArticles:
    '''
    NewsArticles class to define NewsArticles objects
    '''

    def __init__(self, id, name, author, title, description, url, imageUrl, publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = imageUrl
        self.publishedAt = publishedAt