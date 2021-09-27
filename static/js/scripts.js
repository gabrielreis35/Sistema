$(document).ready(function(){ 
    var searchBtn = $('#search-button');
    var searchForm = $('#search-form');

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });
});