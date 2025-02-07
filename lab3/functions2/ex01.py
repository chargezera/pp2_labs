from movies_dict import movies

def check(name = "Love"):
    l = [i["imdb"] for i in movies if i["name"]==name]
    return l[0] > 5.5

print(check("Love"))
print(check("AlphaJet"))