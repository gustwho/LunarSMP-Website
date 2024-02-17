import os
use_cache = True

template = ""
with open("template.html","r") as f:
    template = f.read()
cache = {}
def read_with_cache(file):
    if not file in cache.keys() or not use_cache:
        with open(file,"r") as f:
            cache[file] = f.read()
    return cache[file]

def get_name(data):
    if len(data.split("<!--Name: ")) > 1:
        return data.split("<!--Name: ")[1].split("-->")[0]
    return 0

def gen_page(page):
    final = []
    data = read_with_cache(page)

    pagename = get_name(data)
    for i in os.listdir("./pages/"):
        name = get_name(read_with_cache(f"pages/{i}"))
        if name != 0:
            pn = i.split(".")[0]
            if pagename == name:
                final.append(f'<a href="/p/{pn}/" class="current">&gt; {pagename} &lt;</a>')
            else:
                final.append(f'<a href="/p/{pn}/">{name}</a>')

    return template.replace("[PAGE]",data).replace("[LINKS]","\n".join(final))