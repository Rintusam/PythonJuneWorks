mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    {"id":101,"title":"s23 ","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redmi 10 pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"iphone 14","brand":"mi","price":12000,"network":"4g"}
    
]

#print all obile names

all_mobiles= [mob.get("title") for mob in mobiles ]
print(all_mobiles)

# # print all_brands one time

all_brands=[mob.get("brand")for mob in mobiles]
print(set(all_brands))

#print samsung mobiles
samsung_mob=[mob.get("title")for mob in mobiles if mob.get("brand")=="samsung"]
print(samsung_mob)

#print all mobiles available in range 23k to 40k
price_range=[mob.get("title") for mob in mobiles if mob.get("price") in range(23000,40001)]
print(price_range)

# print highest mobile price

max_price=0
for mob in mobiles:
    if mob.get("price")>max_price:
        max_price=mob.get("price")

hightes_mob_price=[mob.get("title")for mob in mobiles if mob.get("price")==max_price]
print(hightes_mob_price)

           #or 

costly_mobile=max(mobiles,key=lambda mob:mob.get("price"))
print(costly_mobile)



def get_price(mob):
    return mob.get("price")
max_cost_mobile=max(mobiles,key=get_price)
print(max_cost_mobile)

min_cost_mobile=min(mobiles,key=get_price)
print(min_cost_mobile)

sorted_mobiles=sorted(mobiles,key=get_price,reverse=True)
print(sorted_mobiles)

total=sum([mob.get("price") for mob in mobiles])
print(total)
