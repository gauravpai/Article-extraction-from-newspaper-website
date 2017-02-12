from newspaper import Article

g = open('hindu/article.txt', 'w')


def print_article(url):
    b = Article(url)
    b.download()
    b.parse()
    print(b.title + '\n' + b.text)

f = open('hindu/articles.txt', 'rt')

for line in f:
    print_article(line)
    print(line)




f.close()
g.close()







