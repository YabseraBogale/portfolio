from requests import get
from bs4 import BeautifulSoup as bs
from pprint import pprint

def title(url):
    data=get(url).content
    title=bs(data,"html.parser").title.text
    return {title: url}


if __name__=="__main__":
    test="https://www.bbc.com/news/in-pictures-65346964"
    test=title(test)
    pprint(test)
    test="https://securecode.wiki/docs/lang/python/"
    test=title(test)
    pprint(test)