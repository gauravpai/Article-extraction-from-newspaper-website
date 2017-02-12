from urllib.request import urlopen
from link_finder import LinkFinder
from general import *
import re



class Spider:
    # class vairables shared among all spiders(all instances of class spider)
    articles_file = ''
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()
    articles = set()
    expression = 'http://www.thehindu.com.*'
   # expression1 = 'http://www.thehindu.com/.article.'

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        Spider.articles_file = Spider.project_name + '/articles.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
        create_proj_dir(Spider.project_name)
        create_data_file(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
        Spider.articles = file_to_set(Spider.articles_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_link(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print('Error: cannot crawl page : Cannot Open')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            regex = re.compile(Spider.expression)
            if re.match(regex, url) is not None:
                Spider.queue.add(url)
           # regex1 = re.compile(Spider.expression1)
           # if re.match(regex1 ,url):
                Spider.articles.add(url)



    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
        set_to_file(Spider.articles, Spider.articles_file)

