from movies_dict import movies

def above_5p5():
    l = [i["name"] for i in movies if i["imdb"] > 5.5]
    return l

print(above_5p5())