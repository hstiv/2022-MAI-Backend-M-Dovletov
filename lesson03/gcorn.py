from datetime import datetime

def app(environ, start_response):
    """Simplest possible application object"""
    now = datetime.now()
    data = "Current date is %d.%d.%d" % (now.day, now.month, now.year)
    status = '200 OK'
    data = data.encode("ascii")
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])