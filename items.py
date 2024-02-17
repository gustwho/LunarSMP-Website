import os

def get():
    final = []
    for i in os.listdir("assets/items/"):
        if i.endswith(".png"):
            final.append(f'<div><img class="item" src="/assets/items;{i}"> <img class="tooltip" src="/assets/items;tooltip;{i}"></div>')

    return {"[ITEMS]":"\n".join(final)}