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

//
// function setLike(category) {
//     alert(category);
//     var method = 'GET';
//     var url = '/rango/category/like/';
//     var data = category;
//     var likecategory;
//     var inconcategory;
//     var category;
//     $.ajax({
//         type: method,
//         url: url,
//         data: {'category': data},
//         success: function (data) {
//             var message = data.message;
//             var likes = data.likes;
//             if (message == true) {
//
//                 // $('#category-' + category).removeClass('outline');
//                 inconcategory=$('#js-icon-category-' + category);
//                 inconcategory.removeClass('up outline');
//                 inconcategory.addClass('down');
//                 likecategory= $('#js-count-likes-' + category);
//                 likecategory.text(likes);
//                 category= $('#js-like-' + category);
//                 // category.innerHTML="<a>deucerto</a>";
//                 console.log("oi");
//                 // category.removeClass("right");
//
//             }
//
//
//         },
//         error: function (data) {
//             $('#category-' + category).removeClass('error');
//         }
//     });
//     return false;
// }
//
// function removeLike(category) {
//     // alert(category);
//     var method = 'GET';
//     var url = '/rango/category/remove/like/';
//     var data = category;
//     var category;
//     $.ajax({
//         type: method,
//         url: url,
//         data: {'category': data},
//         success: function (data) {
//             var message = data.message;
//             var likes = data.likes;
//             if (message == true) {
//                 // alert("true");
//                 category=$('#js-icon-category-' + category);
//                 category.removeClass('down');
//                 category.addClass('up outline');
//                 // $('#js-icon-category-' + category).addClass('outline');
//                 $('#js-count-likes-' + category).text(likes);
//             }
//
//         },
//         error: function (data) {
//             $('#js-category-' + category).removeClass('error');
//         }
//     });
//     return false;
// }
function set_like(category) {
    // alert(category);
    var method = 'GET';
    var url = '/rango/category/like/';
    var data = category;
    var likecategory;
    var iconcategory;
    var category;
    $.ajax({
        type: method,
        url: url,
        data: {'category': data},
        success: function (data) {
            var message = data.message;
            var likes = data.likes;
            var is_like = data.is_like;
            iconcategory = $('#js-icon-category-' + category);

            if (message) {
                //
                // $('#category-' + category).removeClass('outline');
                // console.e(data);
                // console(data.message);
                // console(data.message);
                // if (is_like) {
                // inconcategory = $('#js-icon-category-' + category);
                iconcategory.removeClass('up outline');
                iconcategory.addClass('down');
            } else {
                // category=$('#js-icon-category-' + category);
                iconcategory.removeClass('down');
                iconcategory.addClass('up outline');
            }
            likecategory = $('#js-count-likes-' + category);
            likecategory.text(likes);
            // category= $('#js-like-' + category);
            // category.innerHTML="<a>deucerto</a>";
            console.log("oi");
            // category.removeClass("right");

            // }


        },
        error: function (data) {
            $('#category-' + category).removeClass('error');
        }
    });
    return false;
}