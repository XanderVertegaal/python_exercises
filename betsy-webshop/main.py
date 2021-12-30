__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

import models
from peewee import fn


def search(term: str):
    query = models.Product.select()
    return [
        x for x in query
        if (term.lower() in x.name.lower() 
        or term.lower() in x.description.lower())
    ]


def list_user_products(user_id: int):
    query = (models.Product
                .select()
                .join(models.UserProduct)
                .join(models.User)
                .where(models.User.id == user_id)
    )
    return query


def list_products_per_tag(tag_id: int):
    query = (models.Product
                .select()
                .join(models.ProductTag)
                .join(models.Tag)
                .where(models.Tag.id == tag_id)
    )
    return query


# The argument 'product' is interpreted as 'product name' here. A default quantity of 1 is assumed.
def add_product_to_catalog(user_id: int, product: str):
    added_product = models.Product.get(models.Product.name == product)
    models.UserProduct.create(
        user_id=user_id,
        product_id=added_product.id,
        quantity=1
    )


"""
It is not clear to me what the function update_stock() should accomplish. The webshop itself does not have a stock of products, so there is nothing to update.

Instead, the users maintain their own products, so it would make more sense to update a user's individual stock. In the scaffolding provided by Wincpy, however, there is no parameter for the user given. To make this function more useful, I would change it to:

def update_stock(product_id: int, user_id: int, new_quantity: int):
    query = (models.UserProduct
                .update({UserProduct.quantity: new_quantity})
                .where(UserProduct.user == user_id && UserProduct.product == product_id))
    q.execute()
"""
def update_stock(product_id: int, new_quantity: int):
    query = (models.Product
                .update({models.Product.quantity: new_quantity})
                .where(models.Product.id == product_id))
    query.execute()

# The product is removed for all users.
def remove_product(product_id: int):
    product = models.Product.get(models.Product.id == product_id)
    product.delete_instance()


"""
The scaffolding provided by Wincpy does not include a seller_id. I have added it, since it is required by the exercise.

Due to the field constraitns, Peewee will shout at us when a negative product quantity is set. This is why the queries are executed at the last possible moment.
"""
def purchase_product(product_id: int, buyer_id: int, seller_id: int, quantity: int):
    buyer_update = (models.UserProduct
                        .update({models.UserProduct.quantity: models.UserProduct.quantity + quantity})
                        .where((models.UserProduct.user == buyer_id) & (models.UserProduct.product == product_id)))

    seller_update = (models.UserProduct
                        .update({models.UserProduct.quantity: models.UserProduct.quantity - quantity})
                        .where((models.UserProduct.user == seller_id) & (models.UserProduct.product == product_id)))

    models.Transaction.create(
        buyer=buyer_id,
        seller=seller_id,
        product=product_id,
        quantity=quantity
    )

    buyer_update.execute()
    seller_update.execute()
