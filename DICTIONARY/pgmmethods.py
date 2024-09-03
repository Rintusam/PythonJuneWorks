# create a dictionary mobile with key name,brand,price,is_available

mobile={"name":"note10pro","brand":"redmi","price":20000,"is_available":True,"offer":1000}


#cls dict : get(key) => get value
# print mobile name
# print(mobile.get("name"))
# # print mobile price
# print(mobile.get("price"))

# all_keys=mobile.keys()
# print(all_keys)

# all_values=mobile.values()
# print(all_values)

# all_item=mobile.items()
# print(all_item)

# for k,v in mobile.items():
#     print(k,v)

# mobile.pop("name")
# print(mobile)

# mobile["offer"]=500
# print(mobile)

# print("name" in mobile)         #true    #false


#selling price

if "offer" in mobile:

    selling_price=mobile.get("price")-mobile.get("offer")

    print(selling_price)

else:
    print(mobile.get("price"))
    


