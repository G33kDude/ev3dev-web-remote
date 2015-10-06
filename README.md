# ev3dev-web-remote

## prerequisites

On the ev3 run `apt-get install python-evdev`.

## running

The easiest way to try it, is to clone the repo directly on the ev3:

```
git clone https://github.com/G33kDude/ev3dev-web-remote.git
cd ev3dev-web-remote
./server.py
```

Now the ev3 remove is accesible as `http://EV3DEV:8080` (via windows naming
service) or `http://ev3dev.local:8080` (via mdns).

