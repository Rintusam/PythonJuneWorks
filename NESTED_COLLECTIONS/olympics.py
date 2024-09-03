olympic_medal_count = [
    {"country": "United States", "gold": 39, "silver": 41, "bronze": 33},
    {"country": "China", "gold": 38, "silver": 32, "bronze": 18},
    {"country": "Japan", "gold": 27, "silver": 14, "bronze": 17},
    {"country": "Great Britain", "gold": 22, "silver": 21, "bronze": 22},
    {"country": "Russia", "gold": 20, "silver": 28, "bronze": 23},
    {"country": "Australia", "gold": 17, "silver": 7, "bronze": 22},
    {"country": "Netherlands", "gold": 10, "silver": 12, "bronze": 14},
    {"country": "France", "gold": 10, "silver": 12, "bronze": 11},
    {"country": "Germany", "gold": 10, "silver": 11, "bronze": 16},
    {"country": "Italy", "gold": 10, "silver": 10, "bronze": 20}
]

# # q1 COUNTRY WITH MOST NUMBER OF GOLD MEDALS
# max_gold_medal=0
# for md in olympic_medal_count:
#     if md.get("gold")>max_gold_medal:
#         max_gold_medal=md.get("gold")
# highest_medal=[md.get("country")for md in olympic_medal_count if md.get("gold")==max_gold_medal]
# print(highest_medal)

#MEDAL COUNT FOR EACH COUNTRIES
for country_data in olympic_medal_count:
    country=country_data["country"]
    gold=country_data["gold"]
    silver=country_data["silver"]
    bronze=country_data["bronze"]

    total_medals=gold+silver+bronze
    print(f"{country}={total_medals}")

#COUNTRY WITH LEAST NUMBER OF MEDALS
low_medal=0
least_medals=[low_medal for i in total_medals if total_medals<low_medal ]
print(least_medals)
