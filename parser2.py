import csv
from datetime import datetime
from bs4 import BeautifulSoup
import requests

# main class
class Parser():
    def __init__(self):
        pass

# response
    def get_html(self, url):
        r = requests.get(url)
        return r.text


# all href of site
    def get_all_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all('ul',class_='pagn')
        print(data)

        links = []


        print(links)

# geting all titles and their prices
    def get_page_data(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        try:
            name = soup.find_all('a', class_='name')
        except:
            name = ''
        try:
            price = soup.find_all('div', class_='price')
        except:
            price = ''

        data = {'name': name,
                'price': price,}
        for key,value in data.items():
            for x in value:
                print(x.get_text())

                # csv for the data
                with open('lalafo.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow((data['name'],
                                     data['price']))

    def style(self):
        s = get_page_data(html)
        return ' \n'.join(s)


        


# main function
    def main(self):
        for i in range(1, 250):
            link = '/kyrgyzstan/mobilnye-telefony-i-aksessuary?page=%s' % i
            base_url = 'https://lalafo.kg' + link
            all_links_data = self.get_page_data(self.get_html(base_url))

parser = Parser()
parser.main()
