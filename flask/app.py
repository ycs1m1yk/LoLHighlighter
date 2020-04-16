import requests
from flask import Flask, render_template, request, url_for
 
app = Flask(__name__, static_url_path='/static')

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/highlight')
def highlight(youtube_url=None):
  if request.method == 'POST':
    pass

  elif request.method == 'GET':
    url = request.args.get('youtube_url') 
    url = str(url)
    print(url)
    
  return render_template('index.html', youtube_url=url)
 
@app.route('/about')
def about():
  return render_template('sample.html')

app.run(debug=True)