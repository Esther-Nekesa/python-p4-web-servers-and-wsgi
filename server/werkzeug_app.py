#!/usr/bin/env python3
# server/werkzeug_app.py
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    # This print statement shows up in the terminal when a request is received
    print(f'This web server is running at {request.remote_addr}')
    
    # This is the response content that the browser will display
    return Response('A WSGI generated this response!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )
