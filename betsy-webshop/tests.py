from models import *
from main import *

db.connect()

db.create_tables([
User,
Product,
Tag,
ProductTag,
UserProduct,
Transaction
])

jim = User.create(
    name='Jim',
    address="Vlamenburg 11",
    credit_card_number=6
)

james = User.create(
    name='James',
    address='Groenling 43',
    credit_card_number=7
)


ball = Product.create(
    name='ball',
    description='round object, unlike sweaters',
    price_per_unit=1,
    quantity=10
)

train = Product.create(
    name='train',
    description='driving thing',
    price_per_unit=2,
    quantity=5
)

sweater = Product.create(
    name='sWeAtEr',
    description='warm thing',
    price_per_unit=3.336,
    quantity=1
)

sweater2 = Product.create(
    name="coolSweater",
    description='warmer thing',
    price_per_unit=4,
    quantity=2
)

jimTrain3 = UserProduct.create(
    user_id=1,
    product_id=2,
    quantity=3
)

jimBall5 = UserProduct.create(
    user_id=1,
    product_id=1,
    quantity=5
)

jamesSweater7 = UserProduct.create(
    user_id=2,
    product_id=3,
    quantity=7
)

jamesTrain1 = UserProduct.create(
    user_id=2,
    product_id=2,
    quantity=1
)

tag1 = Tag.create(
    tag='cool'
)

tag2 = Tag.create(
    tag='warm'
)

tag3 = Tag.create(
    tag='nice'
)

trainCool = ProductTag.create(
    product_id=2,
    tag_id=1
)

trainNice = ProductTag.create(
    product_id=2,
    tag_id=3
)

sweaterWarm = ProductTag.create(
    product_id=3,
    tag_id=2
)

sweaterNice = ProductTag.create(
    product_id=3,
    tag_id=3
)

# TEST 1
# print('Searching for "SWEATER". This also finds "ball", since "sweater" is used in its description.')
# for x in search(term='SWEATER'):
#     print(x.name)

# TEST 2
# for x in list_user_products(user_id=1):
#     print(x.name)

# TEST 3
# for x in list_products_per_tag(tag_id=3):
#     print(x.name)

# TEST 4
# print('Before adding Jims sweater:')
# all_products = UserProduct.select()
# for p in all_products:
#     print(f'User ID: {p.user_id}, Item ID: {p.product_id}')
# add_product_to_catalog(user_id=1, product='coolSweater')
# print('\nAfter adding Jims sweater (user id 1; product 4):')
# all_products = UserProduct.select()
# for p in all_products:
#     print(f'User ID: {p.user_id}, Item ID: {p.product_id}')

# TEST 5
# print('Stock of trains before updating stock quantity:')
# train = Product.get(Product.name == 'train')
# print(train.quantity)
# update_stock(2, 10)
# print('\nAfter updating stock:')
# train = Product.get(Product.name == 'train')
# print(train.quantity)


# TEST 6
# print('List of products before deleting one:')
# all_products = Product.select()
# for p in all_products:
#     print(p.name)
# remove_product(2)
# print('\nAfter removing the train:')
# all_products = Product.select()
# for p in all_products:
#     print(p.name)

# TEST 7
# print('List of items possessed by Jim')
# jim_items = (UserProduct
#                 .select()
#                 .where(UserProduct.user == 1))
# for i in jim_items:
#     print(f"Item id: {i.product}, item quantity: {i.quantity}")
# print('\nList of items possessed by James:')
# james_items = (UserProduct
#                 .select()
#                 .where(UserProduct.user == 2))
# for i in james_items:
#     print(f"Item id: {i.product}, item quantity: {i.quantity}")
# print('\nNow James buys 2 trains (id = 2) from Jim\n')
# purchase_product(product_id=2, buyer_id=2, seller_id=1, quantity=2)
# print('List of items possessed by Jim')
# jim_items = (UserProduct
#                 .select()
#                 .where(UserProduct.user == 1))
# for i in jim_items:
#     print(f"Item id: {i.product}, item quantity: {i.quantity}")
# print('\nList of items possessed by James:')
# james_items = (UserProduct
#                 .select()
#                 .where(UserProduct.user == 2))
# for i in james_items:
#     print(f"Item id: {i.product}, item quantity: {i.quantity}")
# transaction = (Transaction.get(
#     (Transaction.buyer == 2) & 
#     (Transaction.seller == 1) &
#     (Transaction.product == 2)
# ))
# print(f"\nNew transaction quantity: {transaction.quantity}")

# TEST 8:
# print('Check rounding on the sweater price')
# my_sweater = Product.get(Product.name == 'sWeAtEr')
# print(my_sweater.price_per_unit)


db.close()