from urlparse import urlparse
import httplib
import base64

def show_options():
	print "1. Show online devices \n \
		   2. Send Data to device \n \
		   3. Send image to device \n \
		   4. Send webimage to device \n \
		   5. Exit"

def get_image_path(image_path):
	f = None
	try:
		f = open(image_path, 'r')
		data = f.read()
		data = base64.b64encode(data)
		fname = image_path.split('/')[-1]
		return {'fname' : fname, 'data' : data}
	finally:
		if f:
			f.close()

def get_webimage(weburl):
	parse_object = urlparse(weburl)
	if parse_object.scheme == 'http':
		cls = httplib.HTTPConnection
	elif parse_object.scheme == 'https':
		cls = httplib.HTTPSConnection
	conn = cls(parse_object.netloc)
	conn.request("GET", parse_object.path)
	r = conn.getresponse()
	data = r.read()
	data = base64.b64encode(data)
	conn.close()
	fname = weburl.split('/')[-1].split('.')[0] + "." + weburl.split('/')[-1].split('.')[1].split('?')[0] 
	return {'fname' : fname, 'data': data}

def parse_input():
	command_num = int(raw_input('Enter the command'))
	if command_num == 1:
		return None, None
	elif command_num == 2:
		dname = raw_input('Enter device')
		data = raw_input('Enter the data')
		return dname, data
	elif command_num == 3:
		dname = raw_input('Enter device')
		image_path = raw_input('Enter the image path')
		data = get_image_path(image_path)
		return dname, data
	elif command_num == 4:
		dname = raw_input('Enter device')
		imageurl = raw_input('Enter the webimage url')
		data = get_webimage(image_path)
		return dname, data
	elif command_num == 5:
		os._exit(0)


if __name__ == '__main__':
	print get_image_path('/home/prahlad/Documents/DarkSync/Client.py')
	print get_webimage("https://scontent-a-mxp.xx.fbcdn.net/hphotos-xpa1/v/t1.0-9/10696314_931888366830154_8577328321279875552_n.png?oh=82cec157028850f64fd9592f16e9c66e&oe=54FE7A2A")