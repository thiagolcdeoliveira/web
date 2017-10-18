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
    alert(category);
    var method = 'GET';
    var url = '/rango/category/like/';
    var data = category;
    var likecategory;
    var acategory;
    var category;
    $.ajax({
        type: method,
        url: url,
        data: {'category': data},
        success: function (data) {
            var message = data.message;
            var likes = data.likes;
            if (message == true) {

                // $('#category-' + category).removeClass('outline');
                category=$('#js-icon-category-' + category);
                category.removeClass('up outline');
                category.addClass('down');
                likecategory= $('#js-count-likes-' + category);
                likecategory.text(likes);
                // acategory.changeonclick=removeLike(category);
                // acategory.onclick=function() { removeLike(category); };
                // acategory.setAttribute('onclick',"'removeLike("+category+")'");
                // acategory = $('#js-a-category-' + category);
                // acategory.onclick=function() { removeLike(category); };
                // acategory.change=function() { removeLike(category); };
                // acategory.text("bbblabal");
                // acategory.onclick=function() { removeLike(category); };

                // acategory.setAttribute('onclick','removeLike()');
                //this.text(likes);
                // $('#a-category-likes-' + category).onRemoveClick();
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
    var category;
    $.ajax({
        type: method,
        url: url,
        data: {'category': data},
        success: function (data) {
            var message = data.message;
            var likes = data.likes;
            if (message == true) {
                // alert("true");
                category=$('#js-icon-category-' + category);
                category.removeClass('down');
                category.addClass('up outline');
                // $('#js-icon-category-' + category).addClass('outline');
                $('#js-count-likes-' + category).text(likes);
            }

        },
        error: function (data) {
            $('#js-category-' + category).removeClass('error');
        }
    });
    return false;
}