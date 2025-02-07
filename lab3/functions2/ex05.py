from movies_dict import movies

def category_imdb(category):
    l = [i["imdb"] for i in movies if i["category"] == category]
    return sum(l)/len(l)

print(category_imdb('Crime')) 
print(category_imdb('Romance')) 
print(category_imdb('Thriller')) 