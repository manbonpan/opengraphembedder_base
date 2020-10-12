HELLO_WORLD = """
<!DOCTYPE html>
<html xmlns:og="http://ogp.me/ns#">
    <head>
       <!-- Basic required tags -->
<meta name="theme-color" content="{}">
<meta property="og:url" content="{}">
<meta property="og:title" content="EMBEDITT">
<meta property="og:description" content="IZZA FUCKING EMBEDER BY MANBONPAN WTF U EXPECTING BISH">
<meta property="og:image" content="https://i.kym-cdn.com/entries/icons/facebook/000/000/935/puking-rainbows.jpg">
<!-- Optional tags but recommended -->
<meta property="og:type" content="video.other">
<!-- Media related tags -->
<meta property="og:video:url" content="{}">
<meta property="og:video:secure_url" content="{}">
<meta property="og:video:type" content="video/mp4">
<meta property="og:video:width" content="640">
<meta property="og:video:height" content="360">
    </head>

<body>

YEET.



</body>
</html>"""


from urllib.parse import urlparse
from urllib.parse import parse_qs
import random
r = lambda: random.randint(0,255)


def application(environ, start_response):
    if environ.get('PATH_INFO')[0] == '/':
        d = parse_qs(environ['QUERY_STRING'])
        mode = d.get('mode', [''])[0]
        sauce = d.get('source',[''])[0]
        status = '200 OK'
        x='#%02X%02X%02X' % (r(),r(),r())
        content = HELLO_WORLD.format(x,sauce,sauce,sauce)
    else:
        status = '404 NOT FOUND'
        content = 'Page not found.'
    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    yield content.encode('utf8')
