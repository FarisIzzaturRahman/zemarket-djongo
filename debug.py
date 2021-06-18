from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
zemarket_db = client['zemarket_db']
products = zemarket_db['store_product']


data_products = products.find_one({"slug" : 'saffron-antibacterial-face-oil'})
print(data_products)    



# images = products.find({},{"_id": 0,'image':1})

# for x in data_products :
#     # print(type(images))
#     print(x['image'])
