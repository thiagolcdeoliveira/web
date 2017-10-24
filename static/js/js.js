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

function set_like_category(category) {
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
                if (is_like) {
                    iconcategory.removeClass('gray');
                    // iconcategory.addClass('down');
                } else {
                    // category=$('#js-icon-category-' + category);
                    // iconcategory.removeClass('down');
                    iconcategory.addClass('gray');
                }
                likecategory = $('#js-count-likes-category-' + category);
                likecategory.text(likes);
                console.log("oi");
                // category.removeClass("right");

                // }
            }

        },
        error: function (data) {
            // $('#category-' + category).removeClass('error');
        }
    });
    return false;
}


function set_deslike_category(category) {
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
            var is_deslike = data.is_deslike;
            iconcategory = $('#js-icon-deslike-category-' + category);
            if (message) {
                if (is_deslike) {
                    iconcategory.removeClass('gray');
                } else {
                    iconcategory.addClass('gray');
                }
                deslikecategory = $('#js-count-deslikes-' + category);
                deslikecategory.text(deslikes);
                console.log("oi");
            }

        },
        error: function (data) {
            // $('#category-' + category).removeClass('error');
        }
    });
    return false;
}


function set_like_page(page) {
    // alert(category);
    var method = 'GET';
    var url = '/rango/page/like/';
    var data = page;
    var likepage;
    var iconpage;
    var page;
    alert("oi");
    $.ajax({
        type: method,
        url: url,
        data: {'page': data},
        success: function (data) {
            var message = data.message;
            var likes = data.likes;
            var is_like = data.is_like;
            iconpage = $('#js-icon-page-' + page);
            if (message) {
                if (is_like) {
                    iconpage.removeClass('gray');
                    // iconcategory.addClass('down');
                } else {
                    // category=$('#js-icon-category-' + category);
                    // iconcategory.removeClass('down');
                    iconpage.addClass('gray');
                }
                likepage = $('#js-count-likes-page-' + page);
                likepage.text(likes);
                console.log("oi");
                // category.removeClass("right");

                // }
            }

        },
        error: function (data) {
            // $('#category-' + category).removeClass('error');
        }
    });
    return false;
}


function set_deslike_page(page) {
    // alert(category);
    var method = 'GET';
    var url = '/rango/page/deslike/';
    var data = page;
    var deslikepage;
    var iconpage;
    // alert("oi");

    $.ajax({
        type: method,
        url: url,
        data: {'page': data},
        success: function (data) {
            var message = data.message;
            var deslikes = data.deslikes;
            var is_deslike = data.is_deslike;
            iconpage = $('#js-icon-deslike-page-' + page);
            if (message) {
                if (is_deslike) {
                    iconpage.removeClass('gray');
                } else {
                    iconpage.addClass('gray');
                }
                // alert(deslikes);
                deslikepage = $('#js-count-deslikes-page-' + page);
                deslikepage.text(deslikes);
                console.log("oi");
            }

        },
        error: function (data) {
            // $('#category-' + category).removeClass('error');
        }
    });
    return false;
}

