function getElementsByClassName(className, tag, elm)
{
	var testClass = new RegExp("(^|\\\\s)" + className + "(\\\\s|$)");
	var tag = tag || "*";
	var elm = elm || document;
	var elements = (tag == "*" && elm.all)? elm.all : elm.getElementsByTagName(tag);
	var returnElements = [];
	var current;
	var length = elements.length;
	for(var i=0; i<length; i++){
		current = elements[i];
		if(testClass.test(current.className)){
			returnElements.push(current);
		}
	}
	return returnElements;
}

function prependChild(parent, node) {
	if (parent.firstChild) {
		parent.insertBefore(node, parent.firstChild);
	} else {
		parent.appendChild(node);
	}
}

function loadRichEdit()
{
	var div = document.createElement("div");
	div.style.margin = '0 0 5px 0';
	var a = document.createElement("a");
	a.href = "#"
	a.onclick = function() {
		w = window.open('http://www.tjrapid.sk/site_media/file-browser/file-browser.php', null, "width=830,height=530");
		w.focus();
		w.onunload = function() { document.getElementsByTagName('body')[0].innerHTML += w.document.getElementById("path").value; };
	};
	var t = document.createTextNode("Insert File");
	a.appendChild(t);
	var e = document.getElementsByTagName("textarea")[0].parentNode;
	div.appendChild(a);
	prependChild(e, div);
}

window.addEventListener('load', loadRichEdit, true);
