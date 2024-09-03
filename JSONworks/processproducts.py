from json import load

f=open("C:\\Users\\Rintu Sam\\Desktop\\PythonJuneWorks\\JSONworks\\products.json","r",encoding="UTF-8")

products=load(f)

# print(len(products))

products_title=[p.get("title")for p in products]
# print(products_title)


jewellery_title=[i.get("title")for i in products if i.get("category")=="jewelery"]
# print(jewellery_title)

product_price=[j.get("title")for j in products if j.get("price")>100]
# print(product_price)

product_range=[j.get("title")for j in products if j.get("price")>=100 and j.get("price")<=150]
# print(product_range)

def get_rating_count(dic):
    return dic.get("rating").get("count")

top_selling_product=max(products,key=get_rating_count)
print(top_selling_product)



