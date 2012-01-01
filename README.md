##README

HAProxy can be use to proxy for TCP and HTTP-based applications. But when we use it to proxy the TCP request, how can 
we perform the health-check? May this tool can help u.

This tool is based on BaseHTTPServer, "HEAD http://localhost:8000/healthcheck_6379" will examine the port 6379, when 
it is alive, return 200. Otherwise, return 503.
 
### HAProxy Config:
    global
    …
    defaults
    …
    listen redis
        bind 0.0.0.0:6379
        balance roundrobin
        mode   tcp
        option httpchk HEAD /healthcheck_6379 HTTP/1.0\r\n
        server redis1 192.168.1.50:6379 check port 8000 inter 5000 fall 3
        server redis2 192.168.1.51:6379 check port 8000 inter 5000 fall 3

### backend (redis as an example)
python healthcheck.py
