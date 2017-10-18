$(document).ready(function () {
    $('select.ui.dropdown').dropdown({});
    $('span.ui.dropdown').dropdown({});
    $('.message .close')
        .on('click', function () {
            $(this).closest('.message').transition('fade');
        });
    $('.ui.sidebar').sidebar({
        context: $('.pushable')
    }).sidebar('attach events', '.menu .item.sidebar-menu')
    ;
// $('.ui.sidebar').first()
//   .sidebar('attach events', '.menu .item.sidebar-menu')
// ;

});


function setLike(category) {
    // alert(category);
    var method = 'GET';
    var url = '/rango/category/like/';
    var data = category;

    $.ajax({
        type: method,
        url: url,
        data: {'category': data},
        success: function (data) {
            var message = data.message;
            var likes = data.likes;
            if (message == true) {

                $('#category-' + category).removeClass('outline');
                $('#a-category-likes-' + category).text(likes);
            }


        },
        error: function (data) {
            $('#category-' + category).removeClass('error');
        }
    });
    return false;
}

function removeLike(category) {
    // alert(category);
    var method = 'GET';
    var url = '/rango/category/remove/like/';
    var data = category;

    $.ajax({
        type: method,
        url: url,
        data: {'category': data},
        success: function (data) {
            var message = data.message;
            var likes = data.likes;
            if (message == true) {
                // alert("true");
                $('#category-' + category).addClass('outline');
                $('#a-category-likes-' + category).text(likes);
            }

        },
        error: function (data) {
            $('#category-' + category).removeClass('error');
        }
    });
    return false;
}