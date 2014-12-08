import sys, time, os, collections
import threading
import logger
import HTTPServer

from Commander import *

Online_devices = {}

def v1_connect(name):
	global Online_devices
	Online_devices[name] = []

def v1_get_data(name):
	data = Online_devices.get(name)
	if not data:
		Log.info('No data for %s', name)
		return None
	return data


def run_commands():
	global Online_devices
	while True:
		try:
			show_options()
			dname, data = parse_input()
			if dname:
				Online_devices[dname].append(data)
			else:
				print Online_devices
		except Exception, fault:
			Log.traceback(fault)
			time.sleep(10)



def register_methods(srv):
	srv.register_method('v1_connect', v1_connect)
	srv.register_method('v1_get_data', v1_get_data)	

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: python Server port"
		os._exit(0)
	
	port = int(sys.argv[1])
	httpserver = HTTPServer.HTTPServer('0.0.0.0', port)
	register_methods(httpserver)
	#Commander.run()
	threading.Thread(target=run_commands).start()
	httpserver.start()
