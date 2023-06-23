import json

with open('SoeulBodong.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    count = 0
    #print(data['DATA'])
    for item in data['DATA']:
        # if item['bubn'] != 0000:
        print(item)
        count+=1

print(count)



