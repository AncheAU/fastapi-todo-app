t = [
    {
        "name": "Abdullahi"
    },
    {
        "name": "Usman"
    },
    {
        "name": "Sadiq"
    }
]


for i in t:
    if  "ad" in i["name"].lower() :
        print(i)
    else:
        print("Does not exist.")



