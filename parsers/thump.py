from baseparser import BaseParser
from BeautifulSoup import BeautifulSoup, Tag


class ThumpParser(BaseParser):
    SUFFIX = ''
    domains = ['thump.vice.com']

    feeder_pat   = '^http://thump.vice.com/.*_.*/article/'
    feeder_pages = ['http://thump.vice.com/']

    def _parse(self, html):
        soup = BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES,
                             fromEncoding='utf-8')

        self.meta = soup.findAll('meta')
        elt = soup.find('h1')
        if elt is None:
            self.real_article = False
            return
        self.title = elt.getText()
        self.byline = soup.find('span', 'byline').getText()
        self.date = soup.find('span', 'date').getText()

        div = soup.find('div', 'rich-text')
        self.body = '\n'+'\n\n'.join([x.getText() + ' ' for x in div.childGenerator()
                                      if isinstance(x, Tag) ])
