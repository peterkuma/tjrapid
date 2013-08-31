function AttachmentInline(el, prefix) {
    var module = {};
    var data = [];
    var dirty = false;
    var orig_el;
    var form;

    init();

    function init() {
        if (typeof(el) === 'string') el = d3.select(el);

        data = parse_initial();

        orig_el = el;
        el = d3.select(orig_el.node().parentNode).insert('div')
            .attr('id', orig_el.attr('id'))
            .attr('class', orig_el.attr('class'));
        orig_el.remove();

        el.append('h2')
            .text('Attachments');

        el.append('div')
            .attr('class', 'errornote')
            .style('display', 'none');

        el.append('div')
            .attr('class', 'note')
            .style('display', 'none');

        // el.append('input')
        //     .attr('type', 'hidden')
        //     .attr('id', 'id_'+prefix+'-TOTAL_FORMS')
        //     .attr('name', prefix+'-TOTAL_FORMS')
        //     .attr('value', data.length);
        // el.append('input')
        //     .attr('type', 'hidden')
        //     .attr('id', 'id_'+prefix+'-INITIAL_FORMS')
        //     .attr('name', prefix+'-INITIAL_FORMS')
        //     .attr('value', data.length);
        // el.append('input')
        //     .attr('type', 'hidden')
        //     .attr('id', 'id_'+prefix+'-MAX_NUM_FORMS')
        //     .attr('name', prefix+'-MAX_NUM_FORMS')
        //     .attr('value', 1000);

        el.append('div').attr('class', 'list');

        var button = el.append('input')
            .attr('type', 'submit')
            .attr('class', 'attach')
            .attr('value', 'Attach file')
            .on('click', function() {
                d3.event.preventDefault();
                module.attach();
            });

        /* Hack: figure out parent form. */
        form = button.node().form;

        document.addEventListener('DOMContentLoaded', function() {
            d3.select(form).selectAll('.submit-row > input[type="submit"]')
                .on('click', function() {
                    d3.event.preventDefault();
                    submit(d3.select(this));
                });
        });
        //form.onsubmit = submit;

        update();
    }

    function parse_initial() {
        var attachments = el.selectAll('input[type="file"]')
            .filter(function() {
                return this.parentNode.querySelector('a');
            })
            [0].map(function(node) {
                var name = node.name.substring(0, node.name.lastIndexOf('-'));
                var url = d3.select(node.parentNode).select('a').attr('href');
                var filename =  url.substring(url.lastIndexOf('/')+1);
                return {
                    'name': name,
                    'id': el.select('#id_'+name+'-id').attr('value'),
                    'url': url,
                    'filename': filename
                };
            });
        return attachments;
    }

    function error(msg) {
        if (!arguments.length) return error.msg;
        error.msg = msg;
        note(null);
        el.select('.errornote')
            .style('display', msg !== null ? 'block' : 'none')
            .text(msg);
    }
    error.msg = null;

    function note(msg) {
        if (!arguments.length) return this.msg;
        error.msg = msg;
        // if (error() !== null) return;
        el.select('.note')
            .style('display', msg !== null ? 'block' : 'none')
            .text(msg);
    }
    note.msg = null;

    function update() {
        // el.select('#id_'+prefix+'-TOTAL_FORMS')
        //     .attr('value', data.length);

        var attachment = el.select('.list').selectAll('.attachment')
            .data(data.filter(function(d) { return !d.remove; }),
                  function(d) { return d.name; })
            .attr('class', 'attachment');

        var new_attachment = attachment.enter()
            .append('div')
            .attr('class', 'attachment');

        new_attachment.append('a')
            .text(function(d) { return d.filename; })
            .attr('href', function(d) {
                if (d.file) return window.URL.createObjectURL(d.file);
                return d.url;
            });

        new_attachment.append('div')
            .attr('class', 'delete')
            .on('click', function(d) {
                dirty = true;
                if (d.file) data.splice(data.indexOf(d), 1);
                else d.remove = true;
                update();
            });

        attachment.exit().remove();

        // var input_delete = el.selectAll('input.delete')
        //     .data(data.filter(function(d) { return d.remove; }),
        //           function(d) { return d.name; });

        // input_delete.enter().append('input')
        //     .attr('type', 'hidden')
        //     .attr('class', 'delete')
        //     .attr('name', function(d) { return d.name+'-DELETE'; })
        //     .attr('value', 'on');

        // input_delete.exit().remove();
    }

    function submit(button) {
        if (!dirty) {
            orig_el.style('display', 'none');
            el.node().parentNode.insertBefore(orig_el.node(), el.node());
            button.on('click', null);
            button.node().click();
            return;
        }

        var form_data = new FormData(form);

        var initial_forms = data.filter(function(d) { return d.id; }).length;

        form_data.append(prefix+'-TOTAL_FORMS', data.length);
        form_data.append(prefix+'-INITIAL_FORMS', initial_forms);
        form_data.append(prefix+'-MAX_NUM_FORMS', 1000);

        data.forEach(function(d) {
            if (d.remove) {
                form_data.append(d.name+'-DELETE', 'on');
            }
            form_data.append(d.name+'-file', d.file ? d.file : '');
            form_data.append(d.name+'-id', d.id ? d.id : '');
        });

        form_data.append('_continue', '');

        var req = new XMLHttpRequest();
        req.open('POST', form.action);
        req.responseType = 'document';
        req.upload.onprogress = function(evt) {
            var percent = Math.round(100.0*evt.loaded/evt.total);
            note('Uploading... '+percent+'%');
        };
        req.onload = function() {
            if (req.readyState != 4) return;
            if (req.status !== 200) {
                error('Request failed');
                return;
            }
            note('Uploading... 100%');
            var newel = d3.select(req.response.getElementById(el.node().id));
            newel.style('display', 'none');
            el.node().parentNode.insertBefore(newel.node(), el.node());
            //form.onsubmit = undefined;
            //form.elements['_continue'].click();
            button.on('click', null);
            button.node().click();
            // window.location.reload();
        };
        req.onerror = function() {
            error('Request failed');
        };
        req.send(form_data);
        note('Uploading... 0%');
    }

    function available_name(name) {
        var names = data.map(function(d) { return d.filename; });
        var n = name.lastIndexOf('.');
        var base = n >= 0 ? name.substring(0, n) : name;
        var suffix = n >= 0 ? name.substring(n) : '';
        var i = 1;
        while (names.indexOf(name) >= 0) {
            name = base+'_'+i+suffix;
            i++;
        }
        return name;
    }

    function attach_file(file) {
        dirty = true;
        data.push({
            'name': prefix+'-'+data.length,
            'file': file,
            'filename': available_name(file.name)
        });
        update();
    }

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
