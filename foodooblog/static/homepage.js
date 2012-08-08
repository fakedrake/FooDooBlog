
function add_handlers() {
    $(".delete-post-link").click(function (){
	$list_item = $(this).closest("div.post-list-item");
	$title = $list_item.find("a.postlink").text();
	$name = $list_item.attr('id');

	$('<div>', {title:"Delete Post", text: "Really delete the post: "+$title+"?"})
	    .dialog({
		resizable: false,
		modal: true,
		buttons: {
		    "Delete": function() {
			//			$.post("delete", JSON.stringify({type: 'post', name: $name,  contentType: 'application/json; charset=utf-8'}));
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

$("li").hover(
    function () {
	var $post_control = $("<span>", {class: "post-control", text: " - "})
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
