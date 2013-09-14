function likebutton(el, url) {
    var dropdown;
    var button;

    init();

    function init() {
        button = el.querySelector('.button');
        el.removeAttribute('onmousedown');
        el.onmousedown = function(evt) {
            toggle();
            evt.stopPropagation();
        };
        dropdown = document.createElement('div');
        dropdown.className = 'dropdown';
        dropdown.style.top = button.offsetHeight + 5 + "px";
        add('facebook', '<iframe src="//www.facebook.com/plugins/like.php?href='+encodeURIComponent(url)+'&amp;height=20&amp;colorscheme=light&amp;layout=button_count&amp;action=like&amp;show_faces=false&amp;send=false" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:90px; height:21px;" allowTransparency="true"></iframe>');
        window.setTimeout(function() {
            document.addEventListener('mousedown', function(evt) {
                hide();
            }, false);
        }, 0);
        toggle();
    }

    function add(name, html) {
        var item;
        var item_button;

        item = document.createElement('div');
        item.className = 'item';
        item.innerHTML = html;
        dropdown.appendChild(item);
    }

    function toggle() {
        if (dropdown.parentNode === el)
            el.removeChild(dropdown);
        else
            el.appendChild(dropdown);
    }

    function hide() {
        if (dropdown.parentNode == el)
            el.removeChild(dropdown);
    }
}
