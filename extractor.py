from bs4 import BeautifulSoup
import re
import urllib.request

class AppURLOpener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLOpener()
response = opener.open('http://www.hindustantimes.com/cricket/wasim-akram-waqar-younis-twitter-spat-on-anil-kumble-10-74-feat-gets-ugly/story-YNanlf75F8HfubbuIvPVTN.html')
soup = BeautifulSoup(response, 'html.parser')



texts = soup.get_text()
print(texts)

def visible(element):
    if element.parent.name in ['style', 'sccript', '[document', 'head', 'title' ]:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False#
    return True


visible_texts = filter(visible, texts)

print(visible_texts)