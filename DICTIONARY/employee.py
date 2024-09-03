employee={"name":"rintu","dept":"r&d","salary":50000,"offer":1000,"extra_working_days":2}

#print all key values

for k,v in employee.items():

    print(k,v)

#check extra working days is present

if ("extra_working_days") in employee:

    net_pay=employee.get("extra_working_days")*employee.get("offer") + employee.get("salary")

    print(net_pay)

else:
    net_pay= employee.get("salary")
    
    print(net_pay)