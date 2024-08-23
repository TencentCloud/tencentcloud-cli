import traceback
from BaseHTTPServer import BaseHTTPRequestHandler
import socket
from threading import Thread

try:
    from urlparse import urlparse, parse_qs
    from Queue import Queue
    from BaseHTTPServer import HTTPServer
except ImportError:
    from urllib.parse import urlparse, parse_qs
    from queue import Queue
    from http.server import HTTPServer


class HTTPHandler(BaseHTTPRequestHandler):
    result_queue = Queue(1)
    shutdown = None

    def do_GET(self):
        print("req")
        try:
            parsed_url = urlparse(self.path)
            query_vals = parse_qs(parsed_url.query)

            open_id = query_vals.get("open_id")[0]
            access_token = query_vals.get("access_token")[0]
            refresh_token = query_vals.get("refresh_token")[0]
            expires_at = int(query_vals.get("expires_at")[0])
            state = query_vals.get("state")[0]
            redirect_url = query_vals.get("redirect_url")[0]
            self.result_queue.put({
                "open_id": open_id,
                "access_token": access_token,
                "refresh_token": refresh_token,
                "expires_at": expires_at,
                "state": state,
            })
            self.send_response(307)
            self.send_header("Location", redirect_url)
            self.end_headers()
            print("shutdown")
            self.shutdown()
        except Exception:
            err = traceback.format_exc()
            print(err)
            self.send_response(400)
            self.end_headers()
            self.wfile.write("login failed due to the following error:\n\n")
            self.wfile.write(err)
            self.wfile.flush()

    def log_message(self, format, *args):
        pass


def try_run(start_search_port, end_search_port):
    port = start_search_port

    while port <= end_search_port:
        server_address = ('', port)
        try:
            httpd = HTTPServer(server_address, HTTPHandler)
            HTTPServer.request_queue_size = 1024
            HTTPServer.shutdown = httpd.shutdown
            t = Thread(target=httpd.serve_forever)
            t.setDaemon(True)
            t.start()
            print("start", port)
            return port, HTTPHandler.result_queue
        except socket.error:
            port += 1

    raise socket.error("no port available from range [%d, %d]" % (start_search_port, end_search_port))
