#!/usr/bin/python 
#coding=utf-8

__version__ = "0.2"

import BaseHTTPServer
import re
import telnetlib
import daemon

class HealthCheckHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    server_version = "HealthCheck/" + __version__

    # disable GET request 
    def do_GET(self):
        self.send_response(405)
        return None

    def do_HEAD(self):
        # expect request healthcheck_PORT
        request = self.path
        prog = re.compile("/healthcheck_\d{1,5}$") 
        result = prog.match(request)
        if not result :
            self.send_response(503)
        else : 
            testport = request.split("_")[1]
            try:
                telnetlib.Telnet(host="localhost", port=testport, timeout=3)
                self.send_response(200)
            except Exception, e:
                self.send_response(503)
            finally:
                self.end_headers()

        return None


def main(HandlerClass = HealthCheckHTTPRequestHandler,
        ServerClass = BaseHTTPServer.HTTPServer):
    with daemon.DaemonContext():
        BaseHTTPServer.test(HandlerClass, ServerClass)


if __name__ == "__main__" :
    main()
