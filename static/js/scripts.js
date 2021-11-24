$(document).ready(function(){ 
    var searchBtn = $('#search-button');
    var searchForm = $('#search-form');

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });
});

// $(document).on('click', '.confirm-delete', function(){
//     return confirm("Tem certeza que deseja apagar este produto?");
// };

// function confirmButton() {
//     var confirm = confirm("Deseja continuar com a ação?");
//     if (confirm == true) {
//         document.write("Ação feita com sucesso!");
//         return true;
//     }
//     else {
//         document.write("Ação cancelada com sucesso!");
//         return false;
//     }
// }
