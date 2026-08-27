import params

from config import config

class ProductAPI:

    ENDPOINT = '/products'

    def __init__(self, request_context):
        self.request_context=request_context

    def get_products(self):
        return self.request_context.get(self.ENDPOINT)

    def get_product_not_in_stock(self):
        return self.request_context.get(self.ENDPOINT)

    def get_product_by_id(self, product_id):
        return self.request_context.get(self.ENDPOINT+'/'+str(product_id))

    def get_product_by_name(self, name):
        return self.request_context.get(self.ENDPOINT,params={'name':name})


