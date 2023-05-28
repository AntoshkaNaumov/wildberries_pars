# 'id', 'название', 'цена', 'бренд', 'продаж', 'рейтинг', 'в наличии'


import requests
import csv
from models import Items


class ParsWB:
    def __init__(self, url):
        self.url = url


    def parse(self):

        self.__create_csv()
        while True:
            response = requests.get(
                self.url,
            )
            if response.status_code != 200:
                break
            items_info = Items.parse_obj(response.json()["data"])
            if not items_info.products:
                break
            self.__save_csv(items_info)


    def __create_csv(self):
        with open("wb_data.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'название', 'цена', 'бренд', 'продаж', 'рейтинг', 'в наличии'])


    def __save_csv(self, items):
        with open("wb_data.csv", mode="a", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            for product in items.products:
                writer.writerow([product.id,
                                 product.name,
                                 product.salePriceU,
                                 product.brand,
                                 product.sale,
                                 product.rating,
                                 product.volume])


if __name__ == '__main__':
    ParsWB("https://catalog.wb.ru/brands/t/catalog?appType=1&brand=6669&curr=rub&dest=-1257786&regions=80,115,38,4,64,83,33,68,70,69,30,86,75,40,1,66,110,22,31,48,71,114&sort=popular&spp=0").parse()
