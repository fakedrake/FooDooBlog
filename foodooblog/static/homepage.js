
function add_handlers() {
    $(".delete-post-link").click(function (){
	$list_item = $(this).closest(".post-view-link");
	$titlediv = $list_item.find("div.post-title");
	$name = $titlediv.attr('id');

	$('<div>', {title:"Delete Post", text: "Really delete the post: "+$titlediv.text()+"?"})
	    .dialog({
		resizable: false,
		modal: true,
		buttons: {
		    "Delete": function() {
			// $.post("delete", JSON.stringify({type: 'post', name: $name,  contentType: 'application/json; charset=utf-8'}));
			jQuery.ajax({type:'POST',
				     url: 'http://localhost:6543/delete', // the pyramid server
				     data: JSON.stringify({'type':'post', 'name':$name}),
 				     contentType: 'application/json; charset=utf-8',
				     dataType: "json",
				     success: function (data) {
					 if(data["deletion_status"] == "success") { $list_item.closest("li").detach() }
					 else {alert("error while deleting:" + data.msg);}
				     }
				    });

			$( this ).dialog( "close" );
		    },
		    Cancel: function() {
			$( this ).dialog( "close" );
		    }
		}
	    })
    });
}

$(".post-list-item").hover(
    function () {
	var $post_control = $("<div>", {class: "post-control"})
	$("<a>", {text: "Delete", class: "delete-post-link", href: "#"}).appendTo($post_control)
	$post_control.append(" ");
	$("<a>", {text: "Edit", class: "edit-post-link", href: $(this).find("a.postlink").attr("href")+"/edit"}).appendTo($post_control)
	$(this).find("div").append($post_control);
	add_handlers();
    },
    function () {
	$(this).find(".post-control").remove();
    }
);

//li with fade class
// $("li.fade").hover(function(){$(this).fadeOut(100);$(this).fadeIn(500);});
