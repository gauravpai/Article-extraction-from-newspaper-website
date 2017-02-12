import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *
import time


PROJECT_NAME = 'hindu'
HOMEPAGE = 'http://www.thehindu.com'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
ARTICLE_FILE = PROJECT_NAME + '/articles.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create worker threads (will die when main thread exists)
def create_workers():
    for _ in  range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        # time.sleep(30)
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()





# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()
    time.sleep(5)

# Check items in queue , if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' Links in the queue')
        create_jobs()
        time.sleep(1)


create_workers()
crawl()
