$(document).ready(function(){ 
    var searchBtn = $('#search-button');
    var searchForm = $('#search-form');

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });
});

$(document).ready(function(){
    $('#selectworkorder').select2();
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

/*
var Select2Cascade = ( function(window, $) {

    function Select2Cascade(parent, child, url, select2Options) {
        var afterActions = [];
        var options = select2Options || {};

        // Register functions to be called after cascading data loading done
        this.then = function(callback) {
            afterActions.push(callback);
            return this;
        };

        parent.select2(select2Options).on("change", function (e) {

            child.prop("disabled", true);
            var _this = this;
            
            $.getJSON(url.replace(':parentId:', $(this).val()), function(items) {
                var newOptions = '<option value="">-- Select --</option>';
                for(var id in items) {
                    newOptions += '<option value="'+ id +'">'+ items[id] +'</option>';
                }

                child.select2('destroy').html(newOptions).prop("disabled", false)
                    .select2(options);
                
                afterActions.forEach(function (callback) {
                    callback(parent, child, items);
                });
            });
        });
    }

    return Select2Cascade;

})( window, $);
*/