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
        .sidebar('setting', 'transition', 'overlay')
    ;
// $('.ui.sidebar').first()
//   .sidebar('attach events', '.menu .item.sidebar-menu')
// ;

});

// function set_like(category) {
//     // alert(category);
//     var method = 'GET';
//     var url = '/rango/category/like/';
//     var data = category;
//     var likecategory;
//     var iconcategory;
//     var category;
//     $.ajax({
//         type: method,
//         url: url,
//         data: {'category': data},
//         success: function (data) {
//             var message = data.message;
//             var likes = data.likes;
//             var is_like = data.is_like;
//             iconcategory = $('#js-icon-category-' + category);
//
//             if (message) {
//                 //
//                 // $('#category-' + category).removeClass('outline');
//                 // console.e(data);
//                 // console(data.message);
//                 // console(data.message);
//                 // if (is_like) {
//                 // inconcategory = $('#js-icon-category-' + category);
//                 iconcategory.removeClass('up outline');
//                 iconcategory.addClass('down');
//             } else {
//                 // category=$('#js-icon-category-' + category);
//                 iconcategory.removeClass('down');
//                 iconcategory.addClass('up outline');
//             }
//             likecategory = $('#js-count-likes-' + category);
//             likecategory.text(likes);
//             // category= $('#js-like-' + category);
//             // category.innerHTML="<a>deucerto</a>";
//             console.log("oi");
//             // category.removeClass("right");
//
//             // }
//
//
//         },
//         error: function (data) {
//             $('#category-' + category).removeClass('error');
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
                iconcategory.removeClass('gray');
                // iconcategory.addClass('down');
            } else {
                // category=$('#js-icon-category-' + category);
                // iconcategory.removeClass('down');
                iconcategory.addClass('gray');
            }
            likecategory = $('#js-count-likes-' + category);
            likecategory.text(likes);
            console.log("oi");
            // category.removeClass("right");

            // }


        },
        error: function (data) {
            // $('#category-' + category).removeClass('error');
        }
    });
    return false;
}


function set_deslike(category) {
    // alert(category);
    var method = 'GET';
    var url = '/rango/category/deslike/';
    var data = category;
    var deslikecategory;
    var iconcategory;
    $.ajax({
        type: method,
        url: url,
        data: {'category': data},
        success: function (data) {
            var message = data.message;
            var deslikes = data.deslikes;
            var is_like = data.is_deslike;
            iconcategory = $('#js-icon-deslike-category-' + category);
            if (message) {
                iconcategory.removeClass('gray');
            } else {
                iconcategory.addClass('gray');
            }
            deslikecategory = $('#js-count-deslikes-' + category);
            deslikecategory.text(deslikes);
            console.log("oi");


        },
        error: function (data) {
            // $('#category-' + category).removeClass('error');
        }
    });
    return false;
}

