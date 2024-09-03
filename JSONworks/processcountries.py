from json import load

f=open("C:\\Users\\Rintu Sam\\Desktop\\PythonJuneWorks\\JSONworks\\countries.json","r",encoding="UTF-8")

data=load(f)

# print(len(data))

def fetch_country_by_name(name):

   return[c for c in data if c.get("name")==name][0]

country_data=fetch_country_by_name("Barbados")

# print(country_data)

if "regionalBlocs" in country_data:
   
    block_data=country_data.get("regionalBlocs")[0]

    if "otherNames" in block_data:
      
      print(block_data.get("otherNames"))
    
    else:
      
      print(country_data.get("name"))

def get_area(dic):
   
    if "area" in dic:
      
      return dic.get("area")
    
    else:
       return 0
    
biggest_country_by_area=max(data,key=get_area)
# print(biggest_country_by_area.get("name"))


for c in data:
    for l in c.get("languages"):
      
        if l.get("name")=="English":

            print(c.get("name"))
        
        
           

         

   
         
       