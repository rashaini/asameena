from bs4 import BeautifulSoup, SoupStrainer
import urllib
from urlparse import urljoin
import urlparse
from gensim import corpora
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

mydict = {}
map_url_text = {}
keys = []
inverted = {}

# store homepage url:text dict 'mydict'
url = 'https://www.macmillan.org.uk'
response = urllib.urlopen(url).read()
soup1 = BeautifulSoup(response, "lxml")
text = soup1.get_text()
mydict[url] = text

# extract links from homepage text and store them in list with unique elements 'links'
soup2 = BeautifulSoup(response, parse_only=SoupStrainer('a', href=True))
links = soup2.find_all('a')
links = [s.get('href') for s in links]
links = [unicode(s) for s in links]
links = [s for s in links if (s.startswith("https://") or s.startswith("http://"))]
# links = set(links)

# fetch text for each url in 'links' and store them in dict 'map_url_text'
for l in links:
    r = urllib.urlopen(l).read()
    soup = BeautifulSoup(r, "lxml")
    for s in soup(["script", "style"]):
        s.extract()
    t = soup.get_text()
    lines = (line.strip() for line in t.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    t = ' '.join(chunk for chunk in chunks if chunk)
    map_url_text[l] = t

# tokenize text in 'map_url_text' and add unique tokens to list 'keys'
for key, value in map_url_text.iteritems():
    value = set(value.split())
    for word in value:
        keys.append(word)

# build inverted index
for k in keys:
    for key, value in map_url_text.iteritems():
        if k in value:
            if any(k is term for term, urls in inverted.iteritems()):
                if key not in inverted[k]:
                    inverted[k].append(key) 
            else:
                inverted[k] = [key]

print inverted

# pagerank data preprocessing
urls = []
dico = {}
total_urls = []

# extract links from each url page in list of total links
for i, v in enumerate(links):
    open_page = urllib.urlopen(v).read()
    soup_bis_1 = BeautifulSoup(open_page, "lxml")
    urls = soup_bis_1.find_all('a')
    urls = [s.get('href') for s in urls]
    urls = [unicode(s) for s in urls]
    urls = [s for s in urls if (s.startswith("https://") or s.startswith("http://"))]
    urls = set(urls)
    dico[v] = urls

# append elements to reference list for matrix
for key, value in dico.iteritems():
    total_urls.append(key)
#     for i, v in enumerate(value):
#         total_urls.append(v)

# matrix

total_urls.append(url)
size = len(total_urls)

# matrix = [[0 for x in range(size)] for y in range(size)]

print len(matrix)

if (url is v3 for i3, v3 in enumerate(total_urls)) and (v4 in value for index, value in enumerate(links) for i4, v4 in enumerate(total_urls)):
    matrix[i3][i4] = 1

# if (v4 in value for index, value in enumerate(links) for i4, v4 in enumerate(total_urls)):
#     print i4
# if (v2 in value for index, value in enumerate(links) for i2, v2 in enumerate(total_urls)):
#     print i2
        
#     print i3
# if ((v in key for key, value in dico.iteritems()) for i, v in enumerate(total_urls)) and ((v in value for key, value in dico.iteritems()) for ind, val in enumerate(total_urls)):
#     matrix[i][ind] = 1
    
# if (url is v3 for i3, v3 in enumerate(total_urls)):
#     print i3

# for ind, valval in enumerate(total_urls):
#     if (valval in value for index, value in enumerate(links)):
#         print ind
#     matrix[i3][i4] = 1
    
# if (v1 in v for i, v in enumerate(value) for value in value for key, value in dico.iteritems() for i1, v1 in enumerate(total_urls)) and (v2 in value for index, value in enumerate(links) for i2, v2 in enumerate(total_urls)):
#     matrix[i1][i2] = 1