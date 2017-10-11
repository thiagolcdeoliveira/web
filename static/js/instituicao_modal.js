$(document).ready(function () {
    $('#adiconar_instituicao').click(function () {
        $('.ui.modal')
            .modal({
                onDeny: function () {
                    deny     : '.negative, .deny, .cancel'
                },
                onApprove: function () {
                    approve  : '.positive, .approve, .ok'
                }
            })
            .modal('show');
    });
});