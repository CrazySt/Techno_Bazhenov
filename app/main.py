import pprint;
import datetime
def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/html')
    ]
    body = 'time:'
    body += datetime.datetime.now().strftime("%H:%M:%S")
    body += '\n raw '
    body += environ['RAW_URI']
    body += '\n path_info: '
    body += environ['PATH_INFO']
    start_response(status, headers)
    return [body.encode('utf-8')]
