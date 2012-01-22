var current;

$(document).ready(function() {

	il = $("#pix li");
	if (il.length === 0) {
		$('#cam').html("<h1>No JPGs image files found!</h1>");
	}

	il.click(function(e) {
		e.preventDefault();
		il.eq(current).removeClass('active');
		current = ($(this).index());
		il.eq(current).addClass('active');
		title();
	});

	/* Total number of images */
	total = il.length;

	/* Current image index */

	if (location.hash) {
		f = il.find('a[href="' + location.hash.substr(1) + '"]:last');
		current = f.closest('li').index();
	} else {
		current = 0;
	}
	il.eq(current).addClass('active');
	title();

	$(document).keydown(function(e) {
		if (e.keyCode == 37) {
			prev();
		}
		if (e.keyCode == 39) {
			next();
		}
	});

	$('#cam').click(function() {
		next();
	});

});

function next() {
	// console.log("Next...");
	il.eq(current).removeClass('active');
	current = ((current + 1) == total ? 0: (current + 1));
	loadImage(current + 1); // Load the one after the next in advance
	il.eq(current).addClass('active');
	title();
}

function prev() {
	il.eq(current).removeClass('active');
	current = ((current - 1) < 0 ? (total - 1) : (current - 1));
	il.eq(current).addClass('active');
	title();
}

function loadImage(i) {
	if (il[i].img) { return; }
	// console.log("Loading ... " + i);
	il[i].img = new Image();
	il[i].img.src = il[i].textContent;
	il[i].img.onload = function() {
		width = this.width > window.innerWidth ? window.innerWidth: this.width;
		height = this.height > window.innerHeight ? window.innerHeight: this.height;
		this.width = width;
		this.height = height;
	};
}

function title() {

	/* Update which image is visible and the label */
	if (il[current].img) {
		$('#cam').html(il[current].img);
	} else {
		loadImage(current);
		$('#cam').html(il[current].img);
	}

	document.title = ("[" + (current + 1) + " of " + total + "]");
	location.hash = il[current].textContent;

}

