import os

def get():
    final = []
    for i in os.listdir("assets/items/cosmetic_demo/"):
        final.append(f'<p>{i.split(".")[0]}</p><br><img class="cosmeticview" src="/assets/items;cosmetic_demo;{i}">')

    return {"[COSMETICS]":"\n".join(final)}