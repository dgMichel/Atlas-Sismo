import json 


with open("anuales.json","r",encoding='utf-8') as file:
    data=json.load(file)
    
with open("anuales.json","w",encoding='utf-8') as file:
    json.dump(data,file,indent=4)