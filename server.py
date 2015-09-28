import BaseHTTPServer
import SimpleHTTPServer
import SocketServer
from cStringIO import StringIO
import PIL.Image
import threading
import evdev

from uinput_map import js_map

SERVER_PORT = 8080

send_key_lock = threading.Lock()
def send_key(js_keycode, state):
	if js_keycode not in js_map:
		raise KeyError("Unkown javascript keycode: {}".format(js_keycode))
	send_key_lock.acquire()
	with evdev.UInput() as uinput:
		uinput.write(evdev.ecodes.EV_KEY, js_map[js_keycode], 1 if state else 0)
		uinput.syn()
	send_key_lock.release()

class ThreadedHTTPServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
	"""Handle requests in a separate thread."""
	daemon_threads = True

# https://github.com/ev3dev/ev3dev/wiki/Using-the-LCD
fbmap = {chr(i): ''.join(chr(int(x)) for x in '{:08b}'.format(i)[::-1]) for i in range(256)}
def jpg_from_fb():
	with open('/dev/fb0', 'r') as f:
		x = ''.join(fbmap[char] for char in f.read())
	sio = StringIO()
	im = PIL.Image.fromstring('P', (192,128), x)
	im.putpalette((124,145,111, 0,0,0))
	im.convert('RGB').crop((0,0,178,128)).save(sio, 'JPEG')
	jpg = sio.getvalue()
	sio.close()
	return jpg

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		"""Serve a GET request."""
		if self.path.endswith('mjpg'):
			self.send_response(200)
			self.send_header('Content-Type', 'multipart/x-mixed-replace;boundary=boundarydonotcross')
			self.end_headers()
			i = 0
			while True:
				jpg = jpg_from_fb()
				self.send_header('Content-type', 'image/jpeg')
				self.send_header('Content-length', len(jpg))
				self.end_headers()
				self.wfile.write(jpg)
				self.wfile.write('--boundarydonotcross')
				print 'written', i
				i+=1
		else:
			f = self.send_head()
			if f:
				try:
					self.copyfile(f, self.wfile)
				finally:
					f.close()
	def do_POST(self):
		if self.path.endswith('key'):
			self.send_response(200)
			content_len = int(self.headers.getheader('content-length', 0))
			content = self.rfile.read(content_len)
			jskc, state = content.split(',')
			send_key(int(jskc), int(state))

if __name__ == '__main__':
	print "Running on port {}".format(SERVER_PORT)
	httpd = ThreadedHTTPServer(('', SERVER_PORT), MyHandler)
	httpd.serve_forever()
