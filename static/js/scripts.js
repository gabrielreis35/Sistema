$(document).ready(function(){ 
    var searchBtn = $('#search-button');
    var searchForm = $('#search-form');

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });
});

$(document).on('click', '.confirm-delete', function(){
    return confirm("Tem certeza que deseja apagar este produto?");
})
// function searchFunction() {
//     var input, filter, table, tr, td, i, txtValue;
//     input = document.getElementById('search');
//     filter = input.value.toUpperCase();
//     table = document.getElementById('tab-products');
//     tr = ul.getElementsByTagName('tr');

//     for (i = 0; i < td.length; i++) {
//         td = tr[i].getElementsByTagName("td")[0];
//         txtValue = td.textContent || td.innerText;
//         if (txtValue.toUpperCase().indexOf(filter) > -1) {
//             tr[i].style.display = "";
//         }
//         else {
//             tr[i].style.display = "none";
//         }
//     }
// }