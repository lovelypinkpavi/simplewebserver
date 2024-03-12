from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>Top software companies with revenue table</title>
</head>
<body bgcolor="pink">
<table border="3" cellspacing="4" cellpadding="8" height="30" width="80">
<h1>Top Software Companies</h1>
<caption>Top Five Revenue Generating Software Companies</caption>
<tr>
<th>Rank</th>
<th>Company</th>
<th>Revenue</th>
</tr>
<tr>
<td>1</td>
<td>SAP</td>
<td>13975.8</td>
</tr>
<tr>
<td>2</td>
<td>Dassault Systemes</td>
<td>1783.5</td>
</tr>
<tr>
<td>3</td>
<td>Sage</td>
<td>1460.9</td>
</tr>
<tr>
<td>4</td>
<td>Wincor Nixdorf</td>
<td>1169.0</td>
</tr>
<tr>
<td>5</td>
<td>Hexagon</td>
<td>1154.0</td>
</tr>
</tr>
</table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()