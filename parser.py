import re


path1 = 'hindu/articles.txt'
path = 'hindu/crawled.txt'
g = open(path, 'r')
h = open(path1, 'w')

for line in g:
    if re.match("(.*)article(.*)", line):
        if re.match("(.*)archive(.*)", line):
            continue
        if re.match("(.*)book(.*)", line):
            continue
        if re.match("(.*)video(.*)", line):
            continue
        h.write(line)

g.close()
h.close()

