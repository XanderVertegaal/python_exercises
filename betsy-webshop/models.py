from peewee import *

db = SqliteDatabase(":memory:")


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    address = CharField()
    credit_card_number = CharField()


"""
I have no idea why Product should have a quantity property.
Users maintain their own stocks; Betsy itself does not sell anything.
"""


class Product(BaseModel):
    name = CharField(index=True)
    description = CharField(max_length=300)
    price_per_unit = DecimalField(auto_round=True, decimal_places=2)
    quantity = IntegerField(constraints=[Check("quantity >= 0")])


class Tag(BaseModel):
    tag: CharField(unique=True)


class ProductTag(BaseModel):
    product = ForeignKeyField(Product)
    tag = ForeignKeyField(Tag)


class UserProduct(BaseModel):
    user = ForeignKeyField(User)
    product = ForeignKeyField(Product)
    quantity = IntegerField(constraints=[Check("quantity >= 0")])


class Transaction(BaseModel):
    buyer = ForeignKeyField(User)
    seller = ForeignKeyField(User)
    product = ForeignKeyField(Product)
    quantity = IntegerField(constraints=[Check("quantity >= 0")])
