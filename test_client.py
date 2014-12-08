import httplib
host_name = None
def make_rpc(method, data):
	conn = httplib.HTTPConnection(hostname)
	urlpath = '/api/%s' % (method.replace('.', '/'))
	conn.request("POST", urlpath, data)
	response = conn.getresponse()
	return response.read()