#!./env/bin/python3

import http.server 

class Serve(http.server.BaseHTTPRequestHandler):
    def do_GET(self): self.handleAll()
    def do_POST(self): self.handleAll()

    def fetchhtml(self, url):
        import requests

        try:
            return requests.get(url)
        except Exception as e:
            from sys import stderr
            print ( 'self.fetchhtml("%s") ended with an error: %s' % ( url, e ), file=stderr )
            return

    def relToFullUrl(self, rawUrl, response):
        from urllib.parse import urlparse
        from re import sub
        parsed_uri = urlparse( response.url )
        return '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri) + sub('^\/{1,}', '', rawUrl)

    def fetchQuotes(self, response):
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(response.text, 'html.parser')
        payload = []
        
        for quote in soup.findAll( 'div', {'class': 'quote'} ):
            item = dict()
            item['text'] = quote.select_one('span.text')
            item['text'] = item['text'].text if item['text'] else None

            item['author'] = quote.select_one('small.author')
            item['author'] = item['author'].text if item['author'] else None

            item['tags'] = []

            for tag in quote.select('a.tag'):
                tagItem = dict()
                tagItem['link'] = self.relToFullUrl(tag['href'], response) if tag else None
                tagItem['text'] = tag.text if tag else None

                item['tags'].append(tagItem)

            if item['text']:
                payload.append(item)

        pagination = dict(url_previous=None, url_next=None)

        prev = soup.select_one('nav .pager .previous a')

        if prev and hasattr(prev, 'href'):
            pagination['url_previous'] = self.relToFullUrl(prev['href'], response)

        nxt = soup.select_one('nav .pager .next a')

        if nxt and hasattr(nxt, 'href'):
            pagination['url_next'] = self.relToFullUrl(nxt['href'], response)

        return ( payload, pagination )

    def handleAll(self):
        import re
        from json import dumps

        requestUrl = re.sub( r'^\/http(s?)\:\/\/', r'http\1://', self.path, flags=re.IGNORECASE )

        if not requestUrl or not re.match(r'^http(s?)\:\/\/', requestUrl, flags=re.IGNORECASE):
            self.send_response(502)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            return self.wfile.write(b'{"success":false,"error":"Please submit a valid request URL."}')

        response = self.fetchhtml(requestUrl)

        if not response or not hasattr(response, 'text') or not response.text:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            return self.wfile.write(b'{"success":false,"error":"Internal error, request not successful."}')

        quotes, pagination = self.fetchQuotes(response)
        jsonResponse = dict(success=True)
        jsonResponse['items'] = quotes if quotes and len(quotes) else []
        jsonResponse['pagination'] = pagination

        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()

        self.wfile.write( str.encode( dumps(jsonResponse) ) )

if __name__ == '__main__':
    from os import environ
    address = ('0.0.0.0', int(environ.get('PORT', 8083))) # change to your machine IP and desired available port
    httpd = http.server.HTTPServer(address, Serve)
    print('Listening at http://%s' % ':'.join([ str(x) for x in address ]))
    httpd.serve_forever()
