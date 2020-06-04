from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import sys
import subprocess


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        print(self.path)
        if self.path == '/':
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(open("index.html", 'rb').read())
            return
        if self.path.endswith('.html'):
            self.send_header("Content-type", "text/html")
        elif self.path.endswith('.js'):
            self.send_header("Content-type", 'text/javascript')
        else:
            self.send_response(418)
            self.wfile.write(bytes(
                r"""418 I am a teapot

             ;,'
     _o_    ;:;'
 ,-.'---`.__ ;
((j`=====',-'
 `-\     /
    `-=-'     hjw
            """,
                encoding="UTF-8"))
            return
        self.end_headers()
        self.wfile.write(open(self.path.replace('/', ''), 'rb').read())

    def do_POST(self):
        for i in str(self.headers).split('\n'):
            if i.startswith("Value"):
                with open('movement.json', 'w') as f:
                    value = [char for char in i.replace('Value: ', '')]
                    direction = value[0]
                    amount = ''.join(value[1:])
                    movement_dict = '{' + f'"direction": "{direction}", "amount": "{amount}"' + '}'
                    print(movement_dict)
                    f.write('{' + f'"direction": "{direction}", "amount": "{amount}"' + '}')

        subprocess.call(['python', 'interpretter.py'])

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()


def run():
    myServer = HTTPServer((hostName, hostPort), MyServer)
    print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass

    myServer.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))


if __name__ == "__main__":
    hostName = "localhost"
    try:
        hostPort = int(sys.argv[1])
    except Exception:
        hostPort = 8080
    run()
