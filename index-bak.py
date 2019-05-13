#!python
print("content-type: text/html; charset=utf-8\n")
print()
import cgi, os

files=os.listdir('data')
listStr=''
for item in files:
    listStr=listStr+'<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
print(listStr)
form=cgi.FieldStorage()
if 'id' in form:
    pageId=form["id"].value
    description=open('data/'+pageId,'r').read()
else:
    pageId='Welcome'
    description='Hello, web'
print('''<!doctype html>
<html>
<head>
 <title>WEB2-Python</title>
 <meta charset="utf-8">
 <link rel="stylesheet" href="style.css">
  <script src="https://ajax.googleapis.com/ajax/libs/ jquery/3.4.0/jquery.min.js"></script>
 <script src="colors.js"></script>
  <!-- Global site tag (gtag.js) - Google Analytics -->
 <script async src="https://www.googletagmanager.com/gtag/js?id=UA-137651766-1"></script>
 <script>
   window.dataLayer = window.dataLayer || [];
   function gtag(){dataLayer.push(arguments);}
   gtag('js', new Date());

   gtag('config', 'UA-137651766-1');
 </script>

</head>
<body>

<h1><a href="index.py">WEB</a></h1>
  <div id="grid">
    <ol>
      <li><a href="index.py?id=HTML">HTML</a></li>
      <li><a href="index.py?id=CSS">CSS</a></li>
      <li><a href="index.py?id=JavaScript">JavaScript</a></li>
    </ol>
    <div id="article">
    <h2>{title}</h2>
    <p>{desc}</p>
    웹사이트(WebSite)
    </div>
  </div>
  <input type="button" value="night" onclick="
    nightDayHandler(this);
  ">
</body>
</html>
'''.format(title=pageId, desc=description,listStr=listStr))
