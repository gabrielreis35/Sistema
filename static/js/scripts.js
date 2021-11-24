$(document).ready(function(){ 
    var searchBtn = $('#search-button');
    var searchForm = $('#search-form');

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });
});

function confirmButton() {
    var confirm = confirm("Deseja continuar com a ação?");
    if (confirm == true) {
        document.write("Ação feita com sucesso!");
        return true;
    }
    else {
        document.write("Ação cancelada com sucesso!");
        return false;
    }
}