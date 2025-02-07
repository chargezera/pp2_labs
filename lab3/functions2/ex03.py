from movies_dict import movies

def categories(category = "Thriller"):
    l = [i['name'] for i in movies if i['category']==category]
    return l

print(categories())