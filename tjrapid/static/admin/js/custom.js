function select2_osm() {
    fn = function(state) {
        if (!state.id) { return state.text; };
        return $('<span><img src="/static/osm/' + state.element.value + '.svg" style="width: 1em; height: 1em" /\> ' + state.text + '</span>');
    }
    $('#content-main .select2-osm').each(function() {
        if (this.id != 'id_mappoint_set-__prefix__-marker') {
            $(this).select2({templateResult: fn, templateSelection: fn});
        }
    });
}

$(document).ready(function(){
    $('.vLargeTextField').prop('cols', 80);
    $('.vLargeTextField').autosize();
    select2_osm();
});
