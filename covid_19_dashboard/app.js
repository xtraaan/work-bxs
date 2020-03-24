"use strict";

// Run local server in order to fetch JSON file
// Ex. Use Python, python -m http.server 8000
$(document).ready(function() {
    var $select = $('#state');
    $.getJSON('covid-19_weekly-modified-json.json', function(data) {
        $select.html('<option value="" disabled selected>Select a state</option>');
        for (var i = 0; i < data['data'].length; i++) {
            $select.append('<option id="state' + data['data'][i]['index'] + '">' + data['data'][i]["Province\/State"] + '</option>');
        }
    });
});