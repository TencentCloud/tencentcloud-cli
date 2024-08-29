import time
import traceback
import socket
from threading import Thread
from tccli import oauth

try:
    from urlparse import urlparse, parse_qs
    from Queue import Queue
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
    from SocketServer import ThreadingTCPServer, TCPServer
except ImportError:
    from urllib.parse import urlparse, parse_qs
    from queue import Queue
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from socketserver import ThreadingTCPServer, TCPServer


# chrome keeps previous connection alive, so use threading to avoid blocking
class ThreadingHTTPServer(ThreadingTCPServer):
    allow_reuse_address = 1

    def server_bind(self):
        """Override server_bind to store the server name."""
        TCPServer.server_bind(self)
        host, port = self.socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port


class HTTPHandler(BaseHTTPRequestHandler):
    result_queue = Queue(1)

    def do_GET(self):
        try:
            parsed_url = urlparse(self.path)
            query_vals = parse_qs(parsed_url.query)

            open_id = query_vals.get("open_id")[0]
            access_token = query_vals.get("access_token")[0]
            refresh_token = query_vals.get("refresh_token")[0]
            expires_at = int(query_vals.get("expires_at")[0])
            state = query_vals.get("state")[0]
            redirect_url = query_vals.get("redirect_url")[0]
            site = query_vals.get("site")[0]
            token = {
                "openId": open_id,
                "accessToken": access_token,
                "refreshToken": refresh_token,
                "expiresAt": expires_at,
                "state": state,
                "site": site,
            }
            cred = oauth.get_temp_cred(token["accessToken"], token["site"])
            self.result_queue.put((token, cred))
            self.send_response(307)
            self.send_header("Location", redirect_url)
            self.end_headers()
        except Exception:
            err = traceback.format_exc()
            print(err)
            self.send_response(400)
            self.end_headers()
            self.wfile.write("login failed due to the following error:\n\n".encode("utf-8"))
            self.wfile.write(err.encode("utf-8"))
            self.wfile.flush()

    # suppress debug message
    def log_message(self, format, *args):
        pass


def try_run(start_search_port, end_search_port):
    port = start_search_port

    while port <= end_search_port:
        server_address = ('', port)
        try:
            ThreadingHTTPServer.daemon_threads = True
            httpd = ThreadingHTTPServer(server_address, HTTPHandler)
            t = Thread(target=httpd.serve_forever)
            t.setDaemon(True)
            t.start()
            return port, HTTPHandler.result_queue
        except socket.error:
            port += 1

    raise socket.error("no port available from range [%d, %d]" % (start_search_port, end_search_port))
