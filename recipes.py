import os

def get():
    final = []
    for i in os.listdir("assets/items/"):
        if os.path.isfile(f"assets/items/recipes/{i}"):
            final.append(f'<div class="recipe"> <img class="table" src="/assets/items;recipes;{i}"> <img class="result" src="/assets/arrow.png"><img class="result" src="/assets/items;{i}"></div>')

    return {"[RECIPES]":"\n".join(final)}