from bs4 import BeautifulSoup as BS
import requests
import pandas as PD

class ScrapeEngine:

    def __init__(self, search_term):
        self.search_term = search_term

    def scrape_jumia(self):
        search_term=self.search_term
        print(search_term)
        try:
            search_term = search_term.replace_all(' ', '+') #replace all spaces with plus (+)
        except AttributeError:
            search_term = self.search_term
        search_url = f"https://www.jumia.com.ng/catalog/?q={search_term}"
        search_page = requests.get(search_url)

        content = BS(search_page.content, 'html.parser')
        html = list(content.children)[1]

        item_list = [];

        product_info = html.find_all(class_="info")
        
        for item in product_info:
            item_name = item.find(class_='name').get_text()
            item_price = item.find(class_='prc').get_text()
            try:
                item_old_price = item.find(class_="old").get_text()
                item_discount = item.find(class_="_dsct").get_text()
            except AttributeError:
                item_old_price = 'no data'
                item_discount = 'no data'

            item_dict = {
                'product_name':item_name,
                'product_price':item_price,
                'product_old_price':item_old_price,
                'product_discount': item_discount,
            }
            
            item_list.append(item_dict)
        
        return item_list