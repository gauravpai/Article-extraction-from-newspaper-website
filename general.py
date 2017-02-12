import os

# creating a project


def create_proj_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project'+directory)
        os.makedirs(directory)


# create queue and crawled files
def create_data_file(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    articles = project_name + '/articles.txt'
    if not os.path.exists(queue):
        write_file(queue,base_url)
    if not os.path.exists(crawled):
        write_file(crawled,'')
    if not os.path.exists(articles):
        write_file(articles,'')




# creating a new file


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# add data onto an exisitng file


def add_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# Delete all file contents


def delete_contents(path):
    with open(path, 'w'):   # create new file to overwrite the old one
        pass              # do nothing


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# Iterate through set, each line item will be a new line in the file


def set_to_file(links, file):
    delete_contents(file)
    for link in sorted(links):
        add_to_file(file, link)
