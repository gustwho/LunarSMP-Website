from pager import gen_page
from flask import Flask
from flask import send_from_directory

import items
import recipes
import cosmetics

app = Flask(__name__)
htmlmap = {
    "recipes": recipes.get,
    "items": items.get,
    "cosmetics": cosmetics.get,
}

def safe_path(path): # i dont code security someone can probably still get around this!
    return path.replace("..","")

@app.route('/')
def home():
    return gen_page('pages/home.html')

@app.route('/p/<name>/')
def p(name):
    data = gen_page(f'pages/{name}.html')
    if name in htmlmap.keys():
        k = htmlmap[name]()
        for i in k.keys():
            v = k[i]
            data = data.replace(i,v)
    return data

@app.route('/css/<file>')
def css(file):
    return send_from_directory('css',file)

@app.route('/assets/<file>')
def asset(file):
    return send_from_directory('assets',file.replace(";","/"))

@app.errorhandler(404)
def page_not_found(e):
    return gen_page(f'pages/notfound.html')

@app.errorhandler(500)
def page_not_found(e):
    return gen_page(f'pages/notfound.html')