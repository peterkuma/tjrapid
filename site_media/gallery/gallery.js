/* gallery.js
 *
 * Copyright (c) 2012 Peter Kuma
 *
 * Permission to use, copy, modify, and distribute this software for any
 * purpose with or without fee is hereby granted, provided that the above
 * copyright notice and this permission notice appear in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 * ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 * ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 * OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */
 
/*
 * Requires:
 *
 *     - MooTools 1.4.3 or newer: mootools.js (http://mootools.net),
 *     - for keyboard support (optional) the corresponding MooToolsMore:
 *       mootools-more.js with the Keyboard module (http://mootools.net/more/)
 */
 
/*
 * Turn obj into an interactive image gallery.
 *
 * Example:
 *
 * <div id="gallery" style="width: 900px; height: 600px" />
 * <script>
 * document.addEvent('domready', function() {
 *     gallery($('gallery'), {
 *         images: [
 *             {
 *                 src: 'image1.jpg',
 *                 desc: 'Description of image1.',
 *             },
 *             {
 *                 src: 'image2.jpg',
 *                 desc: 'Description of image2.',
 *             },
 *         ]
 *     });
 * });
 * </script>
 */
function gallery(obj, options) {
	if (!options.images)
		options.images = new Array();

	obj.addClass('gallery');
	
	/* Sheet. */
	var sheet = document.createElement('div');
	sheet.addClass('gallery-sheet');
	
	var width = obj.getStyle('width').toInt();
	var height = obj.getStyle('height').toInt();
	
	sheet.setStyle('width', width);
	sheet.setStyle('height', height);
	
	/* Place images on the sheet. */
	var offset = 0;
	options.images.each(function(image) {
		var wrapper = document.createElement('div');
		wrapper.addClass('gallery-wrapper');
		wrapper.setStyle('position', 'absolute');
		wrapper.setStyle('top', 0);
		wrapper.setStyle('left', offset);
		wrapper.setStyle('width', width);
		wrapper.setStyle('height', height);
		sheet.appendChild(wrapper);

		var img = document.createElement('img');
		img.src = image.src;
		img.height = height;
		img.setStyle('display', 'block');
		img.setStyle('margin', '0 auto');
		wrapper.appendChild(img);

		offset += width;
	});	
	obj.appendChild(sheet);	
	
	/* Bottom description panel. */
	var desc = document.createElement('div');
	desc.addClass('gallery-desc');
	desc.setStyle('height', 0);
	desc.setStyle('opacity', 0.7);
	desc.p = document.createElement('p');
	desc.set('tween', {duration: 'short'});
	desc.appendChild(desc.p);

	function updateDesc(n) {
		var descFx = new Fx.Tween(desc, {
			duration: 300,
			property: 'height',
			link: 'chain',
		});
		
		if (options.images.length > n && options.images[n].desc) {
			/* Alter height. */
			descFx.addEvent('complete', function() {
				desc.p.innerHTML = options.images[n].desc;
				desc.p.fade(1);
			});
			desc.p.fade(0);
			var tmpdesc = document.createElement('div');
			tmpdesc.addClass('gallery-desc');
			tmpdesc.setStyle('visibility', 'hidden');
			tmpdesc.p = document.createElement('p');
			tmpdesc.p.innerHTML = options.images[n].desc;
			tmpdesc.appendChild(tmpdesc.p);
			obj.appendChild(tmpdesc);
			h = tmpdesc.getStyle('height');
			obj.removeChild(tmpdesc);
			descFx.start(h);
		} else {
			desc.p.innerHTML = '';
			desc.p.fade(0);
			descFx.start(0);
		}
	}
	updateDesc(0);
	
	/* Image switching (left and right arrows). */
	var n = 0;
	
	var mouseover = 0;
	
	function switchTo(n) {
		var fx = new Fx.Tween(sheet, {
			duration: 'short',
			property: 'left'
		});
		fx.start(-n*width);
		updateDesc(n);
		if (n == 0)
			leftArrow.fade(0);
		else
			leftArrow.fade(mouseover*0.8);
		if (n == options.images.length - 1)
			rightArrow.fade(0);
		else
			rightArrow.fade(mouseover*0.8);
	}
 	
	var leftArrow = document.createElement('div');
	leftArrow.addClass('gallery-left');
	leftArrow.setStyle('width', width*0.3);
	leftArrow.setStyle('height', height);
	leftArrow.setStyle('opacity', 0);
	leftArrow.addEvent('click', function() {
		if (n > 0) switchTo(n = n-1);
	});
	obj.appendChild(leftArrow);
	
	var rightArrow = document.createElement('div');
	rightArrow.addClass('gallery-right');
	rightArrow.setStyle('width', width*0.3);
	rightArrow.setStyle('height', height);
	rightArrow.setStyle('opacity', 0);
	rightArrow.addEvent('click', function() {
		if (n < options.images.length - 1) switchTo(n = n+1);
	});
	
	rightArrow.set('tween', {duration: 'short'});
	leftArrow.set('tween',  {duration: 'short'});
	
	obj.addEvent('mouseover', function() {
		mouseover = 1;
		if (n > 0)
			leftArrow.fade(0.8);
		if (n < options.images.length - 1)
			rightArrow.fade(0.8);
	});
	
	obj.addEvent('mouseout', function() {
		mouseover = 0;
		leftArrow.fade(0);
		rightArrow.fade(0);
	});
	
	/* Keyboard control. */
	if (typeof Keyboard != 'undefined') {
		var kb = new Keyboard({
			defaultEventType: 'keydown',
			events: {
				'left': function() {
					if (n > 0) switchTo(n = n-1);
				},
				'right': function() {
					if (n < options.images.length - 1) switchTo(n = n+1);
				}
			}
		});
		kb.activate();
	}
	
	obj.appendChild(desc);
	obj.appendChild(leftArrow);
	obj.appendChild(rightArrow);
}
