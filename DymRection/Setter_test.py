from scrapy.item import Field,Item
class Base(Item):
    pass

if __name__ == '__main__':
    setattr(Base,'name',Field)
    print(Base)
