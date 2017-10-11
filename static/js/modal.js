$(document).ready(function () {
    $('#adicionar-autor').click(function () {
        $('.ui.modal')
            .modal({
                closable: false,
                onDeny: function () {
                    $('.ui.modal').modal('hide');
                },
            })
            .modal('show');
    });
});