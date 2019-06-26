from app import app
@app.route('/')
@app.route('/index')
def index():
    return '''
    <html>
     <head>
      <title> HOME PAGE-MicroBlog</title>
      <style>
      h1{
         color:orange
         background-color:blue        }
      </style>
     </head>
      <body>
      <h1 align=center> Hello python!</h1>
     </body>
    </html>'''

