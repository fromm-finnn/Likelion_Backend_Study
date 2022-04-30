from django.shortcuts import render, HttpResponse

topics = [
  {'id':1, 'title':'routing', 'body':'Routing is...'},
  {'id':2, 'title':'view', 'body':'View is...'},
  {'id':3, 'title':'Model', 'body':'Model is...'},
]

def HTMLtemplate(articleTag):
  global topics
  ol = ''
  for topic in topics:
    ol += '<li><a href = "/read/{}">{}</a></li>'.format(topic["id"],topic["title"])
  return f'''
  <html>
  <body>
    <h1><a href = '/'>Django</a></h1>
    <ol>
      {ol}
    </ol>
    {articleTag}
  </body>
  </html>
  '''

def index(request):
  article = '''
  <h2>Welcome</h2>
  Hello, Django
  '''
  return HttpResponse(HTMLtemplate(article))

def read(request, id):
  global topics
  article = ''
  for topic in topics:
    if topic['id'] == int(id):
      article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
  return HttpResponse(HTMLtemplate(article))

def create(request):
  return HttpResponse('Create')

