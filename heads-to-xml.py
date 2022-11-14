from bs4 import BeautifulSoup
import requests
import xmltodict
import urllib3
import json
import re

my_sitemap = 'https://staging.calyaconsult.ch/articles/sitemap.xml'
article_base = 'http://staging.calyaconsult.ch/articles/'
pages_base = 'https://staging.calyaconsult.ch/ccch/'
horoscopes_base = 'http://localhost/horoscope/pages/'

def get_xml(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    try:
        data = xmltodict.parse(response.data)
    except:
        print("Failed to parse xml from response (%s)" % traceback.format_exc())
    return data

def get_page(url):
    page = requests.get(url)
    return page.content

def scan_articles():
  articles = [
    'blogpost-20200819-1.html',
    'blogpost-20200822-1.html',
    'blogpost-20200828-1.html',
    'blogpost-20200830-1.html',
    'blogpost-20200900-1.html',
    'blogpost-20200902-1.html',
    'blogpost-20200911-1.html',
    'blogpost-20201009-1.html',
    'blogpost-20201027-1.html',
    'blogpost-20220519-1.html',
    'blogpost-20220525-1.html',
    'blogpost-20220707-1.html',
    'blogpost-20220712-1.html',
    'blogpost-20220903-1.html'
  ]

  for article in articles:
    article_url = article_base+article
    # Uncomment for reading contents of <main> tag
    #article_filename_template = './%s_frag.html'
    #outfile = article_filename_template % (article[0:19])
    #fh = open(outfile,"w")
    html = get_page(article_url)
    soup = BeautifulSoup(html, "html.parser")
    #print("\n"+article, outfile)
    #fh.write(soup.find("main").get_text())
    #fh.close()
    print("\n"+article)
    print(soup.find("head"))

def scan_pages():
  pages = [
	  "index.html",
	  "index-september-A.html",
	  "index-september.html"
  ]
  with open('pages.xml', 'w') as f:
    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"./pages.xsl\"?>\n<pageset>\n")
    for page in pages:
      page_url = pages_base+page
      html = get_page(page_url)
      soup = BeautifulSoup(html, "html.parser")
      f.write("\n<page name=\""+page+"\">")
      f.write(str(soup.find("head")))
      f.write("</page>")
    f.write("</pageset>")
  f.close()
def scan_horoscopes():
    for j in range(2002,2014):
      page = "JH-GEN-%d.html" % j
      page_url = horoscopes_base+page
      html = get_page(page_url)
      soup = BeautifulSoup(html, "html.parser")
      print("\n"+page)
      print(soup.find("head"))

def scan_scripts():
    for j in range(2002,2014):
      page = "JH-GEN-%d.html" % j
      page_url = horoscopes_base+page
      html = get_page(page_url)
      soup = BeautifulSoup(html, "html.parser")
      print("\n"+page)
      for s in soup.findAll("script"):
        print(s)

def scan_sitemap(url):
  urlset = get_xml(url)
  for x in urlset['urlset']['url']:
    if re.match("202[0-9]",x['lastmod']):
      article_url = x['loc']
      html = get_page(article_url)
      soup = BeautifulSoup(html, "html.parser")
      print(article_url)
      print(soup.find("head"))

scan_pages()
#scan_articles()
#scan_horoscopes()
#scan_scripts()
#scan_sitemap(my_sitemap)
