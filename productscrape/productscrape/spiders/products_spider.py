import scrapy
import requests
import re
import random


class ProductsSpider(scrapy.Spider):
    name = "products"

    start_urls = [
        'https://thinkpro.vn/phu-kien',
        # 'https://thinkpro.vn/Lenovo',
        # 'https://thinkpro.vn/Razer',
        # 'https://thinkpro.vn/HP',
        # 'https://thinkpro.vn/Microsoft',
        # 'https://thinkpro.vn/MSI',
        # 'https://thinkpro.vn/Acer',
        # 'https://thinkpro.vn/LG',
        # 'https://thinkpro.vn/Asus'
    ]

    def parse(self, response):
        # brand = response.url.split('/')[-1]
        # filename = 'products-%s.html' % brand
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        sku = 1
        for product in response.css('div.item-grid'):
            if product.css('div.content-bottom div.product-price').get() is None:
                continue
            name = ' '.join(product.css(
                'div.content-bottom a::text').get().split('\n')[1].split())
            image_url = product.css(
                '.image-container img').xpath('@data-src').get()
            img_data = requests.get(image_url).content
            with open('../accessories/' + image_url.split('/')[-1], 'wb') as handler:
                handler.write(img_data)
            price = round(float(''.join(re.search(r'\d+(\.\d+)*', product.css(
                'div.content-bottom div.product-price span::text')[1].get(), re.IGNORECASE).group().split('.'))) / 22935.5, 2)
            imagepath = image_url.split('/')[-1]
            imagepath = 'accessories/' + (imagepath[:-3] + '.jpg',
                                          imagepath)[imagepath[-4:] in ['.jpg', '.png']]
            yield {
                'sku': name,
                'name': name,
                'base_image': imagepath,
                'small_image': imagepath,
                'thumbnail_image': imagepath,
                'additional_images': imagepath,
                'store_view_code': '',
                'attribute_set_code': 'Default',
                'product_type': 'simple',
                'categories': 'Root,Root/Accessories',
                'product_websites': 'base',
                'description': name,
                'tax_class_name': 'Taxable Goods',
                'visibility': 'Catalog, Search',
                'price': price,
                'url_key': imagepath[:-3],
                'meta_title': name,
                'qty': random.randrange(20, 50, 3)
            }
