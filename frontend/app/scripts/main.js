// This hack will compensate mobile control section
// vh works on desktop version fine

const element = document.getElementById('banner');

let size = function() {
	return window.innerHeight;
};

const vpHack = function(size, element) {
	if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
		// banner height calculation - get vh and extract header
		element.style.height = `${size - 60}px`;
		element.style.transition = '0.5s';
	}
};

// listen for orientation change
window.addEventListener('orientationchange', function() {
	window.setTimeout(function() {
		vpHack(size(), element);
	}, 200);

});

vpHack(size(), element);