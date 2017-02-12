''' Extracts articles from hindu '''

import newspaper

HOMEPAGE = 'http://www.thehindu.com'
ARTICLE = 'http://www.thehindu.com/news/national/MHA-website-hacked-Officials-say-it-is-%E2%80%98down-for-repair%E2%80%99/article17292021.ece?homepage=true'

class Extractor:
    ''' extracts details about newspaper '''
    def __init__(self):
        self.paper = newspaper.build(HOMEPAGE, memoize_articles=False)

    def print_article_urls(self):
        ''' prints article urls '''
        for article in self.paper.articles:
            print(article.url)

    def print_latest_article(self):
        ''' prints the latest article '''
        if len(self.paper.articles) == 0:
            print("No articles found")
            return
        art = self.paper.articles[0]
        art.download()
        art.parse()
        print("Written by: " + ", ".join(art.authors))
        print(art.text.encode())

class ArticleExtractor:
    ''' meant to extract articles '''
    def __init__(self):
        self.article = newspaper.Article(url=ARTICLE)
        self.article.download()
        self.article.parse()

    def print_article(self):
        ''' prints extracted article '''
        print("Written by: " + ", ".join(self.article.authors))
        print(self.article.text.encode())

if __name__ == '__main__':
    ex = Extractor()
    ex.print_article_urls()
    ex.print_latest_article()

    art = ArticleExtractor()
    art.print_article()

