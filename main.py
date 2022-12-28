from flask import Flask, Response
from json import load
from os import walk
from random import choice

app = Flask('API')
url = 'https://bocchi-api.vercel.app'

@app.get('/')
def func():
  for root, d, imgs in walk('./imgs/'):
    img = choice(imgs)

  rbee = open(f'./imgs/{img}', 'rb') # rbee 
  return Response(rbee, mimetype='image/jpg')

@app.get('/<img>')
def funcc(img: str):
  rbee = open(f'./imgs/{img}', 'rb') # rbee 
  return Response(rbee, mimetype='image/jpg')

@app.get('/JSON')
def funccc():
  for root, d, imgs in walk('./sauces/'):
    img = choice(imgs)

  JSON = load(open(f'./sauces/{img}'))
  imgURL = JSON['imgURL']
  JSON['imgURL'] = f'{url}/{imgURL}'
  return JSON

@app.get('/JSON/<img>')
def funcccc(img: str):
  JSON = load(open(f'./sauces/{img}'))
  imgURL = JSON['imgURL']
  JSON['imgURL'] = f'{url}/{imgURL}'
  return JSON

# Un-comment this if not using vercel ;)
# app.run(port=3000) 