document.onkeydown = function(e) {
	e.preventDefault();
	if (!e.repeat) {
		var xhr = new XMLHttpRequest();
		xhr.open('POST', '/send.key', true);
		xhr.send(e.keyCode + ',1');
	}
}

document.onkeyup = function(e) {
	e.preventDefault();
	if (!e.repeat) {
		var xhr = new XMLHttpRequest();
		xhr.open('POST', '/send.key', true);
		xhr.send(e.keyCode + ',0');
	}
}