x = {
    "fruit": "Révolutuion",
    "size": "Large",
    "color": "Red"
}

# x_doc = json.loads(json.dumps(x))
print(json.dumps(x, ensure_ascii=False))

with open("example.json","w", encoding='utf-8') as jsonfile:
    json.dump(x,jsonfile,ensure_ascii=False)