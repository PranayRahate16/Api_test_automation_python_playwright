import pytest

from api_clients.Create_Cart_api import CreateCartAPI

@pytest.mark.api
class Test_CreateCartAPI:

    def test_create_cart(self,api_request_context, access_token):
        cart_api=CreateCartAPI(api_request_context)
        response=cart_api.create_cart(access_token=access_token)

        jsondata=response.json()
        print(response.status)
        print(jsondata.get('cartId'))

        assert response.status == 201, f'Cart Creation failed and got {response.status} and Body : {response.text()}'


    def test_add_item_to_cart(self,api_request_context, access_token,cart_id):
        cart_api = CreateCartAPI(api_request_context)
        product_id = 1710  # ← add this: define it as a local variable
        quantity = 1  # ← add this too

        response=cart_api.add_item_to_cart(cart_id=cart_id,
                                  access_token=access_token,
                                  product_id=product_id,
                                  quantity=quantity
                                  )
        jsondata=response.json()

        assert response.status == 201, f'Product id {product_id} not available. Body: {response.text()}'
        #
        print(f'product {product_id} added to cart {cart_id} and quantity is {quantity}')
        print(jsondata)