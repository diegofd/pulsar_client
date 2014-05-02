import httplib
# https://docs.python.org/2/library/httplib.html
import urllib


class ControlServer:
    server = "192.168.56.101"
    port = 80

    def __init__(self):
        pass

    def read(self):
    	conn = httplib.HTTPConnection(self.server)
    	conn.request("GET", "/")

    def write(self):
    	params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    	conn = httplib.HTTPConnection(self.server)
    	conn.request("POST", "", params, headers)
    	response = conn.getresponse()

if __name__ == '__main__':
	controlserver = ControlServer()
	controlserver.read()
	controlserver.write()
