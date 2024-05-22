dic={
    "name":"sagar",
    "student":{
        "phy":89,
        "che":56
    }
}
#print(dic["student"]["phy"])
print(dic.keys())               #.keys() function

print(dic.values())                 #.values() function

print(dic.items())

print(dic.get("name"))          #jyare pan name difine nay hoi ane print karvaso to none avse

print(dic["name"])                  #jyare pan name difine nay hoi ane print karvaso to error avse

new={"city":"rajkot"}
dic.update(new)
print(dic) 
