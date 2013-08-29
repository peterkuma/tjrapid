function AttachmentInline(el, prefix) {
    var module = {};
    var button;
    var form;

    init();

    function init() {
        if (typeof(el) === 'string') el = document.querySelector(el);

        button = document.createElement('button');
        button.className = 'attach';
        button.textContent = 'Attach file';
        button.type = 'button';
        el.appendChild(button);
        button.onclick = function() { module.attach(); };

        /* Hack: figure out parent form. */
        var input = document.createElement('input');
        input.style.display = 'none';
        el.appendChild(input);
        form = input.form;
        el.removeChild(input);

        form.onsubmit = submit;
    }

    function submit(event) {
        var attachments = module.attachments();
        total_forms(attachments.length);
        var data = new FormData(form);
        var i = initial_forms();
        attachments.forEach(function(attachment) {
            if (!attachment.file) return;
            var name = prefix + '-' + i + '-file';
            data.append(name, attachment.file);
            i++;
        });
        var req = new XMLHttpRequest();
        req.open('POST', form.action);
        req.send(data);
        req.onload = function() { window.location.reload(); };
        event.preventDefault();
    }

    function total_forms(n) {
        var input = el.querySelector('#id_' + prefix + '-TOTAL_FORMS');
        if (!arguments.length) return parseInt(input.value, 10);
        input.value = n;
    }

    function initial_forms(n) {
        var input = el.querySelector('#id_' + prefix + '-INITIAL_FORMS');
        if (!arguments.length) return parseInt(input.value, 10);
        input.value = n;
    }

    function next_index() {
        var input = el.querySelector('#id_' + prefix + '-TOTAL_FORMS');
        var i = parseInt(input.value, 10);
        input.value = i + 1;
        return i;
    }

    function available_name(name) {
        var names = module.attachments().map(function(x) { return x.name; });
        if (names.indexOf(name) === -1) return name;
        var n = name.lastIndexOf('.');
        var base = n >= 0 ? name.substring(0, n) : name;
        var suffix = n >= 0 ? name.substring(n) : '';

        var i = 1;
        var s = name;
        while (names.indexOf(s) >= 0) {
            s = base+'_'+i+suffix;
            i++;
        }
        return s;
    }

    function attach_file(file) {
        var div = document.createElement('div');
        div.className = 'inline-related';
        var a = document.createElement('a');
        a.textContent = available_name(file.name);
        a.href = window.URL.createObjectURL(file);
        a.__file__ = file;
        // var input = document.createElement('input');
        // input.type = 'file';
        // input.style.display = 'none';
        // input.name = prefix + '-' + next_index() + '-file';
        div.appendChild(a);
        el.insertBefore(div, button);
    }

    module.attachments = function() {
        var attachments = [];
        var divs = el.querySelectorAll('.inline-related');
        [].forEach.call(divs, function(div) {
            var a = div.querySelector('a');
            attachments.push({
                'name': a.textContent,
                'file': a.__file__
            });
        });
        return attachments;
    };

    module.attach = function() {
        var input = document.createElement('input');
        input.type = 'file';
        input.multiple = true;
        input.onchange = function() {
            [].forEach.call(input.files, function(file) {
                attach_file(file);
            });
        };
        input.click();
        return module;
    };

    return module;
}
