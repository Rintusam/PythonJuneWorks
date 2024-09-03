vehicle_numbers=[
                "KL31J0181",
                "KL49L6815",
                "KL64A9903",
                "KL07BQ1181",
]

f=open("C:\\Users\\Rintu Sam\\Desktop\\PythonJuneWorks\\FILE_WORKS\\vehicle_num.txt","w")

for vehicle in vehicle_numbers:

    f.write(vehicle+"\n")