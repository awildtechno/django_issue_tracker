// Constants
var autocomplete_lists = new Object();
// Development test data constants
autocomplete_lists[".nav-search"] = ["django-", "server-", "sandbox-", "test-", "production-", "aws-", "python-", "timesheets-", "java-", "spring-", "flask-"].sort();
autocomplete_lists["#category"] = ["django", "server", "sandbox", "test", "production", "aws", "python", "timesheets", "java", "spring", "flask"].sort();

$(document).ready(function() {
    $("#severity").on("keyup keydown", function(e) {
        if (e.originalEvent.key.match(/0|[6-9]|\D+/g) || $('#severity').val().length >= 1) {
            if (e.originalEvent.keyCode != 8 && e.originalEvent.keyCode != 46) {
                // Backspace and delete are ok I guess
                e.preventDefault();
            }
        }
        //filter pastes
        $('#severity').val(
            $('#severity').val().replace(/0|[6-9]|\D/g, '')
        );
        //enforce length = 1
        if ($('#severity').val().length > 1) {
            $('#severity').val($('#severity').val().substring(0, 1));
        }
    });

    $('textarea#shortdesc, input#category').keyup(function(e) {
        console.log(e);
        $('.issue-inner').html(
            '<h4>'
            + $('#category').val()
            + '-###</h4>'
            + $('#shortdesc').val()
            );
    });

    Object.keys(autocomplete_lists).forEach(function(key) {
        $(key).autocomplete({
            source: autocomplete_lists[key],
            autoFocus: true,
        });
    });
});