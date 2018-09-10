from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
import time
import argparse


class myHandler(BaseHTTPRequestHandler):
    delimiter='\n'+'-'*40+'\n'
    def response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html>Across the Great Wall, we can reach every corner in the world!</html>")
    def do_POST(self):
        self.response()
        post_data = self.rfile.read(int(self.headers['content-length']))
        print "\n",self.headers,"\n",post_data,self.delimiter

    def do_HEAD(self):
        self.response()
        print "\n",self.headers,self.delimiter

    def do_GET(self):
        self.response()
        print "\n",self.headers, self.delimiter


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p, --port', dest='port', required=False, help="server port", default=2333, type=int)
    parser.add_argument('-l, --local', dest='isLocal', required=False, nargs='?',default=0,const=1,help="if server is available only from localhost")
    # parser.print_help()
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        exit()
    IS_LOCAL=args.isLocal
    PORT_NUMBER=args.port
    HOST_NAME = 'localhost'  if IS_LOCAL else '0.0.0.0'
    server = HTTPServer((HOST_NAME, PORT_NUMBER), myHandler)
    print time.asctime(),'Starting server on %s:%d, use <Ctrl-C> to stop\n\n' % (HOST_NAME,PORT_NUMBER)
    try:
        server.serve_forever()
    except:
        server.server_close()
        print "\n\n", time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
