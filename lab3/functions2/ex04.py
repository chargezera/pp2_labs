from movies_dict import movies

def average_imdb(l):
    d = [i["imdb"] for i in movies if i["name"] in l]
    return sum(d)/len(l)

print(average_imdb(["Hitman", "Love", "AlphaJet", "The Help", "Joking muck"]))
